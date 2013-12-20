import sys


class BaseCommand(object):

    def __init__(self, boto_conn):
        self.boto = boto_conn

    def execute(self):
        raise NotImplemented("Function must be implemented by parent class")

    def set_output(self, output_class):
        self.output = output_class

    def draw_output(self):
        self.output.draw()

    @classmethod
    def search(self, instance, search_key, pattern):
        pattern = pattern.lower()
        if pattern == "*":
            return True

        if pattern in instance.get(search_key, '').lower():
            return True

        return False

    @classmethod
    def sort(self, instances, sort_key):
        return sorted(
            instances, key=lambda i: i.get(sort_key).lower()
        )

    @classmethod
    def prepare_output(self, keys, instances):
        output_instances = []
        for i, instance in enumerate(instances):
            output_instances.append([i] + [instance.get(key) for key in keys])

        return output_instances

    @classmethod
    def select_hosts(self, instances):
        if len(instances) > 1:
            while True:
                try:
                    host_input = raw_input(">> Please choose the instances(s) [0-%d]: " % (
                        len(instances)-1
                    )).strip()

                    if host_input == "all":
                        break

                    choices = []
                    for id in (i.strip() for i in host_input.split(',')):
                        if "-" in id:
                            start, end = map(int, id.split("-", 1))
                            for i in instances[start:end+1]:
                                choices.append(i)
                        else:
                            id = int(id)
                            choices.append(instances[id])

                    return choices
                except (ValueError, IndexError):
                    continue
                except KeyboardInterrupt:
                    sys.exit(0)

        return instances
