#!/bin/bash
# runjs.sh - Run any JS script locally with arguments

# Check if at least one argument (the JS file) is given
if [ $# -lt 1 ]; then
  echo "Usage: $0 <script.js> [arguments...]"
  exit 1
fi

SCRIPT="$1"        # First argument = JS file
shift              # Shift arguments so $@ contains the script arguments

# Check if the file exists
if [ ! -f "$SCRIPT" ]; then
  echo "Error: $SCRIPT not found"
  exit 1
fi

# Run the script using Node
node "$SCRIPT" "$@"
