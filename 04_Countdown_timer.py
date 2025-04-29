import time

def countdown_timer(seconds):
    print(f"Countdown starting from {seconds} seconds:")

    while seconds >= 0:
        print(f"{seconds:2}", end="\r")  # Print with 2 spaces to ensure clearing previous digits
        time.sleep(1)
        seconds -= 1

    
    print("Time's up!")  # Print the 'Time's up!' message

# Get user input for the countdown time in seconds
user_seconds = int(input("Enter the number of seconds for the countdown: "))
countdown_timer(user_seconds)
