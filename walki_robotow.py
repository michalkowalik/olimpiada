#!/usr/bin/env python3
import sys

# prosty stos:
class Stack:
    stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        raise Exception("Empty stack") 

    def peep(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        raise Exception("Empty stack")

    def is_empty(self):
        return len(self.stack) == 0
            

# remove the pairs. an expensive approach
def eliminate_pairs(robots):

    # jeśli mamy tylko jednego robota, nie ma czego dalej sprawdzać:
    if len(robots) < 2:
        return False

    # znajdź robota z największą zwinnością
    robots.sort(key = lambda x : x[1])
    max_z_robot = robots[-1]

    # posortuj po sile
    robots.sort(key = lambda x : (x[0], -x[1]))

    # jeśli najsilniejszy robot jest równiez najzwinniejszy, nie ma czego dalej sprawdzać
    if max_z_robot[0] >= robots[-1][0]:
        return False

    # jeśli najsilniejszy nie jest najzwinniejszy, to kazdy da się usunąć.
    # problem mamy jedynie, jeśli 
    # a) kazdy moze usunąć kazdego
    # b) mamy niaparzystą ilość robotów na wejściu

    if len(robots) % 2 == 0:
        # kaźdy robot moźe być usunięty, parzysta liczba robotów
        return True
    
    # zaczynamy sprawdzać czy aktualny robot moze usunąć wszystkie pozostałe roboty.
    # jeśli tak - kontynuujemy sprawdzanie
    # jeśli nie - wszystkie roboty mogą być usunięte
    for (s, z) in robots:
        eliminated = [x for x in robots if x[0] <= s or x[1] <= z]
        # eliminated będzie miało długość conajemniej 1 ((s,z)), maksymalnie będzie to
        # dlugość wejścia. 
        
        if len(eliminated) < len(robots):
            return True


    # mamy przypadek nieparzystej liczby robotów, gdzie kazdy usuwa kazdego
    return False

def main():
    robots = []
    line_index = 0
    robot_count = 0

    for line in sys.stdin:
        if line_index == 0:
            robot_count = int(line)
            line_index += 1
            continue
        if line_index <= robot_count:
            robots.append([int(x) for x in line.split()])
            line_index += 1

    if robot_count < 1 or robot_count > 200000:
        print("TAK")
        return

    if eliminate_pairs(robots):
        print("TAK")
    else:
        print("NIE")


if __name__=="__main__":
    main()