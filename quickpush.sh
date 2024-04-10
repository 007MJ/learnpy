#!/bin/bash


# ======================== #
#     get user input 🔥    #
#========================= #

echo "What is the message of commit:"
read message
datep=$(date)

# ======================== #
#     command git          #
#========================= #


git add .
git commit -m "$message + $datep"
git push
