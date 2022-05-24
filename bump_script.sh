# !/bin/bash

if [ $# -ne 2 ]; then
        echo "please specify 2 command line arguments"
        exit 1
fi

if [ ! -f $2 ]; then
        echo "$2 does not exist."
        exit 1
fi

FILE_NAME=$2
PART=$1

# Find the pattern
version_number=$(grep -E -o '(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)' $FILE_NAME )

if [ -z "$version_number" ]; then
        echo "No version number found in $FILE_NAME"
        exit 1
fi

# Extract to version_part
IFS='.' read -ra version_part <<< "$version_number"

# Increase phrase
if [ $PART == "patch" ]; then
        version_part[2]=$(( version_part[2] +1 ))
elif [ $PART == "minor" ]; then
        version_part[1]=$(( version_part[1] +1 ))
        version_part[2]=0
elif [ $PART == "major" ]; then
        version_part[0]=$(( version_part[0] +1 ))
        version_part[1]=0
        version_part[2]=0
else
        echo "$PART does not in the command list. "
        echo "<patch>: the program will bump patch version.
<minor>: the program will bump minor version.
<major>: the program will bump major version. "
fi

# Merge it
version_number_new="${version_part[0]}.${version_part[1]}.${version_part[2]}"

# Find again and replace: sed
sed -i "0,/$version_number/s//$version_number_new/" $FILE_NAME