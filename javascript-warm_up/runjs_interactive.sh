#!/bin/bash
# runjs_interactive.sh - Interactive runner for JS scripts

# Find all .js files in current directory
scripts=(*.js)

# Check if any .js scripts exist
if [ ${#scripts[@]} -eq 0 ]; then
  echo "No JavaScript files found in the current directory."
  exit 1
fi

echo "Available JavaScript scripts:"
# List scripts with numbers
for i in "${!scripts[@]}"; do
  echo "$((i+1))) ${scripts[$i]}"
done

# Ask user to select a script
read -p "Enter the number of the script to run: " choice

# Validate input
if ! [[ "$choice" =~ ^[0-9]+$ ]] || [ "$choice" -lt 1 ] || [ "$choice" -gt "${#scripts[@]}" ]; then
  echo "Invalid choice."
  exit 1
fi

selected_script="${scripts[$((choice-1))]}"

# Ask for arguments
read -p "Enter arguments for $selected_script (leave empty if none): " user_args

echo "Running: node $selected_script $user_args"
echo "------------------------"
# Run the selected script with Node
node "$selected_script" $user_args
echo "------------------------"
echo "Done."
