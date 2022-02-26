# occasion_reminder_with_twilio

This project was made as part of a hackathon conducted at Virginia Tech. The app uses Twilio as a means to send reminders for the very important occasions of your dearest friends and helps you to nurture the relationship between them.

## Platform
`Windows`

## Languages
`Python3` `Bat` `JSON`

## Requirements
`pip install twilio`

## **About Twilio**
Twilio acts as a REST API to communicate information (text, video, audio) with the world.

Steps
1. Create Your twilio account and verify your phone number from https://www.twilio.com/console/phone-numbers/verified <br/>
2. Get your twilio credentials from https://www.twilio.com/console and update the `credentials.py` accordingly. <br/>
3. Create a bat file `scheduler.bat` with the code `C:\Python37\python.exe "full file path to the place where this repo is checkout\send_sms.py" <br/>
4. Update the Json with your beloved birthdays and other occassions. <br/>
5. From windows, search and open Task Scheduler <br/>
6. From the Actions panel, click on Create Basic Task <br/>
7. Enter Name (e.g: Wish Reminder) and description (e.g: runs every day at 12:00 AM) for the underlying task <br/>
8. Choose Trigger (e.g: daily) and time (e.g: 12:00:AM) <br/>
9. Start the program <br/>
10. Insert the `scheduler.bat` file path <br/>
11. Finish <br/>

# Results
![image](https://user-images.githubusercontent.com/14051949/155824294-3cecb0dd-6926-440d-a78b-9d6eb046559c.png)

# Future Updates
1. Store Successful and Error Messages in a Database.
2. Automate the process of fetching important dates from Social platforms.
