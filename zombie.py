# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 21:40:28 2020

Amanda Faulconer
Classes and Objects Assignment 
Question #2- Zombies
"""


import sys
import random

class zombie: 
    
    # constructors
    
    def __init__(self, a_name = "", a_gender = "", a_city = "", a_ztype = ""):
        self.a_name = a_name
        self.a_gender = self._assigngender()
        self.a_city = self._assignlocation()
        self.a_ztype = self._assigntype()

    def __str__(self):
        return self.a_name + " " + self.a_gender + " " + self.a_city + " " + self.a_ztype + " "

    #put setters and getters here
    
    @property
    def name(self):
        return self.a_name
    @name.setter
    def name(self,value):
        self.a_name = value
        
    @property
    def gender(self):
        return self.a_gender
    @gender.setter
    def gender(self,value):
        self.a_gender = value
        
    @property
    def city(self):
        return self.a_city
    @city.setter
    def city(self,value):
        self.a_city = value
        
    @property
    def ztype(self):
        return self.a_ztype
    @ztype.setter
    def ztype(self,value):
        self.a_ztype = value
        


    def _assignlocation(self):
        cities = ["Helena", "Butte", "Missoula", "Bozeman"]
        a = random.randint(0,3)
        return cities[a]
    
    def _assigngender(self):
        genders = ["Male", "Female"]
        a = random.randint(0,1)
        return genders[a]
    
    def _assignname(self):
        names = ["Saloman Grundy", "Tarman", "Jason Voorhees", \
                  "Billy Butcherson"]
        a = random.randint(0,3)
        return names[a]
    
    def _assigntype(self):
        types = ["Runner", "Crawler", "Ghoul", "Screamer", "Cannibal Corpses", \
                 "Voodoo","Walker", "Ankle Biters", "Meat Bags"]
        a = random.randint(0,6)
        return types[a]

    def zombieinfo(self):
       print(self.a_name + " " + self.a_gender + " " + self.a_city + " " + self.a_ztype + " ")

#---------- end of class -------------------

zombies = []


def printzombietype():
    # print the zombie type
    cntr = 1
    
    for i in zombies:
        sys.stdout.write(str(cntr) + ". ")
        i.zombieinfo()
        cntr = cntr+1
    

def zombiechoice():
    print("\nAdd or delete a Zombie?     ")
    zombiechoice = input("\nChoose 1 or 2?    ")
    if(zombiechoice == "1"):
        createaZombie()
    elif(zombiechoice == "2"):
        deleteZombie()
    else:
        print("\nThat was a wrong choice dumb dumb")
            

def createaZombie():
    print("\nAdding a new Zombie   ")
    
    quit = "n"
    
    while(quit != "y"): 

        a_zombie = zombie()
        
        a_zombie.name = input("Choose your zombies name   ")
        a_zombie.gender = input("Choose your zombies gender   ")
        zombies.append(a_zombie)
         
        quit = input("Are you done adding zombies to your list y/n? ").lower()         

    printzombietype()
  
    
def deleteZombie():
    print("\nDeleting a Zombie from your list   ")
    printzombietype()
    
    nums = int(input("Which zombie number would you want to delete?  "))
    del zombies[nums-1]
    printzombietype()
    
    
def makeZombies():
    num = int(input("How many zombies do you want to run from? "))
    
    for i in range(num):
        new_zombie = zombie(random.choice)
        
        zombie.append(new_zombie)
    
    printzombietype()      
    

def main():
    
        
    createaZombie()

    
    quit = "n"
    
    while(quit != "y"):
        zombiechoice()

        quit = input("God, are you done yet?  y/n  ").lower()    

    
main()
