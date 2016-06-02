from helper import bcolors

people_alive = list()
original_circle = list()
people_dead = list()
verbose = False
test_pass = True
rounds = 0
last_killer = -1


def init_tests(N):
    """
        Sets up test environment

    """
    global original_circle
    global people_alive
    people_alive = range(1, N + 1, 1)
    original_circle = people_alive
    print "**********************************************"
    print "LOGICAL TESTS SECTION"
    print "**********************************************"


def dead_men_dont_kill(killer):
    global people_dead
    global test_pass

    if killer in people_dead:
        print bcolors.FAIL + "DEAD PEOPLE DON'T KILL"
        print bcolors.WARNING + str(killer) + " is dead and attempted to kill !"
        test_pass = False


def men_cant_be_alive_dead(person):
    global people_alive
    global people_alive
    global test_pass

    if person in people_alive and person in people_dead:
        print bcolors.FAIL + "PEOPLE CANT BE BOTH ALIVE AND DEAD"
        print bcolors.WARNING + str(person) + " is dead and alive !"
        test_pass = False


def men_outside_circle(person):
    global original_circle
    global test_pass

    if person not in original_circle:
        print bcolors.FAIL + "PEOPLE NOT IN CIRCLE CANT PLAY THE GAME"
        print bcolors.WARNING + str(person) + " is not in the circle  !"
        test_pass = False


def is_he_already_dead(killed):
    global people_dead
    global test_pass
    if killed in people_dead:
        print bcolors.FAIL + "DEAD PEOPLE CAN'T BE KILLED"
        print bcolors.WARNING + str(killed) + " is already dead !"
        test_pass = False
        return False
    else:
        return True


def update_dead(killed):
    """
    Works with lists to maintain track of status of each person , per kill
    """
    global people_alive
    global people_dead


    people_dead.append(killed)
    people_alive.remove(killed)

    print bcolors.HEADER + str(killed) + " removed"

    men_cant_be_alive_dead(killed)


def kill_only_to_left(killer, killed):
    legal_kill = -1
    global people_alive
    global people_dead
    global test_pass
    global rounds
    global last_killer

    length = len(people_alive)
    loc = people_alive.index(killer)
    if loc == length - 1:
        legal_kill = people_alive[0]

    else:
        legal_kill = people_alive[loc + 1]
    if verbose:
        print bcolors.OKBLUE + str(people_alive)
        print bcolors.ENDC + "Killer:" + str(killer)
        print bcolors.HEADER + "LEGAL KILL: " + str(legal_kill)
        print "\n"

    if killer > killed:
        rounds = rounds + 1
    elif killer < last_killer:
        rounds = rounds + 1
        print "*********************************"
    last_killer = killer

    if killed != legal_kill:
        print bcolors.FAIL + "LEFT KILL RULE VOILATED"
        print bcolors.WARNING + str(killer) + " TRIED TO KILL" + str(killed) + '\n'
        # print bcolors.WARNING + str(people_alive)
        test_pass = False


def new_person_dead(person):
    global people_dead
    global test_pass
    if person in people_dead:
        print bcolors.FAIL + "DEAD PEOPLE DON'T CARRY SWORDS"
        print bcolors.WARNING + str(person) + " is dead and attempted to take the sword!"
        test_pass = False


def suicide_is_illegal(killer, killed):
    if killer == killed:
        print bcolors.FAIL + "SANE PEOPLE DON'T KILL THEMSELVES"
        print bcolors.WARNING + str(killer) + " is trying to kill himself!"


def is_everyone_dead(alive):
    global people_alive
    if (len(people_alive) != 1):
        print bcolors.FAIL + "EVERYONE ISN'T DEAD YET !"
        print bcolors.WARNING + str(people_alive) + " ARE STILL ALIVE!"


def winner_is_not_dead(alive):
    global people_dead
    if alive in people_dead:
        print bcolors.FAIL + "THE WINNER IS DEAD :(!"
        print bcolors.WARNING + str(alive) + " IS DEAD"




def reset_data():
    """
    Clean up

    """
    global people_alive
    global original_circle
    global people_dead
    global verbose
    global test_pass
    global rounds
    global last_killer

    people_alive = []
    original_circle = []
    people_dead = []
    verbose = False
    test_pass = True
    rounds = 0
    last_killer = -1
