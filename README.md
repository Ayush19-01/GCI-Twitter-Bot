# GCI-Twitter-Bot
___Modules Used: feedparser, selenium, pyautogui___
## How it works:
Firtsly the feedparser module is used to get the link and the title of the latest fedora blog.

After that the user is asked to enter it's twitter username ans password to log in .

After entering the credentials the default web browser is opened on its own with selenium.

A web driver is required for the program to run successfully, here I have used the chrome driver, if you don't have it download  the suitable driver from [here](https://chromedriver.storage.googleapis.com/index.html?path=79.0.3945.36/) and paste it in the same folder as the program is running.

Excpecting that the credentials are the correct the user will get logged into his\her twitter account.

After a relaxation time of  7 seconds the tweet is made.

___Note that same tweet cannot be made twice so if a tweet has been made please delete it before running the program again___
