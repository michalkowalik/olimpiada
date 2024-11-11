#!/usr/bin/env python3
import sys

i=1
j=1
nie=0
eliminacja=0

robots = []
line_index = 0
robot_count = 0


for line in sys.stdin:
    if line_index == 0:
        robot_count = int(line)
        print(f"will read data for {robot_count} robots")
        line_index += 1
        continue
    if line_index <= robot_count:
        robots.append([int(x) for x in line.split()])
        line_index += 1
        


robots.sort(key = lambda x: x[0])
print(robots)

for i in range(1, robot_count):
    if robots[i][1] < robots[i - 1][1]:
        eliminacja=eliminacja+1
    else:
        nie=nie+1
if nie>eliminacja:
    print("NIE")
else:
    print("TAK")