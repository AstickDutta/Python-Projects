Explanation:
# Importing time module:

# The time.sleep() function is used to pause the execution of the code for a specified number of seconds, creating the effect of a real-time countdown.
# Input:

# The user is prompted to enter a countdown time in seconds.
# For loop:

# The loop runs from the entered time down to 1, decrementing by 1 on each iteration (reverse countdown).
# Time conversion:

# Inside the loop, the total time in seconds (i) is converted into hours, minutes, and seconds:
# seceond = i % 60: Extracts the seconds by taking the remainder when dividing by 60.
# minutes = int(i / 60) % 60: Converts the remaining time into minutes by dividing by 60 and taking the remainder.
# hours = int(i / 3600): Converts the remaining time into hours by dividing by 3600 (seconds in an hour).
# Formatted output:

# The time is printed in the HH:MM:SS format with leading zeros if the values are less than 10 (e.g., 02:04:05).
# Sleep function:

# time.sleep(1) pauses the execution of the loop for 1 second, ensuring that the countdown occurs in real time.
# Final message:

# After the countdown completes, the program prints "Time's up!!"