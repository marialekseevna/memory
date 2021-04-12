from main import *
import time

class CPU:
    def __init__(self):
        pass

    def start(self):
        while True:
            if Input1.ready() == 1:
                m.save(Input1.task(), 0)
            else:
                print("ПУ1 не готово к работе")
            time.sleep(1)
            if Input2.ready() == 1:
                m.save(Input2.task(), 1)
            else:
                print("ПУ2 не готово к работе")
            time.sleep(1)
            if Input3.ready() == 1:
                m.save(Input3.task(), 2)
            else:
                print("ПУ3 не готово к работе")
            time.sleep(1)
            m.load_all()
            print("---------------------------")
