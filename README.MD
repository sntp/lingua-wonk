# Lingua Wonk
Shows words from Lingualeo dictionary in notifications. For Linux.

![wonk](https://cloud.githubusercontent.com/assets/7084556/17821908/14b5dade-6665-11e6-8714-d568b13e0d1a.png)

# Usage
* Install dependencies
  * sudo apt install notify-send
  * sudo apt install mpg123
* Specify your email and password in credentials.txt
* Add cron job

        $ crontab -e
        * * * * * cd *LINGUA/WONK/DIRECTORY* && bash cronjob.sh  >/dev/null 2>&1

# Arguments:
    -ns         Play no sound
    -np         Show no picture
    -ne         Show no example

# In addition
* Use [browser add-ons](http://lingualeo.com/ru/browserapps)
* If you want to show different examples you can separate them by '|' in dictionary