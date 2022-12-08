#!/bin/bash

# Get the current date
today=$(date +%Y-%m-%d)

# Extract the day of the month from the date
day=${today:8:2}

# Remove the leading zero from the day of the month if it's a single-digit number
if [ $day -lt 10 ]; then
    day=${day:1:1}
fi

# Create the folder name
folder_name="day${day}"

# Create the new folder
mkdir "$folder_name"

# Create solution.py
touch "$folder_name/solution.py"
