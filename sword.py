import LogicalTests
from helper import bcolors
from people import people

test_mode = False
verbose = False
initial_sword_given_to =1






def unit_test(N):
    '''
    returns False if basic tests failed
    '''
    if N <= 0 :
        print bcolors.FAIL + "Error 1 : Input smaller than or equal to  0 "
        return False
    if str(N).isdigit() == False:
        print bcolors.FAIL+  "Error 2 : Input has to be Numeric"
        return False
    vartype = (type(2) == type(N))
    if not  vartype :
        print bcolors.FAIL + "Error 3 : Expected <int> not " + str(type(N))
        return False

def create_circle(N):
    """
    CLL Creation
    """

    response = unit_test(N)
    if response == False:
        print bcolors.FAIL + "Exiting"
        return False
    current = 2
    first_person = people()
    first_person.location =1
    first_person.next_person=None

    latest_added = first_person
    while current <=N :
        new_person = people()
        new_person.location = latest_added.location+1
        new_person.next_person=None

        latest_added.next_person=new_person

        latest_added=new_person

        current=current+1

    latest_added.next_person=first_person
    give_sword_to(initial_sword_given_to,first_person,N)



def give_sword_to(init_sword,first_person,N):
    """
    Picking starting CLL Node
    """

    response = unit_test(init_sword)
    if response == False:
        print bcolors.FAIL + "Exiting"
        return False

    if init_sword not in range(1,N+1,1):
        print bcolors.WARNING+ "Warning : Sword can't be given to a person not in the circle"
        print bcolors.FAIL+"Exiting"
        return None

    current_person = first_person

    while True :

        if current_person.location == init_sword :
            break
        else:
            current_person=current_person.next_person

    first_person=current_person

    start_game(first_person,N)


def start_game(first_person,N):
    """
    ****************************************
    CORE LOGIC , ALL THE MAGIC HAPPENS HERE
    ****************************************
    """
    global test_mode
    global verbose
    if test_mode:
        LogicalTests.init_tests(N)
        if verbose:
            LogicalTests.verbose = True

    current_person=first_person

    while True :
        if current_person.next_person== current_person:
            print bcolors.OKGREEN+str(current_person.location) + " is left "
            """
            FOR VERIFICATION OF WIN CONDITION IN TEST MODE
            """
            if test_mode:
                LogicalTests.is_everyone_dead(current_person.location)
                LogicalTests.winner_is_not_dead(current_person.location)
            break
        else:
            person_killed=current_person.next_person
            if verbose:
                print bcolors.OKBLUE + str(person_killed.location) + " killed"
            new_person_with_sword= person_killed.next_person
            current_person.next_person=new_person_with_sword
            if test_mode:
                killer = current_person.location
                killed= person_killed.location
            current_person=new_person_with_sword

            """
            LOGICAL TESTING SECTION
            this section is only executed when -t flag is provided in argument.
            This section can be omitted , without any side effects

            Following tests are performed at each kill :

            1.Dead men don't kill
            2.Men can't be both  alive and dead
            3.Men who are not in circle are not killed or can't kill .
            4.A dead  man can't be killed twice
            5.A dead can't become alive .
            6.A person can only kill the person next to him (Left Kill Rule).
            7.New person with sword can't be dead
            8.A sane person won't kill himself .
            9.The Winner must be alive
            10.The Winner must be the only person alive
            (9,10 done above , see line 97)


            Data structures used :
            1.people_alive
            2.people_dead
            (List_Type)

            """
            if test_mode:


                LogicalTests.kill_only_to_left(killer, killed)
                LogicalTests.dead_men_dont_kill(killer)

                LogicalTests.men_cant_be_alive_dead(killer)
                LogicalTests.men_cant_be_alive_dead(killed)

                LogicalTests.men_outside_circle(killer)
                LogicalTests.men_outside_circle(killer)

                result=LogicalTests.is_he_already_dead(killed)
                if result==True:
                    LogicalTests.update_dead(killed)

                LogicalTests.new_person_dead(new_person_with_sword)
                LogicalTests.suicide_is_illegal(killer,killed)

    """
    Clean up tests and verify is all tests passed
    """
    if test_mode:
        if LogicalTests.test_pass == True:
            print "\nAll logical tests passed in " + str(LogicalTests.rounds) + " rounds"
            test_mode = False
        LogicalTests.reset_data()

    return None




