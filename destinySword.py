import sword
import sys
from helper import bcolors , run_unit_test

arglist=sys.argv
arglist.pop(0)

if "-ut"  in arglist:
    arglist.remove("-ut")
    if len(arglist)>0:
        print "-ut is a standalone command"
        print str(arglist) + " commands have been ignored "
    run_unit_test()


if "-t" in arglist:
    sword.test_mode=1
    arglist.remove("-t")

if "-v" in arglist:
    sword.verbose=1
    arglist.remove("-v")

if len(arglist) > 1 :
    print bcolors.FAIL + "\n Too many arguments : "
    for argument in arglist:
        print bcolors.WARNING+argument
    exit()


for argument in arglist :

    if argument.isdigit() == False :
        print bcolors.FAIL + "Number Expected "
        print "Instead got " + argument
        exit()

if len(arglist) ==1 :
    sword.create_circle(int(arglist[0]))
else:
    print bcolors.FAIL + "One Number Expected "
    exit()

