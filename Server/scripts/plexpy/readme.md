# Tautulli blacklist script

Copy pasta ip_whitelist.py from [blacktwin/JBOPS](https://github.com/blacktwin/JBOPS) 

I just changed some variables to make it a blacklist instead. 

[ip_blacklist.py](https://github.com/gilbN/Nostromo/blob/master/Server/scripts/plexpy/ip_blacklist.py)  

## Blacklist Notifications

Add a new notification agent and set trigger to `Playback Stop`

Set condition to `IP Address` `is` `[blacklist IP]`

Add Notification text on `Playback Stop`

Subject Line: e.g. `IP Blacklisted 🚫`

Message Body: e.g. `Killed {user}'s stream of {title}. IP: {ip_address} in blacklist`

![](https://github.com/gilbN/Nostromo/blob/master/Server/scripts/plexpy/culled.png)

