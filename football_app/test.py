from datetime import datetime, timedelta

# The desired date format
date_format = "%Y-%m-%d %H:%M:%S"

# Get the current datetime
today = datetime.now()

# Convert the datetime object to a string using the specified format
today_str = today.strftime(date_format)

# Read the last update datetime string from the file
with open("update_check", "r") as file:
    last_update_str = file.read().strip()  # Use .strip() to remove leading/trailing whitespace and newlines

# Convert the string back to a datetime object
last_update = datetime.strptime(last_update_str, date_format)

# Now you can compare `last_update` with `today` or perform other operations
difference = today - last_update

# Check if three days have passed
if difference >= timedelta(days=3):
    print("Three days have passed since the last update.")
    with open("update_check","w") as file:
        file.write(today_str)
else:
    print("It has not been three days yet.")