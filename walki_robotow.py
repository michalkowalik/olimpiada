#!/usr/bin/env python3
import sys

        
def eliminate(robots):
    robots.sort(key = lambda x: x[1])
    max_z_robot = robots[-1]

    robots.sort(key = lambda x: x[0])
    max_s_robot = robots[-1]

    return max_s_robot[1] < max_z_robot[1]


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

    if eliminate(robots):
        print("TAK")
    else:
        print("NIE")


if __name__=="__main__":
    main()