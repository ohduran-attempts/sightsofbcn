#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Use text editor to edit the script and type in valid Instagram username/password
from InstagramAPI import InstagramAPI

from ..env import PASSWORD, USERNAME

InstagramAPI = InstagramAPI("login", "password")
InstagramAPI.login()  # login

photo_path = '_incrediblebarcelona/15251634_1287660147972927_2075023967713755136_a.jpg'
caption = "Sample photo"
InstagramAPI.uploadPhoto(photo_path, caption=caption)
