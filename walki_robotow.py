#!/usr/bin/env python3
import sys

        
def eliminate(robots):
    i=1
    j=1
    nie=0
    eliminacja=0


    robots.sort(key = lambda x: x[0])

    for i in range(1, len(robots)):
        if robots[i][1] < robots[i - 1][1]:
            eliminacja=eliminacja+1
        else:
            nie=nie+1
    if nie>eliminacja:
        return False
    return True


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