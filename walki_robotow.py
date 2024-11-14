#!/usr/bin/env python3
import sys

        
def eliminate(robots):
    robots.sort(key = lambda x: x[1])
    max_z_robot = robots[-1]

    robots.sort(key = lambda x: x[0])
    max_s_robot = robots[-1]

    return max_s_robot[1] < max_z_robot[1]



# remove the pairs. an expensive approach
def eliminate_pairs(robots):
    robots.sort(key = lambda x : x[0])
    # print(robots)

    index = 0

    while index < len(robots) - 1:
        s1, z1 = robots[index]
        s2, z2 = robots[index + 1]

        if z1 < z2:
            robots.pop(index)
        elif z1 > z2:
            robots.pop(index + 1)
            robots.pop(index)     # because s1 < s2
        else:
            index += 1

    # print(robots)
    return len(robots) == 0

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