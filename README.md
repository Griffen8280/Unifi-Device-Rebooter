# Unifi-Device-Rebooter

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
