# Automated Gmail Cleaner

This is a Python-based program that iterates through a specific number of recent emails, identifies the irrelevant ones, marks them and deletes them after the iteration is complete.

## Technologies and Functionalities

The coding language used for `read_email.py` is Python 3.
Make sure that you have the required packages installed:
    ```pip install imap-tools pyyaml```
- The environment used for testing and optimizing the script is WSL. A remote connection has been established in order to run the script.
- The program reads login credentials from `creds.yml` file. PyYAML is used to securely store credentials in the YAML file.
- The login password was obtained using Google's App Passwords section. From security reasons, the YAML file is excluded with .gitignore
- The library used for connecting to the Gmail inbox and handling the emails is **imap-tools**. The program fetches the most recent n = limit emails (n is manually configured to 3000).
- Then, it iterates through these emails, filtering them based on the sender's address, subject, or body (based on keywords such as "linkedin", "aliexpress", "application was viewed", etc.)
- These filtered emails are marked for deletion and, after all n emails have been verified, all the marked emails are moved to Gmail's bin. 
- The program also displays the total number of deleted emails.

## Automating the script

- The program is set to run daily at 12 PM, in an automated way, using Windows Task Scheduler (which runs the .bat file on the specific schedule).
- The `run_email_script.bat` file calls the script using the Python interpreter:
    ```@echo off
      "C:\Users\PC\miniconda3\envs\rapids-23.12\python.exe" "D:\gmail_reader\read_email.py" >> "D:\gmail_reader\script_log.txt" 2>&1
- The script also logs the results in the `script_log.txt` file.
- Make sure you specify the correct path to the Python interpreter on your local machine.

## Use cases

- This project can be used to automatically clean your inbox.
- It removes job application rejection emails, promotional emails and avoids spam.
- The keywords can be modified in order to create other use cases for the program.
