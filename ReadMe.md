# GmailFormFiller.py

Gmail Form Filler is a Python script which automates certain parts of Google account creation, making it less tedious to make a new email.

For users working with the Python file, the only dependency is `pyautogui`.

**Note that this program is not a bot that can make thousands of Google accounts in seconds.** It is simply a script which fills in the Google account creation webpage automatically, and has added features such as random identity generation. It cannot automate or bypass steps such as phone number verification.

# Usage

To use this program, click on the Code button and choose Download Zip. Then, extract the zip folder.

From there, you can run either `GmailFormFiller.py` or `GmailFormFiller.exe`. If you don't have a Python installation and just want to use the program out-of-the-box, use the `.exe` file. 

Upon launching the program, a prompt will ask the user if they want to enter their own credentials to create the new account (name, email address, password, etc.) or if they want the program to generate everything randomly.

```
Welcome to Gmail Form Filler!

This script will quickly create a Google account for you to use, automatically.
Make sure to have Chrome installed and ready to use in order for this program to work.
Note that if you run into mandatory phone number verification, you will have to
manually complete this before the program can automate the rest.

First, would you like the program to automatically generate an identity,
email address, and password, or would you like to choose your own?

What would you like? (random/my choice):
```

Once the user makes their selection and fills in any information necessary, the automation will begin. Now, simply open a New Tab in Chrome and let the program fill in all of the forms. The program should work even if you have a Chrome theme applied.



Sometimes, the program may be interrupted when Google requests a phone number for verification. The user will have to finish this step themselves, then the program will continue the account creation process.

Once the program has finished creating the new account, it will return the credentials associated with it.


```
#####################################################

The program has finished creating your Google account!

Your details are below:

Name: Roland Kingsley
Gender: Male
Email Address: example123@gmail.com
Password: Ijrgjrom@$#)ng

If your password was randomly generated, make sure to
note it down somewhere!

#####################################################
```

## Notes

`malefirstnames.py`, `femalefirstnames.py`, and `lastnames.py` are used to create a random identity if the user doesn't want to use custom credentials. These secondary Python files contain lists of common names to randomly select from. 

When a user chooses to have a random identity generated, the gender is randomly chosen between Male and Female. The user can choose the "Other" gender option when entering their own custom credentials. 

The `images` folder included with this program contains `.png` files of text fields and buttons that are used on the Google Account Creation webpages. The script scans the screen for these images during the automation process.

Once the script has finished creating an account, it will ask the user if they want to make another one. If they choose yes, the program will loop. If they choose no, the program will end after a short time.
