# -*- coding: utf-8 -*-

'''
Receive session_key and IP from PlexPy when playback starts. 
Use IP to check against blacklist.
If not in whitelist use session_key to determine stream and kill.

PlexPy > Settings > Notification Agents > Scripts > Bell icon:
        [X] Notify on playback start
PlexPy > Settings > Notification Agents > Scripts > Gear icon:
        Playback Start: ip_blacklist.py
PlexPy > Settings > Notifications > Script > Script Arguments:
        {session_key} {ip_address}

'''

import sys
import requests
from plexapi.server import PlexServer
# pip install plexapi


## EDIT THESE SETTINGS ##
PLEX_TOKEN = 'xxxxxx'
PLEX_URL = 'http://localhost:32400'

PLEXPY_APIKEY = 'xxxxxx'  # Your PlexPy API key
PLEXPY_URL = 'http://localhost:8182/'  # Your PlexPy URL

IP_BLACKLIST = ['10.10.0.12']  # List IP addresses.
IGNORE_LST = ('')  # List usernames that should be ignored.

REASON = 'IP Address: {} was found in blacklist.'

AGENT_ID = 14  # Notification agent ID for PlexPy
# Find Notification agent ID here:
# https://github.com/JonnyWong16/plexpy/blob/master/API.md#notify

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
    # Send the notification through PlexPy
    payload = {'apikey': PLEXPY_APIKEY,
               'cmd': 'notify',
               'agent_id': AGENT_ID,
               'subject': subject,
               'body': body}

    try:
        r = requests.post(PLEXPY_URL.rstrip('/') + '/api/v2', params=payload)
        response = r.json()

        if response['response']['result'] == 'success':
            sys.stdout.write("Successfully sent PlexPy notification.")
        else:
            raise Exception(response['response']['message'])
    except Exception as e:
        sys.stderr.write("PlexPy API 'notify' request failed: {0}.".format(e))
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
