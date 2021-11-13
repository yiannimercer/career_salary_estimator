#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 13:23:57 2021

@author: yiannimercer
"""

import glassdoor_scraper as gs
import pandas as pd

path = "/Users/yiannimercer/Desktop/chromedriver"

df = gs.get_jobs('data scientist', 15, False,path,15)

