# -*- coding: utf-8 -*-

'''
Receive session_key and IP from Tautulli when playback starts. 
Use IP to check against blacklist.
If in blacklist use session_key to determine stream and kill.

Tautulli > Settings > Notification Agents > Scripts > Bell icon:
        [X] Notify on playback start
Tautulli > Settings > Notification Agents > Scripts > Gear icon:
        Playback Start: ip_blacklist.py
Tautulli > Settings > Notifications > Script > Script Arguments:
        {session_key} {ip_address}

'''

import sys
import requests
from plexapi.server import PlexServer
import configparser


## EDIT THESE SETTINGS ##
PLEX_TOKEN = 'xxxxxxxx'
PLEX_URL = 'http://localhost:32400'

TAUTULLI_APIKEY = 'xxxxxxxxxxx'  # Your Tautulli API key
TAUTULLI_URL = 'http://localhost:8181/'  # Your Tautulli URL

IP_BLACKLIST = ['192.168.1.160','10.10.1.87','192.168.1.18']  # List IP addresses.
IGNORE_LST = ('')  # List usernames that should be ignored.

REASON = 'IP Address: {} was found in blacklist.'

NOTIFIER_ID = 14  # Notification agent ID for Tautulli
# Find Notification agent ID here:
# Tautulli Settings -> NOTIFICATION AGENTS -> :bell: Agent (NotifierID - {Description)

SUBJECT_TEXT = "IP Blacklist Violation"
BODY_TEXT = "Killed {user}'s stream of {title}. IP: {ip} in blacklist"
##/EDIT THESE SETTINGS ##

sessionKey = sys.argv[1]
ip_address = sys.argv[2]

sess = requests.Session()
sess.verify = False
plex = PlexServer(PLEX_URL, PLEX_TOKEN, session=sess)

def send_notification(subject_text, body_text):
    # Format notification text
    try:
        subject = subject_text
        body = body_text

    except LookupError as e:
        sys.stderr.write("Unable to substitute '{0}' in the notification subject or body".format(e))
        return None
    # Send the notification through Tautulli
    payload = {'apikey': TAUTULLI_APIKEY,
               'cmd': 'notify',
               'notifier_id': NOTIFIER_ID,
               'subject': subject,
               'body': body}

    try:
        r = requests.post(TAUTULLI_URL.rstrip('/') + '/api/v2', params=payload)
        response = r.json()

        if response['response']['result'] == 'success':
            sys.stdout.write("Successfully sent Tautulli notification.")
        else:
            raise Exception(response['response']['message'])
    except Exception as e:
        sys.stderr.write("Tautulli API 'notify' request failed: {0}.".format(e))
        return None


if ip_address in IP_BLACKLIST:
    for session in plex.sessions():
        username = session.usernames[0]
        title = (session.grandparentTitle + ' - ' if session.type == 'episode' else '') + session.title
        if session.sessionKey == int(sessionKey) and username not in IGNORE_LST:
            sys.stdout.write("Killing {user}'s stream of {title}. IP: {ip} in blacklist".format(
                user=username, title=title, ip=ip_address))
            session.stop(reason=REASON.format(ip_address))
            send_notification(SUBJECT_TEXT, BODY_TEXT.format(user=username, ip=ip_address, title=title))
        else:
            sys.stdout.write('User: {} is ignored from this script.'.format(username))
else:
    sys.stdout.write('IP: {} is not in blacklist, ignoring.'.format(ip_address))
