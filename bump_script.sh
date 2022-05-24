#!/bin/bash

if [ $# -ne 2 ]; then
        echo "please specify 2 command line arguments"
        exit 1
fi

patch_command = ('patch', '-p', 'Patch')

# if [ $1 in patch_command] then
#         echo "asdfasdf"

# if [ $1 == 'patch'] || [ $1 == 'minor' ] || [ $1 == 'major' ]; then
#     echo "Bumping version to $1"
# else
#     echo "Please specify a valid version bump type"
#     exit 1
# fi

echo $1
echo $2