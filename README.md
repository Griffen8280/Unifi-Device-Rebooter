# Unifi-Device-Rebooter
**Note: you will need to ssh into each of your devices at least once to accept their ssh key before this will work as an automation**

## Why?
This project started after I couldn't find a decent way to automatically reboot my unifi devices.  The unifi control panel software doesn't provide a way to schedule reboots and many of the "cron" tutorials out there just didn't work because of the confirmation dialog that is required in many unifi devices when running the reboot command.

## Requirements
A requirements.txt is included with this file which you can run with:  
`pip install -r requirements.txt`
Also you will need plink (putty module) for this to work correctly, to install this run:  
`winget install putty.putty`

## Operation
simply running the reboot.py file with python is all that is needed for a default setup.  You will need to update the line:  
`ssh_tunnel = pexpect.popen_spawn.PopenSpawn('plink username@IPADDRESS -pw password -batch', encoding='utf-8')`  
And input the variables for your setup in the fields  
1. username
2. IPADDRESS
3. password

## Scheduled Task
This can be setup to run from a Windows scheduled task.  I have set my wireless ap's to reboot nightly and my main router to reboot weekly.  Your setup should look something like the following screenshots:  
![Screenshot 2022-12-07 104512](https://user-images.githubusercontent.com/42878642/206225946-2e55be1f-2273-458c-b7f9-8007e7356d50.png)

![Screenshot 2022-12-07 104540](https://user-images.githubusercontent.com/42878642/206226013-a7b99dba-0eb3-4bb3-bfeb-c6065a2ca133.png)

![Screenshot 2022-12-07 104610](https://user-images.githubusercontent.com/42878642/206226066-02692912-3dea-49c5-af8d-7ae9e5a30c3b.png)

![Screenshot 2022-12-07 104627](https://user-images.githubusercontent.com/42878642/206226082-baf31ef3-ff15-49f9-9c88-0414a064ade7.png)

![Screenshot 2022-12-07 104740](https://user-images.githubusercontent.com/42878642/206226095-9d63f576-cb9b-478f-8183-57f951b9a9ba.png)  
Note: On this slide be sure to use the full path names for where the files are located ie.  
1. "C:\Program Files\Python311\python.exe" (Note the quotes, they are important!)
2. "C:\Users\username\unifi reboots\firstfloor.py" (Again note the quotes are still there)  
Finally on the last slide click the Finish button  
Then double click your newly created task to open the properties box (or right-click -> properties)  
![Screenshot 2022-12-07 105635](https://user-images.githubusercontent.com/42878642/206227530-79ad0b81-6327-4b98-9a22-f1f27048a7d6.png)  
On this box ensure the "Run whether user is logged on or not" radio button is checked and click "OK"  
You will then be prompted for your user password and that's it.  You can run this task on-demand or wait for the next scheduled time.
