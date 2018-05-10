# Tautulli blacklist script

Copy pasta ip_whitelist.py from [blacktwin/JBOPS](https://github.com/blacktwin/JBOPS) 

I just changed some variables to make it a blacklist instead. 

[ip_blacklist.py](https://github.com/gilbN/Nostromo/blob/master/Server/scripts/plexpy/ip_blacklist.py) 

* * *

## Blacklist Notifications

Add a new notification agent and set **Triggers** to `Playback Stop`

![](https://github.com/gilbN/Nostromo/blob/master/Server/scripts/plexpy/img/triggered.png)

Set **Conditions** to `IP Address` `is` `<blacklisted IP>` Add the IP you want to blacklist here.

![](https://github.com/gilbN/Nostromo/blob/master/Server/scripts/plexpy/img/conditions.png)

Add Notification **Text** on `Playback Stop`

Subject Line: e.g. `IP Blacklisted 🚫`

Message Body: e.g. `Killed {user}'s stream of {title}. IP: {ip_address} in blacklist`

![](https://github.com/gilbN/Nostromo/blob/master/Server/scripts/plexpy/img/text.png)


Discord example notification

![](https://github.com/gilbN/Nostromo/blob/master/Server/scripts/plexpy/img/culled.png)

