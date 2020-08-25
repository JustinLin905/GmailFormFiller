######################################################################

# GmailFormFiller.py  :  a script which automates certain parts of
# Google account creation, making it less tedious for users to make
# a new email.

# Dependencies: pyautogui

# This program automatically fills in the forms necessary to make
# a Google account. All the user needs to do is choose either random or 
# custom credentials, open a New Tab page in Chrome, and let the program 
# handle the rest.

# This script cannot automate phone number verification if Google requests
# it. The user will have to finish this part themselves, then the program 
# will continue automating. The script will also remove the phone number
# used for verification from the account automatically.

# malefirstnames.py, femalefirstnames.py, and lastnames.py are used to create
# a random identity if the user doesn't want to use custom credentials.
# These secondary Python files contain lists of common names to randomly
# select from.
 
# Feel free to reuse, edit, or transform this script into
# anything you like!

# Written by Justin Lin in July 2020

######################################################################




import pyautogui
from time import sleep
import string
import random
from malefirstnames import maleList
from femalefirstnames import femaleList
from lastnames import lastList

# Running variable, controls the main loop of the program
running = True

# Locate image function, locates the center of an image and clicks it
def locateImage (imageName):

    barLocation = pyautogui.locateOnScreen(str(imageName), grayscale = True, confidence = CONFIDENCE_LIMIT)
    barCenter = pyautogui.center(barLocation)
    barX, barY = barCenter

    pyautogui.click(barX, barY)

# Navigate to Google function, handles navigating to the Google Accounts creation page
def navToGoogle():

    pyautogui.typewrite("https://accounts.google.com/signup")

    # Press Space and Backspace to make sure no autocomplete gets in the way
    pyautogui.keyDown("space")
    pyautogui.keyUp("space")

    pyautogui.keyDown("backspace")
    pyautogui.keyUp("backspace")

    pyautogui.keyDown("enter")
    pyautogui.keyUp("enter")






###### MAIN PROGRAM ######

