from people import people
from helper import bcolors
import LogicalTests

test_mode = 0
verbose = 0
initial_sword_given_to =1





'''
returns False if basic tests failed
'''
def unit_test(N):
    if N <= 0 :
        print bcolors.FAIL+  "Error 1 : Input smaller than 0 "
        return False
    if str(N).isdigit() == False:
        print bcolors.FAIL+  "Error 2 : Input has to be Numeric"
        return False
    vartype = type(2)==type(N)
    if not  vartype :
        print bcolors.FAIL + "Error 3 : Expected <int> not " + str(type(N))
        return False

def create_circle(N):
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
    global test_mode
    global verbose
    if test_mode == 1:
        LogicalTests.init_tests(N)
        if verbose == 1 :
            LogicalTests.verbose=1

    current_person=first_person

    while True :
        if current_person.next_person== current_person:
            print bcolors.OKGREEN+str(current_person.location) + " is left "
            break
        else:
            person_killed=current_person.next_person
            if verbose ==1 :
                print bcolors.OKBLUE + str(person_killed.location) + " killed"
            new_person_with_sword= person_killed.next_person
            current_person.next_person=new_person_with_sword
            if test_mode == 1 :
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
            4.A dead man can't be killed twice
            5.A dead can't become alive .
            6.A person can only kill the person next to him (Left Kill Rule).
            7.New person with sword can't be dead


            Data structures used :
            1.people_alive
            2.people_dead
            (List_Type)

            """
            if test_mode == 1 :


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


    if test_mode == 1:
        if LogicalTests.test == True :
            print "\nAll logical tests passed"
        LogicalTests.reset_data()

    return None




