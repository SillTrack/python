import itertools
import time



class TrafficLight:
    def __init__(self):
        print('Traffic light is on')
    __color = ['Red', 'Yellow', 'Green']
    def running(self):
        cycler = itertools.cycle(TrafficLight.__color)
        for el in cycler:
            if el == 'Red':
                print(el)
                time.sleep(7)

            elif el == 'Yellow':
                print(el)
                time.sleep(2)

            else:
                print(el)
                time.sleep(5)




light = TrafficLight()
print(light.running())