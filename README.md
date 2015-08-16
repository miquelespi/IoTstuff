# IoTstuff

IoT stuff that runs on my raspberry.

At this point, this repository just features sample code that obtains data from a thermometer and humidity sensor connected to a Raspberry Pi. The script also uses python package "gspread" to connect to a Google Drive hosted spreadsheet, and stores the values and time there. This requires a Google Drive API JSON credential file stored in the machine where this script runs (you can get one from you Google developer console). In my specific setup, I call this script every 5 minutes using root's crontab in the raspi, as accessing the GPIO requires root access.

You can find a repository with a front-end app that shows graphs with data obtained from the spreadsheet mentioned above at https://github.com/miquelespi/longnap_iot. There is an actual app with this front-end up and running at http://iot.longnap.com.
