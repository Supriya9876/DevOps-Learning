#!/bin/bash

# Check if a file name is provided as an argument
if [ $# -eq 0 ]; then
    echo "Usage: $0 <log_file>"
    exit 1
fi

LOG_FILE=$1

# Check if the file exists
if [ ! -f "$LOG_FILE" ]; then
    echo "Error: File '$LOG_FILE' does not exist."
    exit 1
fi

# Extract and print unique IP addresses
echo "Unique IP addresses found in the log file:"
grep -oE '\b([0-9]{1,3}\.){3}[0-9]{1,3}\b' "$LOG_FILE" | sort -u