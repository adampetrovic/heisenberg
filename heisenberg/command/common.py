class CommonCommand(object):

    @classmethod
    def search(self, instance, search_key, pattern):
        pattern = pattern.lower()
        if pattern == "*":
            return True

        if pattern in instance.get(search_key, '').lower():
            return True

        return False

    def sort(self, instances, sort_key):
        return sorted(
            instances, key=lambda i: i.get(sort_key).lower()
        )

    def prepare_output(self, keys, instances):
        output_instances = []
        for i, instance in enumerate(instances):
            output_instances.append([i] + [instance.get(key) for key in keys])

        return output_instances
