#!/usr/bin/env python3
import sys

# can r1 eliminate r2?
def can_eliminate(r1, r2):
    return r1[0] > r2[0] or r1[1] > r2[1]

## szukamy robotów lezących na granicy.
## sortujemy listę po s malejąco
## jeśli robot o sile s ma zwinność z mniejszą niz aktualna max_z -> nie lezy na granicy
def find_border(ouback_robots):
    ouback_robots.sort(key = lambda x : -x[0])
    inner_robots = set()
    max_z = 0

    for r in ouback_robots:
        if r[1] < max_z:
            inner_robots.add(r)
        else:
            max_z = r[1]

    return set([x for x in ouback_robots if x not in inner_robots])

def eliminate_pairs(robots):

    # jeśli mamy tylko jednego robota, nie ma czego dalej sprawdzać:
    if len(robots) < 2:
        return False

    # znajdź robota z największą zwinnością
    robots.sort(key = lambda x : (x[1], -x[0]))
    max_z_robot = robots[-1]

    # posortuj po sile
    robots.sort(key = lambda x : (x[0], -x[1]))

    # jeśli najsilniejszy robot jest równiez najzwinniejszy, nie ma czego dalej sprawdzać
    if max_z_robot[0] >= robots[-1][0]:
        return False

    max_s_robot = robots[-1]

    # jeśli najsilniejszy nie jest najzwinniejszy, to kazdy robot moze być usunięty
    # ale musimy sprawdzić, czy na zewnętrznej granicy obszaru wyznaczonego przez max_s i max_z nie mamy nieparzystej liczby robotów.
    # te robotu uswają się wzajemnie - jeśli jest ich nieparzysta liczba, wynik jest negatywny.

    # znajdź roboty o s > max_z[s] i z > max_s[z]
    outback_robots = [(x[0], x[1]) for x in robots if x[0] > max_z_robot[0] and x[1] > max_s_robot[1]]
    border_robots = find_border(outback_robots)

    # max_s i max_z lezą na granicy, musimy dodać
    border_robots.add((max_s_robot[0], max_s_robot[1]))
    border_robots.add((max_z_robot[0], max_z_robot[1]))

    if len(border_robots) % 2 == 0:
        return True

    # dla nieparzystej liczby robotów na granicy:
    # sprawdzamy, czy istnieje robot, który ma s < max_z(s), ale z większe niz nasz robot na granicy.
    # jeśli tak, to znaczy, ze moze być ususnięty, a wtedy mozemy idealnie wszystkie roboty usunac:
    for robot in border_robots:
        if len([r for r in robots if can_eliminate(r, robot) and (r[0], r[1]) not in border_robots]) > 0:
            return True

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