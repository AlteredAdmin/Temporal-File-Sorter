import os
import shutil
from datetime import datetime

# prompt user for directory path
dir_path = input("Enter the directory path to be sorted (e.g., /home/administrator/files/): ")

# prompt user for sort preference
sort_pref = input("Sort by 'created' or 'modified' date? ")

# create a list of files in the directory
files = os.listdir(dir_path)

# loop through the list of files
for file in files:
    # get the path of each file
    file_path = os.path.join(dir_path, file)
    # check if the file is a regular file
    if os.path.isfile(file_path):
        # get the time based on the user's preference
        if sort_pref == "created":
            time = os.path.getctime(file_path)
        else:
            time = os.path.getmtime(file_path)

        # convert the time to a datetime object
        time_obj = datetime.fromtimestamp(time)
        # get the month, day, and year of the time
        month = str(time_obj.month)
        day = str(time_obj.day)
        year = str(time_obj.year)
        # create the folder name using the month, day, and year
        folder_name = month + "-" + day + "-" + year
        # create the folder path
        folder_path = os.path.join(dir_path, folder_name)
        # check if the folder already exists
        if not os.path.exists(folder_path):
            # create the folder if it does not exist
            os.mkdir(folder_path)
        # move the file to the folder
        shutil.move(file_path, folder_path)
