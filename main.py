from memory import Memory
import random

m = Memory()

class Input1():
    def __init__(self):
        pass

    def ready():
        return (random.randint(0,1))

    def task():
        a = input()
        return a

class Input2():
    def __init__(self):
        pass

    def ready():
        return (random.randint(0,1))

    def task():
        a = input()
        return a

class Input3():
    def __init__(self):
        pass

    def ready():
        return (random.randint(0,1))

    def task():
        a = input()
        return a

class Output1():
    def __init__(self):
        pass

    def printf(self):
        m.load(0)

class Output2():
    def __init__(self):
        pass

    def printf(self):
        m.load(1)

class Output3():
    def __init__(self):
        pass

    def printf(self):
        m.load(2)

o1 = Output1
o2 = Output2
o3 = Output3
