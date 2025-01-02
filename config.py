#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7982396596:AAGZJZj1Gqc6XV46-9nXl-af1mhwAnLV6PU")
    API_ID = int(os.environ.get("API_ID", "28094744"))
    API_HASH = os.environ.get("API_HASH", "a75af4285edc7747c57bb19147ca0b9b")
    AUTH_USERS = "5680454765"

