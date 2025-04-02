# Auto-Torrent-Search-Template
 Automate your torrent searches in a few steps!

Update your email, password/App password, and torrent search inquiry in the .py file

Some email clients allow for App passwords, like Gmail
 You can generate an App password here: https://myaccount.google.com/apppasswords. You would use this App password instead of your regular Gmail password in the script. 

If you're using an App password and it's not being accepted, here are the most common reasons and how to troubleshoot them:

    Double-check the App Password: Ensure you've copied the App password correctly. App passwords are usually 16 characters long and consist of lowercase letters and numbers.

    Ensure App Passwords are Enabled:

    Go to your Google Account: https://myaccount.google.com/
    Click on "Security" in the left-hand menu.
    Scroll down to the "How you sign in to Google" section and click on "App passwords".
    Make sure "App passwords" are turned on. If it's off, turn it on.
    If it's on, double-check that you generated an App password for "Mail" on "Other" devices.
    Recent Password Change: If you recently changed your main Google account password, you might need to regenerate a new App password.

    Two-Factor Authentication (2FA): App passwords require 2-Factor Authentication to be enabled on your Google account. Make sure 2FA is turned on.

    Account Restrictions: In rare cases, there might be temporary restrictions on your Google account that prevent App passwords from working.

Common ways to automate scripts like this, depending on your operating system:

    1. Using Task Scheduler (Windows):

    Search for "Task Scheduler" in the Windows search bar and open it.
    In the Task Scheduler window, click "Create Basic Task" in the right-hand pane.
    Give your task a name (e.g., "Auto Torrent Check - The White Lotus") and a description.
    Choose a trigger: "Daily," "Weekly," etc., depending on how often you want to check for new episodes. Since new episodes are typically weekly, "Weekly" might be a good starting point.
    Set the start date and time, and how often it should repeat.
    For the "Action," choose "Start a program."
    In the "Program/script" field, enter the path to your Python interpreter (e.g., C:\Python39\python.exe).
    In the "Add arguments (optional)" field, enter the path to your Python script file (e.g., C:\path\to\your\script.py).
    Click "Finish."

    2. Using cron (macOS and Linux):

    Open the Terminal application.
    Type 'crontab -e' and press Enter. This will open the cron table file in a text editor. You might be asked to choose an editor the first time.
    Add a new line to the file with the schedule and the command to run your script. The cron syntax can be a bit tricky, but there are many online resources to help you. For example, to run the script daily at 9 AM, you might use: "0 9 * * * python /path/to/your/script.py"
    Save the file (usually ctrl+x, then y) and exit the editor. cron will automatically pick up the changes.

If you want to test your script, run it in Python after updating email and search parameters. 