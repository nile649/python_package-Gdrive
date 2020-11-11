#!/bin/bash


# while getopts f:o: flag
# do
#     case "${flag}" in
#         f) FileId=${OPTARG};;
#         o) OutFile=${OPTARG};;
#     esac
# done

# echo "FileId: $FileId";
# echo "OutFile: $OutFile";
echo "FileId: $1";

# wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=$FileId' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=$FileId" -O $OutFile && rm -rf /tmp/cookies.txt


wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate "https://docs.google.com/uc?export=download&id=$1" -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=$1" -O $2 && rm -rf /tmp/cookies.txt

