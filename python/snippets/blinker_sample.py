#!/usr/bin/env python
#-*- coding:utf8 -*-

from blinker import signal

class Person(object):
     def __init__(self, name):
         self.name = name
     def __repr__(self):
         return self.name

def say_my_name(lover):
    print "Hello! my name is %s." % lover

def drillbits(lover):
    print "drillbits love %s !!!!" % lover

def oyakata(lover):
    print "oyakata love %s !!!!" % lover

#create person object
podhmo = Person('podhomo')
pasberth = Person('pasberth')
tell_k = Person('tell-k')

#create signal
mysignal = signal('love')

#connect
mysignal.connect(say_my_name)
mysignal.connect(drillbits, sender=pasberth)
mysignal.connect(oyakata, sender=podhmo)

#send signal
mysignal.send(pasberth)
mysignal.send(podhmo)
mysignal.send(tell_k)
