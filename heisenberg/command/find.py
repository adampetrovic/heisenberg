import sys

from heisenberg.command import BaseCommand
from collections import OrderedDict


class FindCommand(BaseCommand):

    output_keys = OrderedDict([
        ('name', 'Name'),
        ('id', 'Instance ID'),
        ('dns_name', 'EC2 Name'),
        ('instance_type', 'Instance Type'),
        ('role', 'Role'),
    ])

    def execute(self, args):
        instances = self.boto.fetch_all(
            fresh=args.refresh
        )

        self.output = self.output(
            header=['#'] + self.output_keys.values()
        )

        matched_instances = []
        for instance in instances:
            instance['name'] = instance['tags'].get('Name', "")
            instance['role'] = instance['tags'].get('role', "")

            if self.search(instance, args.search_key, args.search_pattern):
                matched_instances.append(instance)

        sorted_instances = self.sort(matched_instances, args.sort_key)

        self.output.add_rows(
            self.prepare_output(self.output_keys.keys(), sorted_instances)
        )

        if not len(sorted_instances):
            sys.stderr.write("No instances found")
            sys.exit(1)

        self.draw_output()
