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
    stack = Stack()
    
    # jeśli najsilniejszy robot jest równiez najzwinniejszy, nie ma czego dalej sprawdzać
    if robots[-1][1] == max_z_robot[1]:
        return False


    for s, z in robots:
        is_current_eliminated = False
        while not stack.is_empty():
            top_s, top_z = stack.peep()
            
            if (s > top_s) and (z > top_z):
                # (s, z) jest silniejszy i zwinniejszy niz roboty na stosie
                stack.pop()
            elif (s < top_s) and (z < top_z):
                # (s, z) przegra z kazdym robotem ze stosu
                is_current_eliminated = True
                break
            else:
                # (s, z) i robot z początku stosu usuwają się wzajemnie
                stack.pop()
                is_current_eliminated = True
                break

        # umieść robota na stosie, jeśli nie został wyeliminowany
        if not is_current_eliminated:
            stack.push((s, z))

    return stack.is_empty()

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