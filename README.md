# swordOfDestiny
The Sword of destiny decides who lives ! 

### 1. How the game works :
A group of N people are standing in a circle . Being bored they decide to make the best of their time by playing a game . A random person is given a sword and he / she kills the person next to him / her (to the left ) and passes the sword in the same direction . ( the default implementation gives the sword to the first person , but the code is tested for any of the N people to recieve the sword at initial time .) 

The last person alive wins ! 

This implementation has a unit testing mode , verbose mode , and a test mode which checks for logical accuracy and acts like the umpire . 
The logical test mode has a set of 8 rules which form the game . 
Following tests are performed at each kill :

            1.Dead men don't kill
            2.Men can't be both  alive and dead
            3.Men who are not in circle are not killed or can't kill .
            4.A dead man can't be killed twice
            5.A dead can't become alive .
            6.A person can only kill the person next to him (Left Kill Rule).
            7.New person with sword can't be dead
            8.A sane person won't kill himself .



## 2 .Usage : 
### Case 1 : 
* $python destinySword -t -v 23 
* $python destinySword -v 23 
* $python destinySword -t  23 
* $python destinySword  23 

 Legend :
* -t : test mode, tests program  logic
* -v : verbose mode 
* 23 : number of people in the circle 

### Case 2: 
$python destinySword -ut 

* -ut : Unit test mode ,self tests input 

## 3. How to get the bits in your system : 
* https://github.com/jaideepkekre/swordOfDestiny/archive/master.zip

## 4. System Requirements 
* python 2.7 
* Tested on Ubuntu 16.04 LTS 


