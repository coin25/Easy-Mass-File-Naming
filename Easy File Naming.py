
'''
    File name: Easy File Naming.py
    Author: Austin Young
    Date created: 2016/07/11
    Date last modified: 2016/07/12
    Python Version: 3.43
'''

#NOTE THIS WILL IRREVERSIBLY CHANGE FILENAMES IN A GIVEN LOCATION. BE VERY CAREFUL NOT TO RUIN A FOLDER.

import os
# Feel free to make this any number
number = 1
# Warning
print("THIS WILL RENAME ALL FILES IN THE WALLPAPERS DIRECTORY! THIS CANNOT BE UNDONE!")
# Verifies that the user wants to continue, can really destroy a folder if used accidentally.
if input("Are you SURE you want to continue? y/n").lower() == "yes" or "y":
    # Takes a list of all files and folders inside of a given location, then takes each item in the list as a filename.
    # Change "FOLDER/" to whatever your folder name is
    for filename in os.listdir("FOLDER/"):
        # Renames the file from its original name to the number with a .jpg extension, feel free to change this.
        os.rename("FOLDER/{}".format(filename), "FOLDER/{}.jpg".format(number))
        # Increments the number by 1
        number += 1
        # I had rename thousands of files so I printed out a sort of loading bar using percentages.
        if number % 10 == 0:
            print("We are {}% done".format((number / len(os.listdir("Wallpapers/"))) * 100))


print("Done")