while running:

    ### Variables: ###

    # Constant confidence limit variable, determines how strictness of image searching
    CONFIDENCE_LIMIT = 0.7

    # Random characters variable, used to generate a random secure password
    randChars = string.digits + string.ascii_letters + "!@#$%^&*+=-_"

    # Loop counter variables, end scanning loops when the desired image is found
    barLocationCounter = True
    firstNameLocationCounter = True
    lastNameLocationCounter = True
    emailLocationCounter = True
    passwordLocationCounter = True
    confirmLocationCounter = True
    nextLocationCounter = True
    phoneLocationCounter = True
    monthLocationCounter = True
    septemberLocationCounter = True
    dayLocationCounter = True
    yearLocationCounter = True
    genderFieldLocationCounter = True
    genderLocationCounter = True
    agreeLocationCounter = True

    # Input loop variables to end those loops when needed
    inputCounter = True
    genderInputCounter = True
    repeatInputCounter = True

    # Gender variable, determines what gender the script will select. Either male or female will be chosen if user wants random details, but "Other" can be chosen manually
    maleOrFemale = [0, 1]
    gender = random.choice(maleOrFemale)


    ##################


    ### INTRO BLOCK ###

    # First, we must introduce the user.
    print ("\nWelcome to Gmail Form Filler!")
    print ("\nThis script will quickly create a Google account for you to use, automatically.")
    print ("Make sure to have Chrome installed and ready to use in order for this program to work.")
    print ("Note that if you run into mandatory phone number verification, you will have to \nmanually complete this before the program can automate the rest.")

    # Ask the user if they would like to choose their own details or let the program handle it
    print ("\nFirst, would you like the program to automatically generate an identity, \nemail address, and password, or would you like to choose your own?")

    while inputCounter == True:

        # Take the input
        userChoice = str(input("\nWhat would you like? (random/my choice): "))

        # If the user enters a valid input
        if userChoice == "random" or userChoice == "Random" or userChoice == "my choice" or userChoice == "My choice":

            # If the user chooses random
            if userChoice == "random" or userChoice == "Random":

                # Set this bool to True for random email
                randomEmail = True

                # Assign these name variables with random names from lists based on gender
                if gender == 0:

                    firstName = random.choice(maleList)

                else:

                    firstName = random.choice(femaleList)

                lastName = random.choice(lastList)

                # Create a random password
                password = "".join(random.choice(randChars) for i in range (10))
                

                # End this input loop
                inputCounter = False

            # If the user wants to choose their details
            else:

                # Set this bool to False for manual email input
                randomEmail = False

                # Ask for the first name
                firstName = str(input("\nPlease enter your desired first name: "))

                # Ask for last name
                lastName = str(input("\nPlease enter your desired last name: "))

                # Ask for gender
                while genderInputCounter == True:

                    enteredGender = str(input("\nPlease choose your gender (male/female/other): "))

                    if enteredGender == "male" or enteredGender == "Male" or enteredGender == "female" or enteredGender == "Female" or enteredGender == "other" or enteredGender == "Other":

                        # End the input loop
                        genderInputCounter = False

                        # If user chooses male
                        if enteredGender == "male" or enteredGender == "Male":

                            gender = 0
                        
                        # If user chooses female
                        elif enteredGender == "female" or enteredGender == "Female":

                            gender = 1

                        # If user chooses other
                        else:

                            gender = 2


                    else:

                        print ("Oops! Please enter either male, female, or other.")
                    


                # Ask for email address
                emailAddress = str(input("\nPlease enter your desired email address (WITHOUT @gmail.com): "))

                # Ask for password
                password = str(input("\nPlease enter your desired password (8+ characters with a mix of letters, numbers and symbols): "))

                # End this input loop
                inputCounter = False

        # If the user's input is invalid
        else:

            print ("\nOops! You entered something invalid. Please enter either 'random' or 'my choice'.")




    # Now, we begin the process of creating the Google account. Prompt the user to open Chrome
    sleep (2)
    print ("\nOk! Now the program will begin creating your account automatically.")
    sleep (2)
    print ("Open Google Chrome in fullscreen now! Make sure that you're on the New Tab page. The program will begin in 10 seconds.")

    sleep (10)
    print ("\n")

    # Next, we repeatedlty scan for the Chrome search bar and navigate to google.com
    while barLocationCounter == True:

        # If a selected searchbar (either light or dark mode) is found on screen (both must be empty)
        if pyautogui.locateOnScreen("images/searchbar.png", grayscale = True, confidence = CONFIDENCE_LIMIT) != None or pyautogui.locateOnScreen("images/searchbardark.png", grayscale = True, confidence = CONFIDENCE_LIMIT) != None:  

            # End this scanning loop
            barLocationCounter = False

            # Tell user that search bar has been found
            print ("\nSearch bar found! Navigating to Google Sign-up page...")

            # If the light selected bar image is found:
            if pyautogui.locateOnScreen("images/searchbar.png", grayscale = True, confidence = CONFIDENCE_LIMIT) != None:

                # Assign bar location to the box coordinates of the detected image. Then find the center coordinates of the box, and use these coordinates to navigate to Google
                locateImage("images/searchbar.png")
                navToGoogle()

            # If the dark selected bar image is found:
            else:

                locateImage("images/searchbardark.png")
                navToGoogle()



        # If no Chrome search bar is found, tell the user it hasn't yet been found
        else:
            print ("No Chrome search bar found on screen.")


    # Next step: enter the credentials into the signup forms
    print ("Done!")

    print ("\nFilling in webpage forms...")

    # Type the first name into the already selected box
    while firstNameLocationCounter == True:

        # Scan for the first name box and type in the first name once it appears
        if pyautogui.locateOnScreen("images/firstnamefield.png", grayscale = True, confidence = CONFIDENCE_LIMIT) != None:

            pyautogui.typewrite(str(firstName))
            firstNameLocationCounter = False

            print ("First name field found and entered first name!")

        # If it's not found yet
        else:

            print ("No first name field found.")



    # Search for last name box, click it, and enter a last name
    print ("\nSearching for last name field...")

    while lastNameLocationCounter == True:

        if pyautogui.locateOnScreen("images/lastnamefield.png", grayscale = True, confidence = CONFIDENCE_LIMIT) != None:

            locateImage("images/lastnamefield.png")
            pyautogui.typewrite(str(lastName))

            lastNameLocationCounter = False

            print ("Last name field found and entered last name!")

        else:

            print ("No last name field found.")


    # Time for entering the email. If the user chose 'random' at the start, the program will sleep 
    # to let Google autofill an available email into the field. If the user chose 'my choice', the 
    # program will find the field and enter the user's email.

    if randomEmail == True:

        print ("Waiting for Google to autocomplete email...")
        sleep (6)
        print ("Done!")


    else:
        print ("\nSearching for email field...")

        while emailLocationCounter == True:

            if pyautogui.locateOnScreen("images/emailaddressfield.png", grayscale = True, confidence = CONFIDENCE_LIMIT) != None:

                locateImage("images/emailaddressfield.png")
                pyautogui.typewrite(str(emailAddress))

                emailLocationCounter = False

                print ("Email field found and entered address!")






    # Search for password box, click it, and enter a password
    print ("\nSearching for password field...")

    while passwordLocationCounter == True:

        if pyautogui.locateOnScreen("images/passwordfield.png", grayscale = True, confidence = CONFIDENCE_LIMIT) != None:

            locateImage("images/passwordfield.png")
            pyautogui.typewrite(str(password))

            passwordLocationCounter = False

            print ("Password field found and entered password!")

        else:

            print ("No password field found.")


    # Search for confirm password box, click it, and enter a password
    print ("\nSearching for confirm password field...")

    while confirmLocationCounter == True:

        if pyautogui.locateOnScreen("images/confirmfield.png", grayscale = True, confidence = CONFIDENCE_LIMIT) != None:

            locateImage("images/confirmfield.png")
            pyautogui.typewrite(str(password))

            confirmLocationCounter = False

            print ("Confirm password field found and entered password!")

        else:

            print ("No confirm password field found.")


    # Search for 'Next' button and click it
    print ("\nSearching for Next button...")

    while nextLocationCounter == True:

        if pyautogui.locateOnScreen("images/nextbutton.png", grayscale = True, confidence = CONFIDENCE_LIMIT) != None:

            locateImage("images/nextbutton.png")

            nextLocationCounter = False

            print ("Next button found and clicked!")

        else:

            print ("No Next button found.")


    # At this point the user may encounter phone number verification. The user will have to pass this themselves before the automation continues

    # Now, we clear the phone number field in case the user had to do two-step verification.
    print ("\nClearing phone number field...")

    while phoneLocationCounter == True:

        if pyautogui.locateOnScreen("images/phonenumberfield.png", grayscale = True, confidence = 0.9) != None:

            barLocation = pyautogui.locateOnScreen("images/phonenumberfield.png", grayscale = True, confidence = 0.9)
            barCenter = pyautogui.center(barLocation)
            barX, barY = barCenter

            pyautogui.click(barX, barY + 12)        # Plus 12 since the program scans for the text above the box

            pyautogui.hotkey("ctrl", "a")           # Select all text in the field
            pyautogui.keyDown("backspace")          # Press and release backspace
            pyautogui.keyUp("backspace")

            phoneLocationCounter = False

            print ("Phone number field cleared!")

        else:

            print ("No phone number field found.")

    # Next, look for the month, day, and year fields and fill them in wiht Sept. 4, 1998 (day Google was founded)
    print ("\nSearching for month field...")

    while monthLocationCounter == True:

        if pyautogui.locateOnScreen("images/monthfield.png", grayscale = True, confidence = CONFIDENCE_LIMIT) != None:

            locateImage("images/monthfield.png")

            monthLocationCounter = False

            print ("Month field found and clicked!")

        else:

            print ("No month field found.")



    print ("\nSearching for 'September'...")

    while septemberLocationCounter == True:

        if pyautogui.locateOnScreen("images/septemberfield.png", grayscale = True, confidence = CONFIDENCE_LIMIT) != None:

            locateImage("images/septemberfield.png")

            septemberLocationCounter = False

            print ("September found and clicked!")

        else:

            print ("No September found.")



    print ("\nSearching for day field...")

    while dayLocationCounter == True:

        if pyautogui.locateOnScreen("images/dayfield.png", grayscale = True, confidence = CONFIDENCE_LIMIT) != None:

            locateImage("images/dayfield.png")
            pyautogui.typewrite("4")

            dayLocationCounter = False

            print ("Day field found and entered '4'!")

        else:

            print ("No day field found.")



    print ("\nSearching for year field...")

    while yearLocationCounter == True:

        if pyautogui.locateOnScreen("images/yearfield.png", grayscale = True, confidence = CONFIDENCE_LIMIT) != None:

            locateImage("images/yearfield.png")
            pyautogui.typewrite("1998")

            yearLocationCounter = False

            print ("Year field found and entered '1998'!")

        else:

            print ("No year field found.")


    # Now, click on the gender dropdown and select either male, female, or other based on gender variable
    print ("\nSearching for gender dropdown menu...")

    while genderFieldLocationCounter == True:

        if pyautogui.locateOnScreen("images/genderfield.png", grayscale = True, confidence = CONFIDENCE_LIMIT) != None:

            locateImage("images/genderfield.png")

            genderFieldLocationCounter = False

            print ("Gender field found and clicked!")

        else:

            print ("No gender field found.")

    print ("\nSearching for selected gender...")

    while genderLocationCounter == True:

        # If gender is male
        if gender == 0:

            if pyautogui.locateOnScreen("images/malefield.png", grayscale = True) != None:

                locateImage("images/malefield.png")

                genderLocationCounter = False

                print ("'Male' found and clicked!")

            else:

                print ("No 'Male' found.")

        # If gender is female
        elif gender == 1:

            if pyautogui.locateOnScreen("images/femalefield.png", grayscale = True, confidence = CONFIDENCE_LIMIT) != None:

                locateImage("images/femalefield.png")

                genderLocationCounter = False

                print ("'Female' found and clicked!")

            else:

                print ("No 'Female' found.")


        # If gender is other:
        else:

            if pyautogui.locateOnScreen("images/otherfield.png", grayscale = True, confidence = CONFIDENCE_LIMIT) != None:

                locateImage("images/otherfield.png")

                genderLocationCounter = False

                print ("'Other' gender found and clicked!")

            else:

                print ("No 'Other' found.")


    # Look for the next button again and click it
    nextLocationCounter = True

    print ("\nSearching for Next button...")

    while nextLocationCounter == True:

        if pyautogui.locateOnScreen("images/nextbutton.png", grayscale = True, confidence = CONFIDENCE_LIMIT) != None:

            locateImage("images/nextbutton.png")

            nextLocationCounter = False

            print ("Next button found and clicked!")

        else:

            print ("No Next button found.")



    # Finally, search for the "I agree" button and click it to finsih account creation
    print ("\nSearching for 'I agree' button...")

    while agreeLocationCounter == True:

        # Scroll past the Privacy and Terms
        pyautogui.scroll(-1000)

        if pyautogui.locateOnScreen("images/agreebutton.png", grayscale = True) != None:

            locateImage("images/agreebutton.png")
            pyautogui.click(barX, barY)

            agreeLocationCounter = False

            print ("'I agree' button found and clicked!")

        else:

            print ("No 'I agree' button found.")







    ### Once the program has finished, return the credentials used to make the account ###
    print ("\n\n#####################################################")

    print ("\nThe program has finished creating your Google account!")

    print ("\nYour details are below:")

    # Print name
    print ("\nName: {0} {1}".format(str(firstName), str(lastName)))

    # Print the selected gender
    if gender == 0:

        print ("Gender: Male")

    elif gender == 1:

        print ("Gender: Female")

    else:

        print ("Gender: Other")

    # If the user created their own email, print it. If it was random, print appropriate message
    if randomEmail == True:

        print ("Email Address: Random email generated by Google")

    else:

        print ("Email Address: {0}@gmail.com".format(str(emailAddress)))

    # Print the password for the account
    print ("Password: {0}".format(str(password)))

    print ("\nIf your password was randomly generated, make sure to \nnote it down somewhere!")

    print ("\n#####################################################")

    # Ask user if they want to run the program again
    while repeatInputCounter == True:

        repeat = str(input("\nWould you like to run the program again? (yes/no): "))

        if repeat == "yes" or repeat == "Yes" or repeat == "no" or repeat == "No":

            if repeat == "yes" or repeat == "Yes":

                print ("Okay, repeating...")
                print ("\n")

                repeatInputCounter = False

            else:

                # End the program
                repeatInputCounter = False
                running = False
        
        else:

            print ("Please enter either yes or no.")

# Closing message:
print ("\nThank you for using Gmail Form Filler!")
print ("Program will exit in 10 seconds. Make sure to note down your passwords!")
sleep (10)

