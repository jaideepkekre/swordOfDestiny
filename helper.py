import sword
class bcolors:
    """Pretty colours for the terminal"""

    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def run_unit_test():
    print "\nRunning in Unit Test Mode "

    print bcolors.OKBLUE+"\nTesting input via equivalence partitioning \n"

    print bcolors.OKBLUE + "\nTesting character input"
    sword.create_circle("ABc")

    print bcolors.OKBLUE + "\nTesting alphanumeric input"
    sword.create_circle("ABc123")

    print bcolors.OKBLUE + "\nTesting numbers smaller than or equal to  0"
    sword.create_circle(0)

    print bcolors.OKBLUE + "\nTesting numbers greater than 0 and odd numbers"
    sword.create_circle(101)

    print bcolors.OKBLUE + "\nTesting  even numbers "
    sword.create_circle(100)

    print bcolors.OKBLUE + "\nTesting  input type"
    sword.create_circle("123")

    print bcolors.OKBLUE + "\nTesting  initial sword positions with input as 100 "

    print bcolors.OKBLUE+"\nSword at : -1 "
    sword.initial_sword_given_to=-1
    sword.create_circle(100)

    print bcolors.OKBLUE+"\nSword at : 101 "
    sword.initial_sword_given_to = 101
    sword.create_circle(100)

    print bcolors.OKBLUE+"\nSword at : 100 "
    sword.initial_sword_given_to = 100
    sword.create_circle(100)

    print bcolors.OKBLUE+"\nSword at : 1 "
    sword.initial_sword_given_to = 1
    sword.create_circle(100)
    exit()
