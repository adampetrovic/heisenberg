Heisenberg
----------

Overview
--------

A better EC2 search / SSH utility

Installation
------------

Clone this repository and run:

```
python setup.py install
```

Configuration
-------------
The default configuration should be placed in ~/.heisenberg, it should contain:

```
[aws]
access_key=<AWS_ACCESS_KEY>
secret_key=<AWS_SECRET_KEY>
```

Usage
-----

```
usage: ec2 [-h] [-c FILE] [-z FILE] [-r] [--access-key AWS_ACCESS_KEY]
           [--secret-key AWS_SECRET_KEY]
           {find,ssh,cmd} ...

A utility for searching and connecting to EC2 instances

positional arguments:
  {find,ssh,cmd}
    find                List all the EC2 instances that match a pattern
    ssh                 Connect to EC2 host(s)
    cmd                 Run command(s) on matching EC2 host(s)

optional arguments:
  -h, --help            show this help message and exit
  -c FILE, --config FILE
                        Configuration file
  -z FILE, --cache-file FILE
                        Cache file
  -r, --refresh         Refresh internal AWS instance cache
  --access-key AWS_ACCESS_KEY
                        AWS Access Key
  --secret-key AWS_SECRET_KEY
                        AWS Secret Key
```

*NOTE*: The first search run will take a little while, as the Heisenberg cache is being built.
Successive runs will be instant, as they are read locally. To refresh the cache, use the -r, --refresh
flag before your command. i.e. ```ec2 -r find auth```


Further Help
------------

To display more detailed, command-specific help, use the -h flag after the command. For example:

```
ec2 find -h
usage: ec2 find [-h] [-s SORT_KEY] [-p SEARCH_KEY] search_pattern

positional arguments:
  search_pattern        A search pattern

optional arguments:
  -h, --help            show this help message and exit
  -s SORT_KEY, --sort-key SORT_KEY
                        The column to sort results
  -p SEARCH_KEY, --search-key SEARCH_KEY
                        The column to choose when searching
```
