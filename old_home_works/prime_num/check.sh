#!/bin/bash

str1="OK"

if [ `cat b.txt` == "$str1" ]; then
    python3 check_prime_num.py
else
    echo "unit test pass wrong"
fi
