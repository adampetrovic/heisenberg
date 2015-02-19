import heisenberg.command as commands
import heisenberg.interface as interfaces
from heisenberg.utils import BotoEC2Helper


class Heisenberg(object):

    def __init__(self, args):
        self.commands = dict(
            find=commands.FindCommand,
            ssh=commands.SSHCommand,
            cmd=commands.SSHCommand,
            local=commands.SSHCommand,
        )

        self.args = args

        self.boto_conn = BotoEC2Helper(
            access_key=args.access_key,
            secret_key=args.secret_key,
            region=args.region,
            cache_file=args.cache_file,
        )

        self.boto_conn.connect()

    def get_command(self):
        return self.commands[self.args.command]

    def execute_command(self):
        command_class = self.get_command()
        command = command_class(self.boto_conn)
        command.set_output(interfaces.AsciiTable)
        return command.execute(self.args)


class Test: pass



if __name__ == "__main__":


    a = Test()
    a.access_key = "accesskey"
    a.secret_key = "secretkey"
    a.cache_file = "/home/adam/.heisenberg_cache"
    a.command = "ssh"

    a.sort_key = "role"
    a.search_key = "name"
    a.search_pattern = "auth"

    a.refresh = False

    heisen = Heisenberg(a)
    heisen.execute_command()
