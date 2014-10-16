import sys
import string


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
        while len(instances) > 1:
            try:
                host_input = raw_input(">> Please choose the instances(s) [0-%d]: " % (
                    len(instances)-1
                )).strip()

                if host_input == "all":
                    break
                choices = []
                # strip each element in comma separated input (1 element if no ,)
                comma_input = map(string.strip, host_input.split(','))
                for id in comma_input:
                    # check if range approach
                    if "-" in id:
                        # extract out start and end and cast to int
                        start, end = map(int, id.split("-", 1))
                        for i in instances[start:end+1]:
                            choices.append(i)
                    else:
                        choices.append(instances[int(id)])

                # function returns a list of instances, so if only one instance
                # return the list
                return choices
            except (ValueError, IndexError):
                continue
            except KeyboardInterrupt:
                sys.exit(0)

        return instances
