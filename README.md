# woffu-autologin-script
This is a small script that auto checks you into your Woffu organization, based on the original https://github.com/d-hervas/woffu-autologin-script

I forked this project from the original to add support for automatic detection of working days. Working days are defined as:

* not in the weekend
* not a requested PTO
* and not a bank holiday

The script won't sign in if today is detected as a non-working day.

The simplest way to use it is to set up a cron job / scheduled task that signs you on/off. The script does not know anything about changes in your working hours (i.e. summer schedule) and you need to address that in your cron job.
