#!/bin/bash

# part 1
TEST_PATH="walrob/input1"
OUT_PATH="walrob/output1"

for i in $(seq 1 999);
do
    program_output=$(python3 walki_robotow.py < $TEST_PATH/test$i.in)
    expected=$(cat $OUT_PATH/test$i.out)

    [ "$program_output" != "$expected" ] && echo "Test $i failed" || echo -n "."
done
echo ""
echo "Part 1 done"

# part 2
TEST_PATH="walrob/input2"
OUT_PATH="walrob/output2"

for i in $(seq 1 999);
do
    program_output=$(python3 walki_robotow.py < $TEST_PATH/test$i.in)
    expected=$(cat $OUT_PATH/test$i.out)

    [ "$program_output" != "$expected" ] && echo "Test $i failed" || echo -n "."
done
echo ""
echo "Part 2 done"
