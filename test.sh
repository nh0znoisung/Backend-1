#!/bin/bash

# if [ $# -ne 2 ]; then
#         echo "please specify 2 command line arguments"
# 		exit 1
# fi

# Hello world

# touch $1

# echo $2 > $1

filename='company.txt'
n=1
while read line; 
do
# reading each line
echo "Line No. $n : $line"
n=$((n+1))
done < $filename

# while read line;
# do echo $line;
# done < company.txt