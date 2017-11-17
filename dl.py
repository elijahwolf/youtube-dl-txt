#!/usr/bin/python
# download txt file of youtube urls
# elijah mccormick
# c-sats 2017

import subprocess
import os

# declare variables
fname = 'urls.txt'

# counter
x = 0

# get length of txt file for number of videos
def flength(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

# assign length of txt file
length = flength(fname)

# read and store txt file
f = open('urls.txt')
text = f.readlines()

# run youtube-dl until end of txt file
while (x < length):
    #    os.system("youtube-dl -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4' " + text[x])
    process = subprocess.Popen("youtube-dl -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4' " + text[x], shell=True)
    process.wait()
    x = x + 1
