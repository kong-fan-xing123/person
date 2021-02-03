#!/usr/bin/env python3

from classtools import AttrDisplay
class Person(AttrDisplay):
 """
 Create and process person records
 """
 def __init__(self,name,job=None,pay=0):
  self.name = name
  self.job = job
  self.pay = pay
 def lastName(self):
  return self.name.split()[-1]
 def giveRaise(self,percent):
  self.pay = int(self.pay * (1 + percent))



class Manager(Person):
 def __init__(self,name,pay):
  Person.__init__(self,name,'mgr',pay)
 def giveRaise(self,percent,bonus=.10):
  Person.giveRaise(self,percent+bonus)
 

class Department:
 """
 a Group
 """
 def __init__(self,*args):
  self.members = list(args)
 def addMember(self,person):
  self.members.append(person)
 def giveRaises(self,percent):
  for person in self.members:
   person.giveRaise(percent)
 def showAll(self):
  for person in self.members:
   print(person)
 def a(self,a):
  return self,a
def createGroup(listOfPerson):
 """
 listOfPerson is a list

example:
dev=createGroup([foo,bob])
dev.giveRaises(0.9)
 """
 atk=Department()
 atk.members=listOfPerson
 return atk


 
