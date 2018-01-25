import subprocess as sp
import os
import numpy

FFMPEG_BIN = '/usr/bin/ffmpeg'

cmds = ['FFMPEG_BIN' '-ss' '00:00:45' '-i' 'Avengers.mp4' '-vframes 1' '-q:v' '2' 'output1.jpg']


ffprobe_p = sp.Popen(cmds, stdin=sp.PIPE, 
stdout=sp.PIPE, stderr=sp.PIPE)
