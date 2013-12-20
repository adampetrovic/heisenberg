from collections import OrderedDict
from heisenberg.command import BaseCommand

import subprocess
import sys


class SSHCommand(BaseCommand):

    output_keys = OrderedDict([
        ('name', 'Name'),
        ('id', 'Instance ID'),
        ('dns_name', 'EC2 Name'),
        ('instance_type', 'Instance Type'),
        ('role', 'Role'),
    ])

    def ssh_host(self, instances):
        for instance in instances:
            print ">> Connecting to: \033[92m{name} - {dns}\033[0m".format(
                name=instance.get("name", "unknown"),
                dns=instance.get("dns_name")
            )

            subprocess.call([
                'ssh',
                instance.get('dns_name'),
            ])

        sys.exit(0)

    def ssh_cmd_host(self, instances, command):
        for instance in instances:
            print ">> Performing command \033[93m'{cmd}'\033[0m on \033[92m{name} - {dns}\033[0m".format(
                cmd=command,
                name=instance.get('name', 'unknown'),
                dns=instance.get('dns_name', 'dns_name')
            )

            result = subprocess.call([
                'ssh',
                instance.get('dns_name'),
                command
            ])

        sys.exit(0)

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
            sys.stderr.write("\033[91mERROR:\033[0m No instances found\n")
            sys.exit(1)

        self.draw_output()
        hosts = self.select_hosts(sorted_instances)

        if args.command == "ssh":
            self.ssh_host(hosts)
        elif args.command == "cmd":
            self.ssh_cmd_host(hosts, args.ssh_command)
