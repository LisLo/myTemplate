import os
import sys
# find root dir
root_path = os.path.split((os.path.dirname(__file__)))[0]
# set root
sys.path.append(root_path)
from Source.Config.get_input import GetInput


class Main(GetInput):
    def execute_workflow(self):
        print(self.a + self.b)

my_code = Main(__file__)
my_code.execute_workflow()
