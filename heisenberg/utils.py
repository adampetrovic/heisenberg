import boto.ec2
import json


class BotoEC2Helper(object):

    instance_filter = [
        'id',
        'ip_address',
        'dns_name',
        'instance_type',
        'tags'
    ]

    ec2_filter = {
        'instance-state-name': 'running'
    }

    def __init__(self, access_key, secret_key, region, cache_file):
        self.access_key = access_key
        self.secret_key = secret_key
        self.region = region
        self.cache_file = cache_file

        try:
            self.cache = json.load(open(self.cache_file, 'rb'))
        except (IOError, ValueError):
            self.cache = None

    def connect(self):
        self.conn = boto.ec2.connect_to_region(
            self.region,
            aws_access_key_id=self.access_key,
            aws_secret_access_key=self.secret_key,
        )

    def _boto_fetch(self):
        instances = []
        filter_fun = lambda x: x[0] in self.instance_filter

        for res in self.conn.get_all_instances(filters=self.ec2_filter):
            for instance in res.instances:
                instances.append(dict(
                    filter(filter_fun, instance.__dict__.iteritems())
                ))
        return instances

    def _refresh_cache(self):
        self.cache = self._boto_fetch()
        json.dump(self.cache, open(self.cache_file, 'wb'))

    def fetch_all(self, fresh=False):
        if fresh or not self.cache:
            self._refresh_cache()
        return self.cache
