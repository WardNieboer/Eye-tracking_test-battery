#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on October 03, 2024, at 07:08
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'Nieboer_eye-tracking-test-battery'  # from the Builder filename that created this script
expInfo = {'pilot': '01', 'participant': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='E:\\2023 eye-tracking study\\Public test+analysis\\Nieboer_eye-tracking-test-battery.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=1, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='ACER', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "intro"
introClock = core.Clock()
black_background1 = visual.Rect(
    win=win, name='black_background1',
    width=(1.8, 1)[0], height=(1.8, 1)[1],
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor='black',
    opacity=None, depth=0.0, interpolate=True)
introduction = visual.TextStim(win=win, name='introduction',
    text='This test battery of eye movements was developed by Ward Nieboer with the aim to assess visual function in individuals with vision impairment. \n\nThe test battery consists of 7 components:\n1) Calibration check\n2) Visual search familiarisation + test\n3) Fixation stability test\n4) Saccades test\n5) Smooth pursuit test\n6) Free viewing photos\n7) Free viewing video\n\nReferences:\nNieboer, W., Ghiani, A., De Vries, R., Brenner, E., & Mann, D. L. (2023). Eye Tracking to Assess the Functional Consequences of Vision Impairment: A Systematic Review. Optometry and Vision Science, 100(12), 861-875.',
    font='Open Sans',
    pos=(0, 0), height=0.025, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
intro_done = keyboard.Keyboard()

# Initialize components for Routine "Calibration"
CalibrationClock = core.Clock()
Black_background2 = visual.Rect(
    win=win, name='Black_background2',
    width=(1.8, 1)[0], height=(1.8, 1)[1],
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor='black',
    opacity=None, depth=0.0, interpolate=True)
calibration_done = keyboard.Keyboard()
middle = visual.ShapeStim(
    win=win, name='middle',
    size=(0.25, 0.25), vertices='circle',
    ori=0.0, pos=(0, 0),
    lineWidth=5.0,     colorSpace='rgb',  lineColor='white', fillColor=None,
    opacity=None, depth=-2.0, interpolate=True)
top_left = visual.ShapeStim(
    win=win, name='top_left',
    size=(0.25, 0.25), vertices='circle',
    ori=0.0, pos=(-0.60, 0.3),
    lineWidth=5.0,     colorSpace='rgb',  lineColor='white', fillColor=None,
    opacity=None, depth=-3.0, interpolate=True)
top_right = visual.ShapeStim(
    win=win, name='top_right',
    size=(0.25, 0.25), vertices='circle',
    ori=0.0, pos=(0.6, 0.3),
    lineWidth=5.0,     colorSpace='rgb',  lineColor='white', fillColor=None,
    opacity=None, depth=-4.0, interpolate=True)
bottom_left = visual.ShapeStim(
    win=win, name='bottom_left',
    size=(0.25, 0.25), vertices='circle',
    ori=0.0, pos=(-0.6, -0.3),
    lineWidth=5.0,     colorSpace='rgb',  lineColor='white', fillColor=None,
    opacity=None, depth=-5.0, interpolate=True)
bottom_right = visual.ShapeStim(
    win=win, name='bottom_right',
    size=(0.25, 0.25), vertices='circle',
    ori=0.0, pos=(0.6, -0.3),
    lineWidth=5.0,     colorSpace='rgb',  lineColor='white', fillColor=None,
    opacity=None, depth=-6.0, interpolate=True)
M_fill = visual.ShapeStim(
    win=win, name='M_fill',
    size=(0.25, 0.25), vertices='circle',
    ori=0.0, pos=(0, 0),
    lineWidth=2.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=1.0, depth=-7.0, interpolate=True)
TL_fill = visual.ShapeStim(
    win=win, name='TL_fill',
    size=(0.25, 0.25), vertices='circle',
    ori=0.0, pos=(-0.60, 0.3),
    lineWidth=2.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=1.0, depth=-8.0, interpolate=True)
TR_fill = visual.ShapeStim(
    win=win, name='TR_fill',
    size=(0.25, 0.25), vertices='circle',
    ori=0.0, pos=(0.6, 0.3),
    lineWidth=2.0,     colorSpace='rgb',  lineColor=None, fillColor='white',
    opacity=1.0, depth=-9.0, interpolate=True)
BR_fill = visual.ShapeStim(
    win=win, name='BR_fill',
    size=(0.25, 0.25), vertices='circle',
    ori=0.0, pos=(0.6, -0.3),
    lineWidth=2.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=1.0, depth=-10.0, interpolate=True)
BL_fill = visual.ShapeStim(
    win=win, name='BL_fill',
    size=(0.25, 0.25), vertices='circle',
    ori=0.0, pos=(-0.6, -0.3),
    lineWidth=2.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=1.0, depth=-11.0, interpolate=True)

# Initialize components for Routine "inst_fam_3x3"
inst_fam_3x3Clock = core.Clock()
black_background3 = visual.Rect(
    win=win, name='black_background3',
    width=(1.8, 1)[0], height=(1.8, 1)[1],
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor='black',
    opacity=None, depth=0.0, interpolate=True)
VS_familiarisation_opening = visual.TextStim(win=win, name='VS_familiarisation_opening',
    text='VISUAL SEARCH:\n\nYour task is to determine whether a circle is present among a grid of squares. You have 30 seconds per trial to respond. Press the left arrow key if there is no circle present, press the right arrow key if you find a circle.\n\nWe will now start with 6 practice trials to familiarise you with the task.\n\nPress the left or right arrow key to start.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
resp_familiarisation = keyboard.Keyboard()

# Initialize components for Routine "familiarisation"
familiarisationClock = core.Clock()
resp_fam = keyboard.Keyboard()
figs_fam = visual.ImageStim(
    win=win,
    name='figs_fam', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)

# Initialize components for Routine "blank"
blankClock = core.Clock()
waiting_screen = visual.Rect(
    win=win, name='waiting_screen',
    width=(1.8,1)[0], height=(1.8,1)[1],
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor='black',
    opacity=None, depth=0.0, interpolate=True)

# Initialize components for Routine "instr_3x3"
instr_3x3Clock = core.Clock()
black_background4 = visual.Rect(
    win=win, name='black_background4',
    width=(1.8, 1)[0], height=(1.8, 1)[1],
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor='black',
    opacity=None, depth=0.0, interpolate=True)
VS_instruction_done = keyboard.Keyboard()
instr_test_start = visual.TextStim(win=win, name='instr_test_start',
    text='We will now begin the test. The first block will be 18 trials with a 3x3 grid, the second block 18 trials with a 8x8 grid and the third and final block 18 trials with a 15x15 grid.\n\nYou can take a short break between blocks if needed. \n\nIf you fully understand the task and you are ready to start, press the right key arrow.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "routine_3x3"
routine_3x3Clock = core.Clock()
resp_3x3 = keyboard.Keyboard()
figs_3x3 = visual.ImageStim(
    win=win,
    name='figs_3x3', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)

# Initialize components for Routine "blank"
blankClock = core.Clock()
waiting_screen = visual.Rect(
    win=win, name='waiting_screen',
    width=(1.8,1)[0], height=(1.8,1)[1],
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor='black',
    opacity=None, depth=0.0, interpolate=True)

# Initialize components for Routine "break_3"
break_3Clock = core.Clock()
black_background5 = visual.Rect(
    win=win, name='black_background5',
    width=(1.8, 1)[0], height=(1.8, 1)[1],
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor='black',
    opacity=None, depth=0.0, interpolate=True)
break1 = visual.TextStim(win=win, name='break1',
    text='break',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
break_over = keyboard.Keyboard()

# Initialize components for Routine "routine_8x8"
routine_8x8Clock = core.Clock()
resp_8x8 = keyboard.Keyboard()
figs_8x8 = visual.ImageStim(
    win=win,
    name='figs_8x8', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)

# Initialize components for Routine "blank"
blankClock = core.Clock()
waiting_screen = visual.Rect(
    win=win, name='waiting_screen',
    width=(1.8,1)[0], height=(1.8,1)[1],
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor='black',
    opacity=None, depth=0.0, interpolate=True)

# Initialize components for Routine "break_3"
break_3Clock = core.Clock()
black_background5 = visual.Rect(
    win=win, name='black_background5',
    width=(1.8, 1)[0], height=(1.8, 1)[1],
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor='black',
    opacity=None, depth=0.0, interpolate=True)
break1 = visual.TextStim(win=win, name='break1',
    text='break',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
break_over = keyboard.Keyboard()

# Initialize components for Routine "routine_15x15"
routine_15x15Clock = core.Clock()
resp_15x15 = keyboard.Keyboard()
figs_15x15 = visual.ImageStim(
    win=win,
    name='figs_15x15', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)

# Initialize components for Routine "blank"
blankClock = core.Clock()
waiting_screen = visual.Rect(
    win=win, name='waiting_screen',
    width=(1.8,1)[0], height=(1.8,1)[1],
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor='black',
    opacity=None, depth=0.0, interpolate=True)

# Initialize components for Routine "inst_fix"
inst_fixClock = core.Clock()
black_background6 = visual.Rect(
    win=win, name='black_background6',
    width=(1.8, 1)[0], height=(1.8, 1)[1],
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor='black',
    opacity=None, depth=0.0, interpolate=True)
FS_instruction_done = keyboard.Keyboard()
Fixation_stability_instruction = visual.TextStim(win=win, name='Fixation_stability_instruction',
    text='FIXATION STABILITY:\n\nFor the next test, you have to fixate as steady as possible on the center of the cross for 30 seconds. Please limit any head or eye movements.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "fix_stab"
fix_stabClock = core.Clock()
black_background7 = visual.Rect(
    win=win, name='black_background7',
    width=(1.8, 1)[0], height=(1.8, 1)[1],
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor='black',
    opacity=None, depth=0.0, interpolate=True)
interrupt_FS = keyboard.Keyboard()
horizontal = visual.Rect(
    win=win, name='horizontal',units='deg', 
    width=(40,1)[0], height=(40,1)[1],
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor='white',
    opacity=None, depth=-2.0, interpolate=True)
vertical = visual.Rect(
    win=win, name='vertical',units='deg', 
    width=(1,20)[0], height=(1,20)[1],
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor='white',
    opacity=None, depth=-3.0, interpolate=True)
inner_line_horizontal = visual.Rect(
    win=win, name='inner_line_horizontal',units='deg', 
    width=(40,0.4)[0], height=(40,0.4)[1],
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor='black',
    opacity=None, depth=-4.0, interpolate=True)
inner_line_vertical = visual.Rect(
    win=win, name='inner_line_vertical',units='deg', 
    width=(0.4,20)[0], height=(0.4,20)[1],
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor='black',
    opacity=None, depth=-5.0, interpolate=True)

# Initialize components for Routine "instr_saccades"
instr_saccadesClock = core.Clock()
black_background8 = visual.Rect(
    win=win, name='black_background8',
    width=(1.8, 1)[0], height=(1.8, 1)[1],
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor='black',
    opacity=None, depth=0.0, interpolate=True)
saccade_test_instructions = visual.TextStim(win=win, name='saccade_test_instructions',
    text='SACCADES TEST:\n\nFixate on the white dot in the center, it will dissapear and reappear at a different location for 2 seconds before returning to the center. Your task is to locate all dots.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
SAC_instructions_done = keyboard.Keyboard()

# Initialize components for Routine "trial_saccades"
trial_saccadesClock = core.Clock()
black_background9 = visual.Rect(
    win=win, name='black_background9',
    width=(1.8,1)[0], height=(1.8,1)[1],
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor='black',
    opacity=None, depth=0.0, interpolate=True)
SAC_fix_target = visual.ShapeStim(
    win=win, name='SAC_fix_target',units='deg', 
    size=[1.0, 1.0], vertices='circle',
    ori=0.0, pos=(0,0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor='white',
    opacity=None, depth=-1.0, interpolate=True)

# Initialize components for Routine "saccades"
saccadesClock = core.Clock()
black_background10 = visual.Rect(
    win=win, name='black_background10',
    width=(1.8,1)[0], height=(1.8,1)[1],
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor='black',
    opacity=None, depth=0.0, interpolate=True)
N_6 = visual.ShapeStim(
    win=win, name='N_6',units='deg', 
    size=[1.0, 1.0], vertices='circle',
    ori=0.0, pos=(0, 6),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor='white',
    opacity=1.0, depth=-1.0, interpolate=True)
N_10 = visual.ShapeStim(
    win=win, name='N_10',units='deg', 
    size=[1.0, 1.0], vertices='circle',
    ori=0.0, pos=(0, 8),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor='white',
    opacity=1.0, depth=-2.0, interpolate=True)
E_6 = visual.ShapeStim(
    win=win, name='E_6',units='deg', 
    size=[1.0, 1.0], vertices='circle',
    ori=0.0, pos=(6,0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor='white',
    opacity=1.0, depth=-3.0, interpolate=True)
E_10 = visual.ShapeStim(
    win=win, name='E_10',units='deg', 
    size=[1.0, 1.0], vertices='circle',
    ori=0.0, pos=(10,0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor='white',
    opacity=1.0, depth=-4.0, interpolate=True)
S_6 = visual.ShapeStim(
    win=win, name='S_6',units='deg', 
    size=[1.0, 1.0], vertices='circle',
    ori=0.0, pos=(0, -6),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor='white',
    opacity=1.0, depth=-5.0, interpolate=True)
S_10 = visual.ShapeStim(
    win=win, name='S_10',units='deg', 
    size=[1.0, 1.0], vertices='circle',
    ori=0.0, pos=(0, -8),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor='white',
    opacity=1.0, depth=-6.0, interpolate=True)
W_6 = visual.ShapeStim(
    win=win, name='W_6',units='deg', 
    size=[1.0, 1.0], vertices='circle',
    ori=0.0, pos=(-6,0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor='white',
    opacity=1.0, depth=-7.0, interpolate=True)
W_10 = visual.ShapeStim(
    win=win, name='W_10',units='deg', 
    size=[1.0, 1.0], vertices='circle',
    ori=0.0, pos=(-10,0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor='white',
    opacity=1.0, depth=-8.0, interpolate=True)
NE_10 = visual.ShapeStim(
    win=win, name='NE_10',units='deg', 
    size=[1.0, 1.0], vertices='circle',
    ori=0.0, pos=(6,6),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor='white',
    opacity=1.0, depth=-9.0, interpolate=True)
SE_10 = visual.ShapeStim(
    win=win, name='SE_10',units='deg', 
    size=[1.0, 1.0], vertices='circle',
    ori=0.0, pos=(-6,6),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor='white',
    opacity=1.0, depth=-10.0, interpolate=True)
SW_10 = visual.ShapeStim(
    win=win, name='SW_10',units='deg', 
    size=[1.0, 1.0], vertices='circle',
    ori=0.0, pos=(-6,-6),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor='white',
    opacity=1.0, depth=-11.0, interpolate=True)
NW_10 = visual.ShapeStim(
    win=win, name='NW_10',units='deg', 
    size=[1.0, 1.0], vertices='circle',
    ori=0.0, pos=(-6,6),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor='white',
    opacity=1.0, depth=-12.0, interpolate=True)

# Initialize components for Routine "instr_SP"
instr_SPClock = core.Clock()
black_background11 = visual.Rect(
    win=win, name='black_background11',
    width=(1.8, 1)[0], height=(1.8, 1)[1],
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor='black',
    opacity=None, depth=0.0, interpolate=True)
SP_instructions_done = visual.TextStim(win=win, name='SP_instructions_done',
    text='SMOOTH PURSUIT TEST:\n\nFixate on the white dot in the center, it will disappear and reappear at a different location and will move in towards the center of the screen before returning as a central fixation point. Your task is to find and follow the dot.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
Smooth_pursuit_instructions = keyboard.Keyboard()

# Initialize components for Routine "fix"
fixClock = core.Clock()
black_background12 = visual.Rect(
    win=win, name='black_background12',
    width=(1.8,1)[0], height=(1.8,1)[1],
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor='black',
    opacity=None, depth=0.0, interpolate=True)
SP_fixation_target = visual.ShapeStim(
    win=win, name='SP_fixation_target',units='deg', 
    size=[1.0, 1.0], vertices='circle',
    ori=0.0, pos=(0,0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor='white',
    opacity=None, depth=-1.0, interpolate=True)

# Initialize components for Routine "start_sp"
start_spClock = core.Clock()
black_background13 = visual.Rect(
    win=win, name='black_background13',
    width=(1.8,1)[0], height=(1.8,1)[1],
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor='black',
    opacity=None, depth=0.0, interpolate=True)
stimuli_north_2 = visual.ShapeStim(
    win=win, name='stimuli_north_2',units='deg', 
    size=[1.0, 1.0], vertices='circle',
    ori=0.0, pos=(0, 6),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor='white',
    opacity=1.0, depth=-1.0, interpolate=True)
stimuli_east_2 = visual.ShapeStim(
    win=win, name='stimuli_east_2',units='deg', 
    size=[1.0, 1.0], vertices='circle',
    ori=0.0, pos=(6, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor='white',
    opacity=1.0, depth=-2.0, interpolate=True)
stimuli_south_2 = visual.ShapeStim(
    win=win, name='stimuli_south_2',units='deg', 
    size=[1.0, 1.0], vertices='circle',
    ori=0.0, pos=(0,-6),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor='white',
    opacity=1.0, depth=-3.0, interpolate=True)
stimuli_west_2 = visual.ShapeStim(
    win=win, name='stimuli_west_2',units='deg', 
    size=[1.0, 1.0], vertices='circle',
    ori=0.0, pos=(-6, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor='white',
    opacity=1.0, depth=-4.0, interpolate=True)

# Initialize components for Routine "trial_SP"
trial_SPClock = core.Clock()
black_background14 = visual.Rect(
    win=win, name='black_background14',
    width=(1.8,1)[0], height=(1.8,1)[1],
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor='black',
    opacity=None, depth=0.0, interpolate=True)
stimuli_north = visual.ShapeStim(
    win=win, name='stimuli_north',units='deg', 
    size=[1.0, 1.0], vertices='circle',
    ori=0.0, pos=[0,0],
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor='white',
    opacity=1.0, depth=-1.0, interpolate=True)
stimuli_east = visual.ShapeStim(
    win=win, name='stimuli_east',units='deg', 
    size=[1.0, 1.0], vertices='circle',
    ori=0.0, pos=[0,0],
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor='white',
    opacity=1.0, depth=-2.0, interpolate=True)
stimuli_south = visual.ShapeStim(
    win=win, name='stimuli_south',units='deg', 
    size=[1.0, 1.0], vertices='circle',
    ori=0.0, pos=[0,0],
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor='white',
    opacity=1.0, depth=-3.0, interpolate=True)
stimuli_west = visual.ShapeStim(
    win=win, name='stimuli_west',units='deg', 
    size=[1.0, 1.0], vertices='circle',
    ori=0.0, pos=[0,0],
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor='white',
    opacity=1.0, depth=-4.0, interpolate=True)
SP_fixation_target2 = visual.ShapeStim(
    win=win, name='SP_fixation_target2',units='deg', 
    size=[1.0, 1.0], vertices='circle',
    ori=0.0, pos=(0,0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor='white',
    opacity=1.0, depth=-5.0, interpolate=True)
SP_fixation_target3 = visual.ShapeStim(
    win=win, name='SP_fixation_target3',units='deg', 
    size=[1.0, 1.0], vertices='circle',
    ori=0.0, pos=(0,0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor='white',
    opacity=1.0, depth=-6.0, interpolate=True)

# Initialize components for Routine "instr_free_view"
instr_free_viewClock = core.Clock()
black_background15 = visual.Rect(
    win=win, name='black_background15',
    width=(1.8, 1)[0], height=(1.8, 1)[1],
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor='black',
    opacity=None, depth=0.0, interpolate=True)
instructions_free_view = visual.TextStim(win=win, name='instructions_free_view',
    text='FREE VIEWING:\n\nFor the next two tests, there are no instructions. We will present to you 30 photos with different content, each will be visible for 3 seconds. You can just freely look at the photos. Afterwards, we will play a 1-minute video, and again, you can just freely watch the video.\n\nEnjoy!',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
FV_instructions_done = keyboard.Keyboard()

# Initialize components for Routine "free_viewing_photos"
free_viewing_photosClock = core.Clock()
FV_photo = visual.ImageStim(
    win=win,
    name='FV_photo', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(1.8, 1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# Initialize components for Routine "break_3"
break_3Clock = core.Clock()
black_background5 = visual.Rect(
    win=win, name='black_background5',
    width=(1.8, 1)[0], height=(1.8, 1)[1],
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor='black',
    opacity=None, depth=0.0, interpolate=True)
break1 = visual.TextStim(win=win, name='break1',
    text='break',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
break_over = keyboard.Keyboard()

# Initialize components for Routine "FV_video"
FV_videoClock = core.Clock()
black_background17 = visual.Rect(
    win=win, name='black_background17',
    width=(1.8, 1)[0], height=(1.8, 1)[1],
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor='black',
    opacity=None, depth=0.0, interpolate=True)
interrupt_video = keyboard.Keyboard()
free_view_video = visual.MovieStim3(
    win=win, name='free_view_video',
    noAudio = True,
    filename='Free-view_vid.mp4',
    ori=0.0, pos=(0, 0), opacity=1.0,
    loop=False,
    depth=-2.0,
    )

# Initialize components for Routine "done"
doneClock = core.Clock()
black_background16 = visual.Rect(
    win=win, name='black_background16',
    width=(1.8, 1)[0], height=(1.8, 1)[1],
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor='black',
    opacity=None, depth=0.0, interpolate=True)
done_txt = visual.TextStim(win=win, name='done_txt',
    text='Testing done!\n\nThank you.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "intro"-------
continueRoutine = True
# update component parameters for each repeat
intro_done.keys = []
intro_done.rt = []
_intro_done_allKeys = []
# keep track of which components have finished
introComponents = [black_background1, introduction, intro_done]
for thisComponent in introComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
introClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "intro"-------
while continueRoutine:
    # get current time
    t = introClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=introClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *black_background1* updates
    if black_background1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        black_background1.frameNStart = frameN  # exact frame index
        black_background1.tStart = t  # local t and not account for scr refresh
        black_background1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(black_background1, 'tStartRefresh')  # time at next scr refresh
        black_background1.setAutoDraw(True)
    
    # *introduction* updates
    if introduction.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        introduction.frameNStart = frameN  # exact frame index
        introduction.tStart = t  # local t and not account for scr refresh
        introduction.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(introduction, 'tStartRefresh')  # time at next scr refresh
        introduction.setAutoDraw(True)
    
    # *intro_done* updates
    waitOnFlip = False
    if intro_done.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intro_done.frameNStart = frameN  # exact frame index
        intro_done.tStart = t  # local t and not account for scr refresh
        intro_done.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intro_done, 'tStartRefresh')  # time at next scr refresh
        intro_done.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(intro_done.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(intro_done.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if intro_done.status == STARTED and not waitOnFlip:
        theseKeys = intro_done.getKeys(keyList=['y', 'n', 'left', 'right', 'space'], waitRelease=False)
        _intro_done_allKeys.extend(theseKeys)
        if len(_intro_done_allKeys):
            intro_done.keys = _intro_done_allKeys[-1].name  # just the last key pressed
            intro_done.rt = _intro_done_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in introComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "intro"-------
for thisComponent in introComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('black_background1.started', black_background1.tStartRefresh)
thisExp.addData('black_background1.stopped', black_background1.tStopRefresh)
thisExp.addData('introduction.started', introduction.tStartRefresh)
thisExp.addData('introduction.stopped', introduction.tStopRefresh)
# check responses
if intro_done.keys in ['', [], None]:  # No response was made
    intro_done.keys = None
thisExp.addData('intro_done.keys',intro_done.keys)
if intro_done.keys != None:  # we had a response
    thisExp.addData('intro_done.rt', intro_done.rt)
thisExp.addData('intro_done.started', intro_done.tStartRefresh)
thisExp.addData('intro_done.stopped', intro_done.tStopRefresh)
thisExp.nextEntry()
# the Routine "intro" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
checks = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('calibration_opacity.xlsx'),
    seed=None, name='checks')
thisExp.addLoop(checks)  # add the loop to the experiment
thisCheck = checks.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisCheck.rgb)
if thisCheck != None:
    for paramName in thisCheck:
        exec('{} = thisCheck[paramName]'.format(paramName))

for thisCheck in checks:
    currentLoop = checks
    # abbreviate parameter names if possible (e.g. rgb = thisCheck.rgb)
    if thisCheck != None:
        for paramName in thisCheck:
            exec('{} = thisCheck[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Calibration"-------
    continueRoutine = True
    # update component parameters for each repeat
    calibration_done.keys = []
    calibration_done.rt = []
    _calibration_done_allKeys = []
    M_fill.setOpacity(M_opacity)
    TL_fill.setOpacity(TL_opacity)
    TR_fill.setOpacity(TR_opacity)
    BR_fill.setOpacity(BR_opacity)
    BL_fill.setOpacity(BL_opacity)
    # keep track of which components have finished
    CalibrationComponents = [Black_background2, calibration_done, middle, top_left, top_right, bottom_left, bottom_right, M_fill, TL_fill, TR_fill, BR_fill, BL_fill]
    for thisComponent in CalibrationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    CalibrationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Calibration"-------
    while continueRoutine:
        # get current time
        t = CalibrationClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=CalibrationClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Black_background2* updates
        if Black_background2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Black_background2.frameNStart = frameN  # exact frame index
            Black_background2.tStart = t  # local t and not account for scr refresh
            Black_background2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Black_background2, 'tStartRefresh')  # time at next scr refresh
            Black_background2.setAutoDraw(True)
        
        # *calibration_done* updates
        waitOnFlip = False
        if calibration_done.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            calibration_done.frameNStart = frameN  # exact frame index
            calibration_done.tStart = t  # local t and not account for scr refresh
            calibration_done.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(calibration_done, 'tStartRefresh')  # time at next scr refresh
            calibration_done.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(calibration_done.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(calibration_done.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if calibration_done.status == STARTED and not waitOnFlip:
            theseKeys = calibration_done.getKeys(keyList=['y', 'n', 'left', 'right', 'space'], waitRelease=False)
            _calibration_done_allKeys.extend(theseKeys)
            if len(_calibration_done_allKeys):
                calibration_done.keys = _calibration_done_allKeys[-1].name  # just the last key pressed
                calibration_done.rt = _calibration_done_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *middle* updates
        if middle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            middle.frameNStart = frameN  # exact frame index
            middle.tStart = t  # local t and not account for scr refresh
            middle.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(middle, 'tStartRefresh')  # time at next scr refresh
            middle.setAutoDraw(True)
        
        # *top_left* updates
        if top_left.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            top_left.frameNStart = frameN  # exact frame index
            top_left.tStart = t  # local t and not account for scr refresh
            top_left.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(top_left, 'tStartRefresh')  # time at next scr refresh
            top_left.setAutoDraw(True)
        
        # *top_right* updates
        if top_right.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            top_right.frameNStart = frameN  # exact frame index
            top_right.tStart = t  # local t and not account for scr refresh
            top_right.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(top_right, 'tStartRefresh')  # time at next scr refresh
            top_right.setAutoDraw(True)
        
        # *bottom_left* updates
        if bottom_left.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            bottom_left.frameNStart = frameN  # exact frame index
            bottom_left.tStart = t  # local t and not account for scr refresh
            bottom_left.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(bottom_left, 'tStartRefresh')  # time at next scr refresh
            bottom_left.setAutoDraw(True)
        
        # *bottom_right* updates
        if bottom_right.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            bottom_right.frameNStart = frameN  # exact frame index
            bottom_right.tStart = t  # local t and not account for scr refresh
            bottom_right.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(bottom_right, 'tStartRefresh')  # time at next scr refresh
            bottom_right.setAutoDraw(True)
        
        # *M_fill* updates
        if M_fill.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            M_fill.frameNStart = frameN  # exact frame index
            M_fill.tStart = t  # local t and not account for scr refresh
            M_fill.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(M_fill, 'tStartRefresh')  # time at next scr refresh
            M_fill.setAutoDraw(True)
        
        # *TL_fill* updates
        if TL_fill.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            TL_fill.frameNStart = frameN  # exact frame index
            TL_fill.tStart = t  # local t and not account for scr refresh
            TL_fill.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TL_fill, 'tStartRefresh')  # time at next scr refresh
            TL_fill.setAutoDraw(True)
        
        # *TR_fill* updates
        if TR_fill.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            TR_fill.frameNStart = frameN  # exact frame index
            TR_fill.tStart = t  # local t and not account for scr refresh
            TR_fill.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TR_fill, 'tStartRefresh')  # time at next scr refresh
            TR_fill.setAutoDraw(True)
        
        # *BR_fill* updates
        if BR_fill.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            BR_fill.frameNStart = frameN  # exact frame index
            BR_fill.tStart = t  # local t and not account for scr refresh
            BR_fill.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(BR_fill, 'tStartRefresh')  # time at next scr refresh
            BR_fill.setAutoDraw(True)
        
        # *BL_fill* updates
        if BL_fill.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            BL_fill.frameNStart = frameN  # exact frame index
            BL_fill.tStart = t  # local t and not account for scr refresh
            BL_fill.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(BL_fill, 'tStartRefresh')  # time at next scr refresh
            BL_fill.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in CalibrationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Calibration"-------
    for thisComponent in CalibrationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    checks.addData('Black_background2.started', Black_background2.tStartRefresh)
    checks.addData('Black_background2.stopped', Black_background2.tStopRefresh)
    # check responses
    if calibration_done.keys in ['', [], None]:  # No response was made
        calibration_done.keys = None
    checks.addData('calibration_done.keys',calibration_done.keys)
    if calibration_done.keys != None:  # we had a response
        checks.addData('calibration_done.rt', calibration_done.rt)
    checks.addData('calibration_done.started', calibration_done.tStartRefresh)
    checks.addData('calibration_done.stopped', calibration_done.tStopRefresh)
    checks.addData('middle.started', middle.tStartRefresh)
    checks.addData('middle.stopped', middle.tStopRefresh)
    checks.addData('top_left.started', top_left.tStartRefresh)
    checks.addData('top_left.stopped', top_left.tStopRefresh)
    checks.addData('top_right.started', top_right.tStartRefresh)
    checks.addData('top_right.stopped', top_right.tStopRefresh)
    checks.addData('bottom_left.started', bottom_left.tStartRefresh)
    checks.addData('bottom_left.stopped', bottom_left.tStopRefresh)
    checks.addData('bottom_right.started', bottom_right.tStartRefresh)
    checks.addData('bottom_right.stopped', bottom_right.tStopRefresh)
    checks.addData('M_fill.started', M_fill.tStartRefresh)
    checks.addData('M_fill.stopped', M_fill.tStopRefresh)
    checks.addData('TL_fill.started', TL_fill.tStartRefresh)
    checks.addData('TL_fill.stopped', TL_fill.tStopRefresh)
    checks.addData('TR_fill.started', TR_fill.tStartRefresh)
    checks.addData('TR_fill.stopped', TR_fill.tStopRefresh)
    checks.addData('BR_fill.started', BR_fill.tStartRefresh)
    checks.addData('BR_fill.stopped', BR_fill.tStopRefresh)
    checks.addData('BL_fill.started', BL_fill.tStartRefresh)
    checks.addData('BL_fill.stopped', BL_fill.tStopRefresh)
    # the Routine "Calibration" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1.0 repeats of 'checks'


# ------Prepare to start Routine "inst_fam_3x3"-------
continueRoutine = True
# update component parameters for each repeat
resp_familiarisation.keys = []
resp_familiarisation.rt = []
_resp_familiarisation_allKeys = []
# keep track of which components have finished
inst_fam_3x3Components = [black_background3, VS_familiarisation_opening, resp_familiarisation]
for thisComponent in inst_fam_3x3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
inst_fam_3x3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "inst_fam_3x3"-------
while continueRoutine:
    # get current time
    t = inst_fam_3x3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=inst_fam_3x3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *black_background3* updates
    if black_background3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        black_background3.frameNStart = frameN  # exact frame index
        black_background3.tStart = t  # local t and not account for scr refresh
        black_background3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(black_background3, 'tStartRefresh')  # time at next scr refresh
        black_background3.setAutoDraw(True)
    
    # *VS_familiarisation_opening* updates
    if VS_familiarisation_opening.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        VS_familiarisation_opening.frameNStart = frameN  # exact frame index
        VS_familiarisation_opening.tStart = t  # local t and not account for scr refresh
        VS_familiarisation_opening.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(VS_familiarisation_opening, 'tStartRefresh')  # time at next scr refresh
        VS_familiarisation_opening.setAutoDraw(True)
    
    # *resp_familiarisation* updates
    waitOnFlip = False
    if resp_familiarisation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        resp_familiarisation.frameNStart = frameN  # exact frame index
        resp_familiarisation.tStart = t  # local t and not account for scr refresh
        resp_familiarisation.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(resp_familiarisation, 'tStartRefresh')  # time at next scr refresh
        resp_familiarisation.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(resp_familiarisation.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(resp_familiarisation.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if resp_familiarisation.status == STARTED and not waitOnFlip:
        theseKeys = resp_familiarisation.getKeys(keyList=['y', 'n', 'left', 'right', 'space', '1', '2', '3'], waitRelease=False)
        _resp_familiarisation_allKeys.extend(theseKeys)
        if len(_resp_familiarisation_allKeys):
            resp_familiarisation.keys = _resp_familiarisation_allKeys[-1].name  # just the last key pressed
            resp_familiarisation.rt = _resp_familiarisation_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in inst_fam_3x3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "inst_fam_3x3"-------
for thisComponent in inst_fam_3x3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('black_background3.started', black_background3.tStartRefresh)
thisExp.addData('black_background3.stopped', black_background3.tStopRefresh)
thisExp.addData('VS_familiarisation_opening.started', VS_familiarisation_opening.tStartRefresh)
thisExp.addData('VS_familiarisation_opening.stopped', VS_familiarisation_opening.tStopRefresh)
# check responses
if resp_familiarisation.keys in ['', [], None]:  # No response was made
    resp_familiarisation.keys = None
thisExp.addData('resp_familiarisation.keys',resp_familiarisation.keys)
if resp_familiarisation.keys != None:  # we had a response
    thisExp.addData('resp_familiarisation.rt', resp_familiarisation.rt)
thisExp.addData('resp_familiarisation.started', resp_familiarisation.tStartRefresh)
thisExp.addData('resp_familiarisation.stopped', resp_familiarisation.tStopRefresh)
thisExp.nextEntry()
# the Routine "inst_fam_3x3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
fam_3x3 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('fam_loop.xlsx'),
    seed=None, name='fam_3x3')
thisExp.addLoop(fam_3x3)  # add the loop to the experiment
thisFam_3x3 = fam_3x3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisFam_3x3.rgb)
if thisFam_3x3 != None:
    for paramName in thisFam_3x3:
        exec('{} = thisFam_3x3[paramName]'.format(paramName))

for thisFam_3x3 in fam_3x3:
    currentLoop = fam_3x3
    # abbreviate parameter names if possible (e.g. rgb = thisFam_3x3.rgb)
    if thisFam_3x3 != None:
        for paramName in thisFam_3x3:
            exec('{} = thisFam_3x3[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "familiarisation"-------
    continueRoutine = True
    # update component parameters for each repeat
    resp_fam.keys = []
    resp_fam.rt = []
    _resp_fam_allKeys = []
    figs_fam.setImage(Fam_3x3)
    # keep track of which components have finished
    familiarisationComponents = [resp_fam, figs_fam]
    for thisComponent in familiarisationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    familiarisationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "familiarisation"-------
    while continueRoutine:
        # get current time
        t = familiarisationClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=familiarisationClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *resp_fam* updates
        waitOnFlip = False
        if resp_fam.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            resp_fam.frameNStart = frameN  # exact frame index
            resp_fam.tStart = t  # local t and not account for scr refresh
            resp_fam.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(resp_fam, 'tStartRefresh')  # time at next scr refresh
            resp_fam.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(resp_fam.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(resp_fam.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if resp_fam.status == STARTED and not waitOnFlip:
            theseKeys = resp_fam.getKeys(keyList=['left', 'right', 'space', '1', '2', '3'], waitRelease=False)
            _resp_fam_allKeys.extend(theseKeys)
            if len(_resp_fam_allKeys):
                resp_fam.keys = _resp_fam_allKeys[-1].name  # just the last key pressed
                resp_fam.rt = _resp_fam_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *figs_fam* updates
        if figs_fam.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            figs_fam.frameNStart = frameN  # exact frame index
            figs_fam.tStart = t  # local t and not account for scr refresh
            figs_fam.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(figs_fam, 'tStartRefresh')  # time at next scr refresh
            figs_fam.setAutoDraw(True)
        if figs_fam.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > figs_fam.tStartRefresh + 30-frameTolerance:
                # keep track of stop time/frame for later
                figs_fam.tStop = t  # not accounting for scr refresh
                figs_fam.frameNStop = frameN  # exact frame index
                win.timeOnFlip(figs_fam, 'tStopRefresh')  # time at next scr refresh
                figs_fam.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in familiarisationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "familiarisation"-------
    for thisComponent in familiarisationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if resp_fam.keys in ['', [], None]:  # No response was made
        resp_fam.keys = None
    fam_3x3.addData('resp_fam.keys',resp_fam.keys)
    if resp_fam.keys != None:  # we had a response
        fam_3x3.addData('resp_fam.rt', resp_fam.rt)
    fam_3x3.addData('resp_fam.started', resp_fam.tStartRefresh)
    fam_3x3.addData('resp_fam.stopped', resp_fam.tStopRefresh)
    fam_3x3.addData('figs_fam.started', figs_fam.tStartRefresh)
    fam_3x3.addData('figs_fam.stopped', figs_fam.tStopRefresh)
    # the Routine "familiarisation" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "blank"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    blankComponents = [waiting_screen]
    for thisComponent in blankComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    blankClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "blank"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blankClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=blankClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *waiting_screen* updates
        if waiting_screen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            waiting_screen.frameNStart = frameN  # exact frame index
            waiting_screen.tStart = t  # local t and not account for scr refresh
            waiting_screen.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(waiting_screen, 'tStartRefresh')  # time at next scr refresh
            waiting_screen.setAutoDraw(True)
        if waiting_screen.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > waiting_screen.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                waiting_screen.tStop = t  # not accounting for scr refresh
                waiting_screen.frameNStop = frameN  # exact frame index
                win.timeOnFlip(waiting_screen, 'tStopRefresh')  # time at next scr refresh
                waiting_screen.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blankComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "blank"-------
    for thisComponent in blankComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    fam_3x3.addData('waiting_screen.started', waiting_screen.tStartRefresh)
    fam_3x3.addData('waiting_screen.stopped', waiting_screen.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'fam_3x3'

# get names of stimulus parameters
if fam_3x3.trialList in ([], [None], None):
    params = []
else:
    params = fam_3x3.trialList[0].keys()
# save data for this loop
fam_3x3.saveAsExcel(filename + '.xlsx', sheetName='fam_3x3',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "instr_3x3"-------
continueRoutine = True
# update component parameters for each repeat
VS_instruction_done.keys = []
VS_instruction_done.rt = []
_VS_instruction_done_allKeys = []
# keep track of which components have finished
instr_3x3Components = [black_background4, VS_instruction_done, instr_test_start]
for thisComponent in instr_3x3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instr_3x3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instr_3x3"-------
while continueRoutine:
    # get current time
    t = instr_3x3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instr_3x3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *black_background4* updates
    if black_background4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        black_background4.frameNStart = frameN  # exact frame index
        black_background4.tStart = t  # local t and not account for scr refresh
        black_background4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(black_background4, 'tStartRefresh')  # time at next scr refresh
        black_background4.setAutoDraw(True)
    
    # *VS_instruction_done* updates
    waitOnFlip = False
    if VS_instruction_done.status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
        # keep track of start time/frame for later
        VS_instruction_done.frameNStart = frameN  # exact frame index
        VS_instruction_done.tStart = t  # local t and not account for scr refresh
        VS_instruction_done.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(VS_instruction_done, 'tStartRefresh')  # time at next scr refresh
        VS_instruction_done.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(VS_instruction_done.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(VS_instruction_done.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if VS_instruction_done.status == STARTED and not waitOnFlip:
        theseKeys = VS_instruction_done.getKeys(keyList=['y', 'n', 'left', 'right', 'space', '1', '2', '3'], waitRelease=False)
        _VS_instruction_done_allKeys.extend(theseKeys)
        if len(_VS_instruction_done_allKeys):
            VS_instruction_done.keys = _VS_instruction_done_allKeys[-1].name  # just the last key pressed
            VS_instruction_done.rt = _VS_instruction_done_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *instr_test_start* updates
    if instr_test_start.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_test_start.frameNStart = frameN  # exact frame index
        instr_test_start.tStart = t  # local t and not account for scr refresh
        instr_test_start.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_test_start, 'tStartRefresh')  # time at next scr refresh
        instr_test_start.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr_3x3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr_3x3"-------
for thisComponent in instr_3x3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('black_background4.started', black_background4.tStartRefresh)
thisExp.addData('black_background4.stopped', black_background4.tStopRefresh)
# check responses
if VS_instruction_done.keys in ['', [], None]:  # No response was made
    VS_instruction_done.keys = None
thisExp.addData('VS_instruction_done.keys',VS_instruction_done.keys)
if VS_instruction_done.keys != None:  # we had a response
    thisExp.addData('VS_instruction_done.rt', VS_instruction_done.rt)
thisExp.addData('VS_instruction_done.started', VS_instruction_done.tStartRefresh)
thisExp.addData('VS_instruction_done.stopped', VS_instruction_done.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('instr_test_start.started', instr_test_start.tStartRefresh)
thisExp.addData('instr_test_start.stopped', instr_test_start.tStopRefresh)
# the Routine "instr_3x3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_3x3 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('figs_loop.xlsx'),
    seed=None, name='trials_3x3')
thisExp.addLoop(trials_3x3)  # add the loop to the experiment
thisTrials_3x3 = trials_3x3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials_3x3.rgb)
if thisTrials_3x3 != None:
    for paramName in thisTrials_3x3:
        exec('{} = thisTrials_3x3[paramName]'.format(paramName))

for thisTrials_3x3 in trials_3x3:
    currentLoop = trials_3x3
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_3x3.rgb)
    if thisTrials_3x3 != None:
        for paramName in thisTrials_3x3:
            exec('{} = thisTrials_3x3[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "routine_3x3"-------
    continueRoutine = True
    # update component parameters for each repeat
    resp_3x3.keys = []
    resp_3x3.rt = []
    _resp_3x3_allKeys = []
    figs_3x3.setImage(Figs_3x3)
    # keep track of which components have finished
    routine_3x3Components = [resp_3x3, figs_3x3]
    for thisComponent in routine_3x3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    routine_3x3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "routine_3x3"-------
    while continueRoutine:
        # get current time
        t = routine_3x3Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routine_3x3Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *resp_3x3* updates
        waitOnFlip = False
        if resp_3x3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            resp_3x3.frameNStart = frameN  # exact frame index
            resp_3x3.tStart = t  # local t and not account for scr refresh
            resp_3x3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(resp_3x3, 'tStartRefresh')  # time at next scr refresh
            resp_3x3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(resp_3x3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(resp_3x3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if resp_3x3.status == STARTED and not waitOnFlip:
            theseKeys = resp_3x3.getKeys(keyList=['left', 'right', 'space', '1', '2', '3'], waitRelease=False)
            _resp_3x3_allKeys.extend(theseKeys)
            if len(_resp_3x3_allKeys):
                resp_3x3.keys = _resp_3x3_allKeys[-1].name  # just the last key pressed
                resp_3x3.rt = _resp_3x3_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *figs_3x3* updates
        if figs_3x3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            figs_3x3.frameNStart = frameN  # exact frame index
            figs_3x3.tStart = t  # local t and not account for scr refresh
            figs_3x3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(figs_3x3, 'tStartRefresh')  # time at next scr refresh
            figs_3x3.setAutoDraw(True)
        if figs_3x3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > figs_3x3.tStartRefresh + 30-frameTolerance:
                # keep track of stop time/frame for later
                figs_3x3.tStop = t  # not accounting for scr refresh
                figs_3x3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(figs_3x3, 'tStopRefresh')  # time at next scr refresh
                figs_3x3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in routine_3x3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "routine_3x3"-------
    for thisComponent in routine_3x3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if resp_3x3.keys in ['', [], None]:  # No response was made
        resp_3x3.keys = None
    trials_3x3.addData('resp_3x3.keys',resp_3x3.keys)
    if resp_3x3.keys != None:  # we had a response
        trials_3x3.addData('resp_3x3.rt', resp_3x3.rt)
    trials_3x3.addData('resp_3x3.started', resp_3x3.tStartRefresh)
    trials_3x3.addData('resp_3x3.stopped', resp_3x3.tStopRefresh)
    trials_3x3.addData('figs_3x3.started', figs_3x3.tStartRefresh)
    trials_3x3.addData('figs_3x3.stopped', figs_3x3.tStopRefresh)
    # the Routine "routine_3x3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "blank"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    blankComponents = [waiting_screen]
    for thisComponent in blankComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    blankClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "blank"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blankClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=blankClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *waiting_screen* updates
        if waiting_screen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            waiting_screen.frameNStart = frameN  # exact frame index
            waiting_screen.tStart = t  # local t and not account for scr refresh
            waiting_screen.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(waiting_screen, 'tStartRefresh')  # time at next scr refresh
            waiting_screen.setAutoDraw(True)
        if waiting_screen.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > waiting_screen.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                waiting_screen.tStop = t  # not accounting for scr refresh
                waiting_screen.frameNStop = frameN  # exact frame index
                win.timeOnFlip(waiting_screen, 'tStopRefresh')  # time at next scr refresh
                waiting_screen.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blankComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "blank"-------
    for thisComponent in blankComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_3x3.addData('waiting_screen.started', waiting_screen.tStartRefresh)
    trials_3x3.addData('waiting_screen.stopped', waiting_screen.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_3x3'

# get names of stimulus parameters
if trials_3x3.trialList in ([], [None], None):
    params = []
else:
    params = trials_3x3.trialList[0].keys()
# save data for this loop
trials_3x3.saveAsExcel(filename + '.xlsx', sheetName='trials_3x3',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "break_3"-------
continueRoutine = True
# update component parameters for each repeat
break_over.keys = []
break_over.rt = []
_break_over_allKeys = []
# keep track of which components have finished
break_3Components = [black_background5, break1, break_over]
for thisComponent in break_3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
break_3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "break_3"-------
while continueRoutine:
    # get current time
    t = break_3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=break_3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *black_background5* updates
    if black_background5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        black_background5.frameNStart = frameN  # exact frame index
        black_background5.tStart = t  # local t and not account for scr refresh
        black_background5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(black_background5, 'tStartRefresh')  # time at next scr refresh
        black_background5.setAutoDraw(True)
    
    # *break1* updates
    if break1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        break1.frameNStart = frameN  # exact frame index
        break1.tStart = t  # local t and not account for scr refresh
        break1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(break1, 'tStartRefresh')  # time at next scr refresh
        break1.setAutoDraw(True)
    
    # *break_over* updates
    waitOnFlip = False
    if break_over.status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
        # keep track of start time/frame for later
        break_over.frameNStart = frameN  # exact frame index
        break_over.tStart = t  # local t and not account for scr refresh
        break_over.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(break_over, 'tStartRefresh')  # time at next scr refresh
        break_over.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(break_over.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(break_over.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if break_over.status == STARTED and not waitOnFlip:
        theseKeys = break_over.getKeys(keyList=['y', 'n', 'left', 'right', 'space', '1', '2', '3'], waitRelease=False)
        _break_over_allKeys.extend(theseKeys)
        if len(_break_over_allKeys):
            break_over.keys = _break_over_allKeys[-1].name  # just the last key pressed
            break_over.rt = _break_over_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in break_3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "break_3"-------
for thisComponent in break_3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('black_background5.started', black_background5.tStartRefresh)
thisExp.addData('black_background5.stopped', black_background5.tStopRefresh)
thisExp.addData('break1.started', break1.tStartRefresh)
thisExp.addData('break1.stopped', break1.tStopRefresh)
# check responses
if break_over.keys in ['', [], None]:  # No response was made
    break_over.keys = None
thisExp.addData('break_over.keys',break_over.keys)
if break_over.keys != None:  # we had a response
    thisExp.addData('break_over.rt', break_over.rt)
thisExp.addData('break_over.started', break_over.tStartRefresh)
thisExp.addData('break_over.stopped', break_over.tStopRefresh)
thisExp.nextEntry()
# the Routine "break_3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_8x8 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('figs_loop.xlsx'),
    seed=None, name='trials_8x8')
thisExp.addLoop(trials_8x8)  # add the loop to the experiment
thisTrials_8x8 = trials_8x8.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials_8x8.rgb)
if thisTrials_8x8 != None:
    for paramName in thisTrials_8x8:
        exec('{} = thisTrials_8x8[paramName]'.format(paramName))

for thisTrials_8x8 in trials_8x8:
    currentLoop = trials_8x8
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_8x8.rgb)
    if thisTrials_8x8 != None:
        for paramName in thisTrials_8x8:
            exec('{} = thisTrials_8x8[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "routine_8x8"-------
    continueRoutine = True
    # update component parameters for each repeat
    resp_8x8.keys = []
    resp_8x8.rt = []
    _resp_8x8_allKeys = []
    figs_8x8.setImage(Figs_8x8)
    # keep track of which components have finished
    routine_8x8Components = [resp_8x8, figs_8x8]
    for thisComponent in routine_8x8Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    routine_8x8Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "routine_8x8"-------
    while continueRoutine:
        # get current time
        t = routine_8x8Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routine_8x8Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *resp_8x8* updates
        waitOnFlip = False
        if resp_8x8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            resp_8x8.frameNStart = frameN  # exact frame index
            resp_8x8.tStart = t  # local t and not account for scr refresh
            resp_8x8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(resp_8x8, 'tStartRefresh')  # time at next scr refresh
            resp_8x8.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(resp_8x8.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(resp_8x8.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if resp_8x8.status == STARTED and not waitOnFlip:
            theseKeys = resp_8x8.getKeys(keyList=['left', 'right', 'space', '1', '2', '3'], waitRelease=False)
            _resp_8x8_allKeys.extend(theseKeys)
            if len(_resp_8x8_allKeys):
                resp_8x8.keys = _resp_8x8_allKeys[-1].name  # just the last key pressed
                resp_8x8.rt = _resp_8x8_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *figs_8x8* updates
        if figs_8x8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            figs_8x8.frameNStart = frameN  # exact frame index
            figs_8x8.tStart = t  # local t and not account for scr refresh
            figs_8x8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(figs_8x8, 'tStartRefresh')  # time at next scr refresh
            figs_8x8.setAutoDraw(True)
        if figs_8x8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > figs_8x8.tStartRefresh + 30-frameTolerance:
                # keep track of stop time/frame for later
                figs_8x8.tStop = t  # not accounting for scr refresh
                figs_8x8.frameNStop = frameN  # exact frame index
                win.timeOnFlip(figs_8x8, 'tStopRefresh')  # time at next scr refresh
                figs_8x8.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in routine_8x8Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "routine_8x8"-------
    for thisComponent in routine_8x8Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if resp_8x8.keys in ['', [], None]:  # No response was made
        resp_8x8.keys = None
    trials_8x8.addData('resp_8x8.keys',resp_8x8.keys)
    if resp_8x8.keys != None:  # we had a response
        trials_8x8.addData('resp_8x8.rt', resp_8x8.rt)
    trials_8x8.addData('resp_8x8.started', resp_8x8.tStartRefresh)
    trials_8x8.addData('resp_8x8.stopped', resp_8x8.tStopRefresh)
    trials_8x8.addData('figs_8x8.started', figs_8x8.tStartRefresh)
    trials_8x8.addData('figs_8x8.stopped', figs_8x8.tStopRefresh)
    # the Routine "routine_8x8" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "blank"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    blankComponents = [waiting_screen]
    for thisComponent in blankComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    blankClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "blank"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blankClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=blankClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *waiting_screen* updates
        if waiting_screen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            waiting_screen.frameNStart = frameN  # exact frame index
            waiting_screen.tStart = t  # local t and not account for scr refresh
            waiting_screen.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(waiting_screen, 'tStartRefresh')  # time at next scr refresh
            waiting_screen.setAutoDraw(True)
        if waiting_screen.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > waiting_screen.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                waiting_screen.tStop = t  # not accounting for scr refresh
                waiting_screen.frameNStop = frameN  # exact frame index
                win.timeOnFlip(waiting_screen, 'tStopRefresh')  # time at next scr refresh
                waiting_screen.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blankComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "blank"-------
    for thisComponent in blankComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_8x8.addData('waiting_screen.started', waiting_screen.tStartRefresh)
    trials_8x8.addData('waiting_screen.stopped', waiting_screen.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_8x8'

# get names of stimulus parameters
if trials_8x8.trialList in ([], [None], None):
    params = []
else:
    params = trials_8x8.trialList[0].keys()
# save data for this loop
trials_8x8.saveAsExcel(filename + '.xlsx', sheetName='trials_8x8',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "break_3"-------
continueRoutine = True
# update component parameters for each repeat
break_over.keys = []
break_over.rt = []
_break_over_allKeys = []
# keep track of which components have finished
break_3Components = [black_background5, break1, break_over]
for thisComponent in break_3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
break_3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "break_3"-------
while continueRoutine:
    # get current time
    t = break_3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=break_3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *black_background5* updates
    if black_background5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        black_background5.frameNStart = frameN  # exact frame index
        black_background5.tStart = t  # local t and not account for scr refresh
        black_background5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(black_background5, 'tStartRefresh')  # time at next scr refresh
        black_background5.setAutoDraw(True)
    
    # *break1* updates
    if break1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        break1.frameNStart = frameN  # exact frame index
        break1.tStart = t  # local t and not account for scr refresh
        break1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(break1, 'tStartRefresh')  # time at next scr refresh
        break1.setAutoDraw(True)
    
    # *break_over* updates
    waitOnFlip = False
    if break_over.status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
        # keep track of start time/frame for later
        break_over.frameNStart = frameN  # exact frame index
        break_over.tStart = t  # local t and not account for scr refresh
        break_over.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(break_over, 'tStartRefresh')  # time at next scr refresh
        break_over.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(break_over.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(break_over.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if break_over.status == STARTED and not waitOnFlip:
        theseKeys = break_over.getKeys(keyList=['y', 'n', 'left', 'right', 'space', '1', '2', '3'], waitRelease=False)
        _break_over_allKeys.extend(theseKeys)
        if len(_break_over_allKeys):
            break_over.keys = _break_over_allKeys[-1].name  # just the last key pressed
            break_over.rt = _break_over_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in break_3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "break_3"-------
for thisComponent in break_3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('black_background5.started', black_background5.tStartRefresh)
thisExp.addData('black_background5.stopped', black_background5.tStopRefresh)
thisExp.addData('break1.started', break1.tStartRefresh)
thisExp.addData('break1.stopped', break1.tStopRefresh)
# check responses
if break_over.keys in ['', [], None]:  # No response was made
    break_over.keys = None
thisExp.addData('break_over.keys',break_over.keys)
if break_over.keys != None:  # we had a response
    thisExp.addData('break_over.rt', break_over.rt)
thisExp.addData('break_over.started', break_over.tStartRefresh)
thisExp.addData('break_over.stopped', break_over.tStopRefresh)
thisExp.nextEntry()
# the Routine "break_3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_15x15 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('figs_loop.xlsx'),
    seed=None, name='trials_15x15')
thisExp.addLoop(trials_15x15)  # add the loop to the experiment
thisTrials_15x15 = trials_15x15.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials_15x15.rgb)
if thisTrials_15x15 != None:
    for paramName in thisTrials_15x15:
        exec('{} = thisTrials_15x15[paramName]'.format(paramName))

for thisTrials_15x15 in trials_15x15:
    currentLoop = trials_15x15
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_15x15.rgb)
    if thisTrials_15x15 != None:
        for paramName in thisTrials_15x15:
            exec('{} = thisTrials_15x15[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "routine_15x15"-------
    continueRoutine = True
    # update component parameters for each repeat
    resp_15x15.keys = []
    resp_15x15.rt = []
    _resp_15x15_allKeys = []
    figs_15x15.setImage(Figs_15x15)
    # keep track of which components have finished
    routine_15x15Components = [resp_15x15, figs_15x15]
    for thisComponent in routine_15x15Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    routine_15x15Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "routine_15x15"-------
    while continueRoutine:
        # get current time
        t = routine_15x15Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routine_15x15Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *resp_15x15* updates
        waitOnFlip = False
        if resp_15x15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            resp_15x15.frameNStart = frameN  # exact frame index
            resp_15x15.tStart = t  # local t and not account for scr refresh
            resp_15x15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(resp_15x15, 'tStartRefresh')  # time at next scr refresh
            resp_15x15.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(resp_15x15.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(resp_15x15.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if resp_15x15.status == STARTED and not waitOnFlip:
            theseKeys = resp_15x15.getKeys(keyList=['left', 'right', 'space', '1', '2', '3'], waitRelease=False)
            _resp_15x15_allKeys.extend(theseKeys)
            if len(_resp_15x15_allKeys):
                resp_15x15.keys = _resp_15x15_allKeys[-1].name  # just the last key pressed
                resp_15x15.rt = _resp_15x15_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *figs_15x15* updates
        if figs_15x15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            figs_15x15.frameNStart = frameN  # exact frame index
            figs_15x15.tStart = t  # local t and not account for scr refresh
            figs_15x15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(figs_15x15, 'tStartRefresh')  # time at next scr refresh
            figs_15x15.setAutoDraw(True)
        if figs_15x15.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > figs_15x15.tStartRefresh + 30-frameTolerance:
                # keep track of stop time/frame for later
                figs_15x15.tStop = t  # not accounting for scr refresh
                figs_15x15.frameNStop = frameN  # exact frame index
                win.timeOnFlip(figs_15x15, 'tStopRefresh')  # time at next scr refresh
                figs_15x15.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in routine_15x15Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "routine_15x15"-------
    for thisComponent in routine_15x15Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if resp_15x15.keys in ['', [], None]:  # No response was made
        resp_15x15.keys = None
    trials_15x15.addData('resp_15x15.keys',resp_15x15.keys)
    if resp_15x15.keys != None:  # we had a response
        trials_15x15.addData('resp_15x15.rt', resp_15x15.rt)
    trials_15x15.addData('resp_15x15.started', resp_15x15.tStartRefresh)
    trials_15x15.addData('resp_15x15.stopped', resp_15x15.tStopRefresh)
    trials_15x15.addData('figs_15x15.started', figs_15x15.tStartRefresh)
    trials_15x15.addData('figs_15x15.stopped', figs_15x15.tStopRefresh)
    # the Routine "routine_15x15" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "blank"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    blankComponents = [waiting_screen]
    for thisComponent in blankComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    blankClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "blank"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blankClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=blankClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *waiting_screen* updates
        if waiting_screen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            waiting_screen.frameNStart = frameN  # exact frame index
            waiting_screen.tStart = t  # local t and not account for scr refresh
            waiting_screen.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(waiting_screen, 'tStartRefresh')  # time at next scr refresh
            waiting_screen.setAutoDraw(True)
        if waiting_screen.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > waiting_screen.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                waiting_screen.tStop = t  # not accounting for scr refresh
                waiting_screen.frameNStop = frameN  # exact frame index
                win.timeOnFlip(waiting_screen, 'tStopRefresh')  # time at next scr refresh
                waiting_screen.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blankComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "blank"-------
    for thisComponent in blankComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_15x15.addData('waiting_screen.started', waiting_screen.tStartRefresh)
    trials_15x15.addData('waiting_screen.stopped', waiting_screen.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_15x15'

# get names of stimulus parameters
if trials_15x15.trialList in ([], [None], None):
    params = []
else:
    params = trials_15x15.trialList[0].keys()
# save data for this loop
trials_15x15.saveAsExcel(filename + '.xlsx', sheetName='trials_15x15',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "inst_fix"-------
continueRoutine = True
# update component parameters for each repeat
FS_instruction_done.keys = []
FS_instruction_done.rt = []
_FS_instruction_done_allKeys = []
# keep track of which components have finished
inst_fixComponents = [black_background6, FS_instruction_done, Fixation_stability_instruction]
for thisComponent in inst_fixComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
inst_fixClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "inst_fix"-------
while continueRoutine:
    # get current time
    t = inst_fixClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=inst_fixClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *black_background6* updates
    if black_background6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        black_background6.frameNStart = frameN  # exact frame index
        black_background6.tStart = t  # local t and not account for scr refresh
        black_background6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(black_background6, 'tStartRefresh')  # time at next scr refresh
        black_background6.setAutoDraw(True)
    
    # *FS_instruction_done* updates
    waitOnFlip = False
    if FS_instruction_done.status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
        # keep track of start time/frame for later
        FS_instruction_done.frameNStart = frameN  # exact frame index
        FS_instruction_done.tStart = t  # local t and not account for scr refresh
        FS_instruction_done.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(FS_instruction_done, 'tStartRefresh')  # time at next scr refresh
        FS_instruction_done.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(FS_instruction_done.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(FS_instruction_done.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if FS_instruction_done.status == STARTED and not waitOnFlip:
        theseKeys = FS_instruction_done.getKeys(keyList=['y', 'n', 'left', 'right', 'space'], waitRelease=False)
        _FS_instruction_done_allKeys.extend(theseKeys)
        if len(_FS_instruction_done_allKeys):
            FS_instruction_done.keys = _FS_instruction_done_allKeys[-1].name  # just the last key pressed
            FS_instruction_done.rt = _FS_instruction_done_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *Fixation_stability_instruction* updates
    if Fixation_stability_instruction.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Fixation_stability_instruction.frameNStart = frameN  # exact frame index
        Fixation_stability_instruction.tStart = t  # local t and not account for scr refresh
        Fixation_stability_instruction.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Fixation_stability_instruction, 'tStartRefresh')  # time at next scr refresh
        Fixation_stability_instruction.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in inst_fixComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "inst_fix"-------
for thisComponent in inst_fixComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('black_background6.started', black_background6.tStartRefresh)
thisExp.addData('black_background6.stopped', black_background6.tStopRefresh)
# check responses
if FS_instruction_done.keys in ['', [], None]:  # No response was made
    FS_instruction_done.keys = None
thisExp.addData('FS_instruction_done.keys',FS_instruction_done.keys)
if FS_instruction_done.keys != None:  # we had a response
    thisExp.addData('FS_instruction_done.rt', FS_instruction_done.rt)
thisExp.addData('FS_instruction_done.started', FS_instruction_done.tStartRefresh)
thisExp.addData('FS_instruction_done.stopped', FS_instruction_done.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('Fixation_stability_instruction.started', Fixation_stability_instruction.tStartRefresh)
thisExp.addData('Fixation_stability_instruction.stopped', Fixation_stability_instruction.tStopRefresh)
# the Routine "inst_fix" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "fix_stab"-------
continueRoutine = True
routineTimer.add(30.000000)
# update component parameters for each repeat
interrupt_FS.keys = []
interrupt_FS.rt = []
_interrupt_FS_allKeys = []
# keep track of which components have finished
fix_stabComponents = [black_background7, interrupt_FS, horizontal, vertical, inner_line_horizontal, inner_line_vertical]
for thisComponent in fix_stabComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
fix_stabClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "fix_stab"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = fix_stabClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=fix_stabClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *black_background7* updates
    if black_background7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        black_background7.frameNStart = frameN  # exact frame index
        black_background7.tStart = t  # local t and not account for scr refresh
        black_background7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(black_background7, 'tStartRefresh')  # time at next scr refresh
        black_background7.setAutoDraw(True)
    if black_background7.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > black_background7.tStartRefresh + 30-frameTolerance:
            # keep track of stop time/frame for later
            black_background7.tStop = t  # not accounting for scr refresh
            black_background7.frameNStop = frameN  # exact frame index
            win.timeOnFlip(black_background7, 'tStopRefresh')  # time at next scr refresh
            black_background7.setAutoDraw(False)
    
    # *interrupt_FS* updates
    waitOnFlip = False
    if interrupt_FS.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        interrupt_FS.frameNStart = frameN  # exact frame index
        interrupt_FS.tStart = t  # local t and not account for scr refresh
        interrupt_FS.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(interrupt_FS, 'tStartRefresh')  # time at next scr refresh
        interrupt_FS.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(interrupt_FS.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(interrupt_FS.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if interrupt_FS.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > interrupt_FS.tStartRefresh + 30-frameTolerance:
            # keep track of stop time/frame for later
            interrupt_FS.tStop = t  # not accounting for scr refresh
            interrupt_FS.frameNStop = frameN  # exact frame index
            win.timeOnFlip(interrupt_FS, 'tStopRefresh')  # time at next scr refresh
            interrupt_FS.status = FINISHED
    if interrupt_FS.status == STARTED and not waitOnFlip:
        theseKeys = interrupt_FS.getKeys(keyList=['space'], waitRelease=False)
        _interrupt_FS_allKeys.extend(theseKeys)
        if len(_interrupt_FS_allKeys):
            interrupt_FS.keys = _interrupt_FS_allKeys[-1].name  # just the last key pressed
            interrupt_FS.rt = _interrupt_FS_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *horizontal* updates
    if horizontal.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        horizontal.frameNStart = frameN  # exact frame index
        horizontal.tStart = t  # local t and not account for scr refresh
        horizontal.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(horizontal, 'tStartRefresh')  # time at next scr refresh
        horizontal.setAutoDraw(True)
    if horizontal.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > horizontal.tStartRefresh + 30-frameTolerance:
            # keep track of stop time/frame for later
            horizontal.tStop = t  # not accounting for scr refresh
            horizontal.frameNStop = frameN  # exact frame index
            win.timeOnFlip(horizontal, 'tStopRefresh')  # time at next scr refresh
            horizontal.setAutoDraw(False)
    
    # *vertical* updates
    if vertical.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        vertical.frameNStart = frameN  # exact frame index
        vertical.tStart = t  # local t and not account for scr refresh
        vertical.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(vertical, 'tStartRefresh')  # time at next scr refresh
        vertical.setAutoDraw(True)
    if vertical.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > vertical.tStartRefresh + 30-frameTolerance:
            # keep track of stop time/frame for later
            vertical.tStop = t  # not accounting for scr refresh
            vertical.frameNStop = frameN  # exact frame index
            win.timeOnFlip(vertical, 'tStopRefresh')  # time at next scr refresh
            vertical.setAutoDraw(False)
    
    # *inner_line_horizontal* updates
    if inner_line_horizontal.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        inner_line_horizontal.frameNStart = frameN  # exact frame index
        inner_line_horizontal.tStart = t  # local t and not account for scr refresh
        inner_line_horizontal.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(inner_line_horizontal, 'tStartRefresh')  # time at next scr refresh
        inner_line_horizontal.setAutoDraw(True)
    if inner_line_horizontal.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > inner_line_horizontal.tStartRefresh + 30-frameTolerance:
            # keep track of stop time/frame for later
            inner_line_horizontal.tStop = t  # not accounting for scr refresh
            inner_line_horizontal.frameNStop = frameN  # exact frame index
            win.timeOnFlip(inner_line_horizontal, 'tStopRefresh')  # time at next scr refresh
            inner_line_horizontal.setAutoDraw(False)
    
    # *inner_line_vertical* updates
    if inner_line_vertical.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        inner_line_vertical.frameNStart = frameN  # exact frame index
        inner_line_vertical.tStart = t  # local t and not account for scr refresh
        inner_line_vertical.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(inner_line_vertical, 'tStartRefresh')  # time at next scr refresh
        inner_line_vertical.setAutoDraw(True)
    if inner_line_vertical.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > inner_line_vertical.tStartRefresh + 30-frameTolerance:
            # keep track of stop time/frame for later
            inner_line_vertical.tStop = t  # not accounting for scr refresh
            inner_line_vertical.frameNStop = frameN  # exact frame index
            win.timeOnFlip(inner_line_vertical, 'tStopRefresh')  # time at next scr refresh
            inner_line_vertical.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in fix_stabComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "fix_stab"-------
for thisComponent in fix_stabComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('black_background7.started', black_background7.tStartRefresh)
thisExp.addData('black_background7.stopped', black_background7.tStopRefresh)
# check responses
if interrupt_FS.keys in ['', [], None]:  # No response was made
    interrupt_FS.keys = None
thisExp.addData('interrupt_FS.keys',interrupt_FS.keys)
if interrupt_FS.keys != None:  # we had a response
    thisExp.addData('interrupt_FS.rt', interrupt_FS.rt)
thisExp.addData('interrupt_FS.started', interrupt_FS.tStartRefresh)
thisExp.addData('interrupt_FS.stopped', interrupt_FS.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('horizontal.started', horizontal.tStartRefresh)
thisExp.addData('horizontal.stopped', horizontal.tStopRefresh)
thisExp.addData('vertical.started', vertical.tStartRefresh)
thisExp.addData('vertical.stopped', vertical.tStopRefresh)
thisExp.addData('inner_line_horizontal.started', inner_line_horizontal.tStartRefresh)
thisExp.addData('inner_line_horizontal.stopped', inner_line_horizontal.tStopRefresh)
thisExp.addData('inner_line_vertical.started', inner_line_vertical.tStartRefresh)
thisExp.addData('inner_line_vertical.stopped', inner_line_vertical.tStopRefresh)

# ------Prepare to start Routine "instr_saccades"-------
continueRoutine = True
# update component parameters for each repeat
SAC_instructions_done.keys = []
SAC_instructions_done.rt = []
_SAC_instructions_done_allKeys = []
# keep track of which components have finished
instr_saccadesComponents = [black_background8, saccade_test_instructions, SAC_instructions_done]
for thisComponent in instr_saccadesComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instr_saccadesClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instr_saccades"-------
while continueRoutine:
    # get current time
    t = instr_saccadesClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instr_saccadesClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *black_background8* updates
    if black_background8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        black_background8.frameNStart = frameN  # exact frame index
        black_background8.tStart = t  # local t and not account for scr refresh
        black_background8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(black_background8, 'tStartRefresh')  # time at next scr refresh
        black_background8.setAutoDraw(True)
    
    # *saccade_test_instructions* updates
    if saccade_test_instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        saccade_test_instructions.frameNStart = frameN  # exact frame index
        saccade_test_instructions.tStart = t  # local t and not account for scr refresh
        saccade_test_instructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(saccade_test_instructions, 'tStartRefresh')  # time at next scr refresh
        saccade_test_instructions.setAutoDraw(True)
    
    # *SAC_instructions_done* updates
    waitOnFlip = False
    if SAC_instructions_done.status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
        # keep track of start time/frame for later
        SAC_instructions_done.frameNStart = frameN  # exact frame index
        SAC_instructions_done.tStart = t  # local t and not account for scr refresh
        SAC_instructions_done.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(SAC_instructions_done, 'tStartRefresh')  # time at next scr refresh
        SAC_instructions_done.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(SAC_instructions_done.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(SAC_instructions_done.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if SAC_instructions_done.status == STARTED and not waitOnFlip:
        theseKeys = SAC_instructions_done.getKeys(keyList=['y', 'n', 'left', 'right', 'space', '1', '2', '3'], waitRelease=False)
        _SAC_instructions_done_allKeys.extend(theseKeys)
        if len(_SAC_instructions_done_allKeys):
            SAC_instructions_done.keys = _SAC_instructions_done_allKeys[-1].name  # just the last key pressed
            SAC_instructions_done.rt = _SAC_instructions_done_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr_saccadesComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr_saccades"-------
for thisComponent in instr_saccadesComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('black_background8.started', black_background8.tStartRefresh)
thisExp.addData('black_background8.stopped', black_background8.tStopRefresh)
thisExp.addData('saccade_test_instructions.started', saccade_test_instructions.tStartRefresh)
thisExp.addData('saccade_test_instructions.stopped', saccade_test_instructions.tStopRefresh)
# check responses
if SAC_instructions_done.keys in ['', [], None]:  # No response was made
    SAC_instructions_done.keys = None
thisExp.addData('SAC_instructions_done.keys',SAC_instructions_done.keys)
if SAC_instructions_done.keys != None:  # we had a response
    thisExp.addData('SAC_instructions_done.rt', SAC_instructions_done.rt)
thisExp.addData('SAC_instructions_done.started', SAC_instructions_done.tStartRefresh)
thisExp.addData('SAC_instructions_done.stopped', SAC_instructions_done.tStopRefresh)
thisExp.nextEntry()
# the Routine "instr_saccades" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
SAC_trials = data.TrialHandler(nReps=2.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('saccades_loop.xlsx'),
    seed=None, name='SAC_trials')
thisExp.addLoop(SAC_trials)  # add the loop to the experiment
thisSAC_trial = SAC_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisSAC_trial.rgb)
if thisSAC_trial != None:
    for paramName in thisSAC_trial:
        exec('{} = thisSAC_trial[paramName]'.format(paramName))

for thisSAC_trial in SAC_trials:
    currentLoop = SAC_trials
    # abbreviate parameter names if possible (e.g. rgb = thisSAC_trial.rgb)
    if thisSAC_trial != None:
        for paramName in thisSAC_trial:
            exec('{} = thisSAC_trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial_saccades"-------
    continueRoutine = True
    routineTimer.add(1.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    trial_saccadesComponents = [black_background9, SAC_fix_target]
    for thisComponent in trial_saccadesComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trial_saccadesClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial_saccades"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trial_saccadesClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trial_saccadesClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *black_background9* updates
        if black_background9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            black_background9.frameNStart = frameN  # exact frame index
            black_background9.tStart = t  # local t and not account for scr refresh
            black_background9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(black_background9, 'tStartRefresh')  # time at next scr refresh
            black_background9.setAutoDraw(True)
        if black_background9.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > black_background9.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                black_background9.tStop = t  # not accounting for scr refresh
                black_background9.frameNStop = frameN  # exact frame index
                win.timeOnFlip(black_background9, 'tStopRefresh')  # time at next scr refresh
                black_background9.setAutoDraw(False)
        
        # *SAC_fix_target* updates
        if SAC_fix_target.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            SAC_fix_target.frameNStart = frameN  # exact frame index
            SAC_fix_target.tStart = t  # local t and not account for scr refresh
            SAC_fix_target.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(SAC_fix_target, 'tStartRefresh')  # time at next scr refresh
            SAC_fix_target.setAutoDraw(True)
        if SAC_fix_target.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > SAC_fix_target.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                SAC_fix_target.tStop = t  # not accounting for scr refresh
                SAC_fix_target.frameNStop = frameN  # exact frame index
                win.timeOnFlip(SAC_fix_target, 'tStopRefresh')  # time at next scr refresh
                SAC_fix_target.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial_saccadesComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial_saccades"-------
    for thisComponent in trial_saccadesComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    SAC_trials.addData('black_background9.started', black_background9.tStartRefresh)
    SAC_trials.addData('black_background9.stopped', black_background9.tStopRefresh)
    SAC_trials.addData('SAC_fix_target.started', SAC_fix_target.tStartRefresh)
    SAC_trials.addData('SAC_fix_target.stopped', SAC_fix_target.tStopRefresh)
    
    # ------Prepare to start Routine "saccades"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    N_6.setOpacity(opacity_N6)
    N_10.setOpacity(opacity_N10)
    E_6.setOpacity(opacity_E6)
    E_10.setOpacity(opacity_E10)
    S_6.setOpacity(opacity_S6)
    S_10.setOpacity(opacity_S10)
    W_6.setOpacity(opacity_W6)
    W_10.setOpacity(opacity_W10)
    NE_10.setOpacity(opacity_NE10)
    SE_10.setOpacity(opacity_SE10)
    SW_10.setOpacity(opacity_SW10)
    NW_10.setOpacity(opacity_NW10)
    # keep track of which components have finished
    saccadesComponents = [black_background10, N_6, N_10, E_6, E_10, S_6, S_10, W_6, W_10, NE_10, SE_10, SW_10, NW_10]
    for thisComponent in saccadesComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    saccadesClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "saccades"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = saccadesClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=saccadesClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *black_background10* updates
        if black_background10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            black_background10.frameNStart = frameN  # exact frame index
            black_background10.tStart = t  # local t and not account for scr refresh
            black_background10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(black_background10, 'tStartRefresh')  # time at next scr refresh
            black_background10.setAutoDraw(True)
        if black_background10.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > black_background10.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                black_background10.tStop = t  # not accounting for scr refresh
                black_background10.frameNStop = frameN  # exact frame index
                win.timeOnFlip(black_background10, 'tStopRefresh')  # time at next scr refresh
                black_background10.setAutoDraw(False)
        
        # *N_6* updates
        if N_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            N_6.frameNStart = frameN  # exact frame index
            N_6.tStart = t  # local t and not account for scr refresh
            N_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(N_6, 'tStartRefresh')  # time at next scr refresh
            N_6.setAutoDraw(True)
        if N_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > N_6.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                N_6.tStop = t  # not accounting for scr refresh
                N_6.frameNStop = frameN  # exact frame index
                win.timeOnFlip(N_6, 'tStopRefresh')  # time at next scr refresh
                N_6.setAutoDraw(False)
        
        # *N_10* updates
        if N_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            N_10.frameNStart = frameN  # exact frame index
            N_10.tStart = t  # local t and not account for scr refresh
            N_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(N_10, 'tStartRefresh')  # time at next scr refresh
            N_10.setAutoDraw(True)
        if N_10.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > N_10.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                N_10.tStop = t  # not accounting for scr refresh
                N_10.frameNStop = frameN  # exact frame index
                win.timeOnFlip(N_10, 'tStopRefresh')  # time at next scr refresh
                N_10.setAutoDraw(False)
        
        # *E_6* updates
        if E_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            E_6.frameNStart = frameN  # exact frame index
            E_6.tStart = t  # local t and not account for scr refresh
            E_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(E_6, 'tStartRefresh')  # time at next scr refresh
            E_6.setAutoDraw(True)
        if E_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > E_6.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                E_6.tStop = t  # not accounting for scr refresh
                E_6.frameNStop = frameN  # exact frame index
                win.timeOnFlip(E_6, 'tStopRefresh')  # time at next scr refresh
                E_6.setAutoDraw(False)
        
        # *E_10* updates
        if E_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            E_10.frameNStart = frameN  # exact frame index
            E_10.tStart = t  # local t and not account for scr refresh
            E_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(E_10, 'tStartRefresh')  # time at next scr refresh
            E_10.setAutoDraw(True)
        if E_10.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > E_10.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                E_10.tStop = t  # not accounting for scr refresh
                E_10.frameNStop = frameN  # exact frame index
                win.timeOnFlip(E_10, 'tStopRefresh')  # time at next scr refresh
                E_10.setAutoDraw(False)
        
        # *S_6* updates
        if S_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            S_6.frameNStart = frameN  # exact frame index
            S_6.tStart = t  # local t and not account for scr refresh
            S_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(S_6, 'tStartRefresh')  # time at next scr refresh
            S_6.setAutoDraw(True)
        if S_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > S_6.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                S_6.tStop = t  # not accounting for scr refresh
                S_6.frameNStop = frameN  # exact frame index
                win.timeOnFlip(S_6, 'tStopRefresh')  # time at next scr refresh
                S_6.setAutoDraw(False)
        
        # *S_10* updates
        if S_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            S_10.frameNStart = frameN  # exact frame index
            S_10.tStart = t  # local t and not account for scr refresh
            S_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(S_10, 'tStartRefresh')  # time at next scr refresh
            S_10.setAutoDraw(True)
        if S_10.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > S_10.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                S_10.tStop = t  # not accounting for scr refresh
                S_10.frameNStop = frameN  # exact frame index
                win.timeOnFlip(S_10, 'tStopRefresh')  # time at next scr refresh
                S_10.setAutoDraw(False)
        
        # *W_6* updates
        if W_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            W_6.frameNStart = frameN  # exact frame index
            W_6.tStart = t  # local t and not account for scr refresh
            W_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(W_6, 'tStartRefresh')  # time at next scr refresh
            W_6.setAutoDraw(True)
        if W_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > W_6.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                W_6.tStop = t  # not accounting for scr refresh
                W_6.frameNStop = frameN  # exact frame index
                win.timeOnFlip(W_6, 'tStopRefresh')  # time at next scr refresh
                W_6.setAutoDraw(False)
        
        # *W_10* updates
        if W_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            W_10.frameNStart = frameN  # exact frame index
            W_10.tStart = t  # local t and not account for scr refresh
            W_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(W_10, 'tStartRefresh')  # time at next scr refresh
            W_10.setAutoDraw(True)
        if W_10.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > W_10.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                W_10.tStop = t  # not accounting for scr refresh
                W_10.frameNStop = frameN  # exact frame index
                win.timeOnFlip(W_10, 'tStopRefresh')  # time at next scr refresh
                W_10.setAutoDraw(False)
        
        # *NE_10* updates
        if NE_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            NE_10.frameNStart = frameN  # exact frame index
            NE_10.tStart = t  # local t and not account for scr refresh
            NE_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(NE_10, 'tStartRefresh')  # time at next scr refresh
            NE_10.setAutoDraw(True)
        if NE_10.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > NE_10.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                NE_10.tStop = t  # not accounting for scr refresh
                NE_10.frameNStop = frameN  # exact frame index
                win.timeOnFlip(NE_10, 'tStopRefresh')  # time at next scr refresh
                NE_10.setAutoDraw(False)
        
        # *SE_10* updates
        if SE_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            SE_10.frameNStart = frameN  # exact frame index
            SE_10.tStart = t  # local t and not account for scr refresh
            SE_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(SE_10, 'tStartRefresh')  # time at next scr refresh
            SE_10.setAutoDraw(True)
        if SE_10.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > SE_10.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                SE_10.tStop = t  # not accounting for scr refresh
                SE_10.frameNStop = frameN  # exact frame index
                win.timeOnFlip(SE_10, 'tStopRefresh')  # time at next scr refresh
                SE_10.setAutoDraw(False)
        
        # *SW_10* updates
        if SW_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            SW_10.frameNStart = frameN  # exact frame index
            SW_10.tStart = t  # local t and not account for scr refresh
            SW_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(SW_10, 'tStartRefresh')  # time at next scr refresh
            SW_10.setAutoDraw(True)
        if SW_10.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > SW_10.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                SW_10.tStop = t  # not accounting for scr refresh
                SW_10.frameNStop = frameN  # exact frame index
                win.timeOnFlip(SW_10, 'tStopRefresh')  # time at next scr refresh
                SW_10.setAutoDraw(False)
        
        # *NW_10* updates
        if NW_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            NW_10.frameNStart = frameN  # exact frame index
            NW_10.tStart = t  # local t and not account for scr refresh
            NW_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(NW_10, 'tStartRefresh')  # time at next scr refresh
            NW_10.setAutoDraw(True)
        if NW_10.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > NW_10.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                NW_10.tStop = t  # not accounting for scr refresh
                NW_10.frameNStop = frameN  # exact frame index
                win.timeOnFlip(NW_10, 'tStopRefresh')  # time at next scr refresh
                NW_10.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in saccadesComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "saccades"-------
    for thisComponent in saccadesComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    SAC_trials.addData('black_background10.started', black_background10.tStartRefresh)
    SAC_trials.addData('black_background10.stopped', black_background10.tStopRefresh)
    SAC_trials.addData('N_6.started', N_6.tStartRefresh)
    SAC_trials.addData('N_6.stopped', N_6.tStopRefresh)
    SAC_trials.addData('N_10.started', N_10.tStartRefresh)
    SAC_trials.addData('N_10.stopped', N_10.tStopRefresh)
    SAC_trials.addData('E_6.started', E_6.tStartRefresh)
    SAC_trials.addData('E_6.stopped', E_6.tStopRefresh)
    SAC_trials.addData('E_10.started', E_10.tStartRefresh)
    SAC_trials.addData('E_10.stopped', E_10.tStopRefresh)
    SAC_trials.addData('S_6.started', S_6.tStartRefresh)
    SAC_trials.addData('S_6.stopped', S_6.tStopRefresh)
    SAC_trials.addData('S_10.started', S_10.tStartRefresh)
    SAC_trials.addData('S_10.stopped', S_10.tStopRefresh)
    SAC_trials.addData('W_6.started', W_6.tStartRefresh)
    SAC_trials.addData('W_6.stopped', W_6.tStopRefresh)
    SAC_trials.addData('W_10.started', W_10.tStartRefresh)
    SAC_trials.addData('W_10.stopped', W_10.tStopRefresh)
    SAC_trials.addData('NE_10.started', NE_10.tStartRefresh)
    SAC_trials.addData('NE_10.stopped', NE_10.tStopRefresh)
    SAC_trials.addData('SE_10.started', SE_10.tStartRefresh)
    SAC_trials.addData('SE_10.stopped', SE_10.tStopRefresh)
    SAC_trials.addData('SW_10.started', SW_10.tStartRefresh)
    SAC_trials.addData('SW_10.stopped', SW_10.tStopRefresh)
    SAC_trials.addData('NW_10.started', NW_10.tStartRefresh)
    SAC_trials.addData('NW_10.stopped', NW_10.tStopRefresh)
    thisExp.nextEntry()
    
# completed 2.0 repeats of 'SAC_trials'

# get names of stimulus parameters
if SAC_trials.trialList in ([], [None], None):
    params = []
else:
    params = SAC_trials.trialList[0].keys()
# save data for this loop
SAC_trials.saveAsExcel(filename + '.xlsx', sheetName='SAC_trials',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "instr_SP"-------
continueRoutine = True
# update component parameters for each repeat
Smooth_pursuit_instructions.keys = []
Smooth_pursuit_instructions.rt = []
_Smooth_pursuit_instructions_allKeys = []
# keep track of which components have finished
instr_SPComponents = [black_background11, SP_instructions_done, Smooth_pursuit_instructions]
for thisComponent in instr_SPComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instr_SPClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instr_SP"-------
while continueRoutine:
    # get current time
    t = instr_SPClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instr_SPClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *black_background11* updates
    if black_background11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        black_background11.frameNStart = frameN  # exact frame index
        black_background11.tStart = t  # local t and not account for scr refresh
        black_background11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(black_background11, 'tStartRefresh')  # time at next scr refresh
        black_background11.setAutoDraw(True)
    
    # *SP_instructions_done* updates
    if SP_instructions_done.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        SP_instructions_done.frameNStart = frameN  # exact frame index
        SP_instructions_done.tStart = t  # local t and not account for scr refresh
        SP_instructions_done.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(SP_instructions_done, 'tStartRefresh')  # time at next scr refresh
        SP_instructions_done.setAutoDraw(True)
    
    # *Smooth_pursuit_instructions* updates
    waitOnFlip = False
    if Smooth_pursuit_instructions.status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
        # keep track of start time/frame for later
        Smooth_pursuit_instructions.frameNStart = frameN  # exact frame index
        Smooth_pursuit_instructions.tStart = t  # local t and not account for scr refresh
        Smooth_pursuit_instructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Smooth_pursuit_instructions, 'tStartRefresh')  # time at next scr refresh
        Smooth_pursuit_instructions.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(Smooth_pursuit_instructions.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(Smooth_pursuit_instructions.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Smooth_pursuit_instructions.status == STARTED and not waitOnFlip:
        theseKeys = Smooth_pursuit_instructions.getKeys(keyList=['y', 'n', 'left', 'right', 'space', '1', '2', '3'], waitRelease=False)
        _Smooth_pursuit_instructions_allKeys.extend(theseKeys)
        if len(_Smooth_pursuit_instructions_allKeys):
            Smooth_pursuit_instructions.keys = _Smooth_pursuit_instructions_allKeys[-1].name  # just the last key pressed
            Smooth_pursuit_instructions.rt = _Smooth_pursuit_instructions_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr_SPComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr_SP"-------
for thisComponent in instr_SPComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('black_background11.started', black_background11.tStartRefresh)
thisExp.addData('black_background11.stopped', black_background11.tStopRefresh)
thisExp.addData('SP_instructions_done.started', SP_instructions_done.tStartRefresh)
thisExp.addData('SP_instructions_done.stopped', SP_instructions_done.tStopRefresh)
# check responses
if Smooth_pursuit_instructions.keys in ['', [], None]:  # No response was made
    Smooth_pursuit_instructions.keys = None
thisExp.addData('Smooth_pursuit_instructions.keys',Smooth_pursuit_instructions.keys)
if Smooth_pursuit_instructions.keys != None:  # we had a response
    thisExp.addData('Smooth_pursuit_instructions.rt', Smooth_pursuit_instructions.rt)
thisExp.addData('Smooth_pursuit_instructions.started', Smooth_pursuit_instructions.tStartRefresh)
thisExp.addData('Smooth_pursuit_instructions.stopped', Smooth_pursuit_instructions.tStopRefresh)
thisExp.nextEntry()
# the Routine "instr_SP" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
SP_trials = data.TrialHandler(nReps=5.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('SP_loop.xlsx'),
    seed=None, name='SP_trials')
thisExp.addLoop(SP_trials)  # add the loop to the experiment
thisSP_trial = SP_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisSP_trial.rgb)
if thisSP_trial != None:
    for paramName in thisSP_trial:
        exec('{} = thisSP_trial[paramName]'.format(paramName))

for thisSP_trial in SP_trials:
    currentLoop = SP_trials
    # abbreviate parameter names if possible (e.g. rgb = thisSP_trial.rgb)
    if thisSP_trial != None:
        for paramName in thisSP_trial:
            exec('{} = thisSP_trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "fix"-------
    continueRoutine = True
    routineTimer.add(1.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    fixComponents = [black_background12, SP_fixation_target]
    for thisComponent in fixComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    fixClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "fix"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = fixClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=fixClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *black_background12* updates
        if black_background12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            black_background12.frameNStart = frameN  # exact frame index
            black_background12.tStart = t  # local t and not account for scr refresh
            black_background12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(black_background12, 'tStartRefresh')  # time at next scr refresh
            black_background12.setAutoDraw(True)
        if black_background12.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > black_background12.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                black_background12.tStop = t  # not accounting for scr refresh
                black_background12.frameNStop = frameN  # exact frame index
                win.timeOnFlip(black_background12, 'tStopRefresh')  # time at next scr refresh
                black_background12.setAutoDraw(False)
        
        # *SP_fixation_target* updates
        if SP_fixation_target.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            SP_fixation_target.frameNStart = frameN  # exact frame index
            SP_fixation_target.tStart = t  # local t and not account for scr refresh
            SP_fixation_target.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(SP_fixation_target, 'tStartRefresh')  # time at next scr refresh
            SP_fixation_target.setAutoDraw(True)
        if SP_fixation_target.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > SP_fixation_target.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                SP_fixation_target.tStop = t  # not accounting for scr refresh
                SP_fixation_target.frameNStop = frameN  # exact frame index
                win.timeOnFlip(SP_fixation_target, 'tStopRefresh')  # time at next scr refresh
                SP_fixation_target.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fix"-------
    for thisComponent in fixComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    SP_trials.addData('black_background12.started', black_background12.tStartRefresh)
    SP_trials.addData('black_background12.stopped', black_background12.tStopRefresh)
    SP_trials.addData('SP_fixation_target.started', SP_fixation_target.tStartRefresh)
    SP_trials.addData('SP_fixation_target.stopped', SP_fixation_target.tStopRefresh)
    
    # ------Prepare to start Routine "start_sp"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    stimuli_north_2.setOpacity(opacity_north)
    stimuli_east_2.setOpacity(opacity_east)
    stimuli_south_2.setOpacity(opacity_south)
    stimuli_west_2.setOpacity(opacity_west)
    # keep track of which components have finished
    start_spComponents = [black_background13, stimuli_north_2, stimuli_east_2, stimuli_south_2, stimuli_west_2]
    for thisComponent in start_spComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    start_spClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "start_sp"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = start_spClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=start_spClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *black_background13* updates
        if black_background13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            black_background13.frameNStart = frameN  # exact frame index
            black_background13.tStart = t  # local t and not account for scr refresh
            black_background13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(black_background13, 'tStartRefresh')  # time at next scr refresh
            black_background13.setAutoDraw(True)
        if black_background13.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > black_background13.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                black_background13.tStop = t  # not accounting for scr refresh
                black_background13.frameNStop = frameN  # exact frame index
                win.timeOnFlip(black_background13, 'tStopRefresh')  # time at next scr refresh
                black_background13.setAutoDraw(False)
        
        # *stimuli_north_2* updates
        if stimuli_north_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            stimuli_north_2.frameNStart = frameN  # exact frame index
            stimuli_north_2.tStart = t  # local t and not account for scr refresh
            stimuli_north_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stimuli_north_2, 'tStartRefresh')  # time at next scr refresh
            stimuli_north_2.setAutoDraw(True)
        if stimuli_north_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > stimuli_north_2.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                stimuli_north_2.tStop = t  # not accounting for scr refresh
                stimuli_north_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(stimuli_north_2, 'tStopRefresh')  # time at next scr refresh
                stimuli_north_2.setAutoDraw(False)
        
        # *stimuli_east_2* updates
        if stimuli_east_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            stimuli_east_2.frameNStart = frameN  # exact frame index
            stimuli_east_2.tStart = t  # local t and not account for scr refresh
            stimuli_east_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stimuli_east_2, 'tStartRefresh')  # time at next scr refresh
            stimuli_east_2.setAutoDraw(True)
        if stimuli_east_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > stimuli_east_2.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                stimuli_east_2.tStop = t  # not accounting for scr refresh
                stimuli_east_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(stimuli_east_2, 'tStopRefresh')  # time at next scr refresh
                stimuli_east_2.setAutoDraw(False)
        
        # *stimuli_south_2* updates
        if stimuli_south_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            stimuli_south_2.frameNStart = frameN  # exact frame index
            stimuli_south_2.tStart = t  # local t and not account for scr refresh
            stimuli_south_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stimuli_south_2, 'tStartRefresh')  # time at next scr refresh
            stimuli_south_2.setAutoDraw(True)
        if stimuli_south_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > stimuli_south_2.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                stimuli_south_2.tStop = t  # not accounting for scr refresh
                stimuli_south_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(stimuli_south_2, 'tStopRefresh')  # time at next scr refresh
                stimuli_south_2.setAutoDraw(False)
        
        # *stimuli_west_2* updates
        if stimuli_west_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            stimuli_west_2.frameNStart = frameN  # exact frame index
            stimuli_west_2.tStart = t  # local t and not account for scr refresh
            stimuli_west_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stimuli_west_2, 'tStartRefresh')  # time at next scr refresh
            stimuli_west_2.setAutoDraw(True)
        if stimuli_west_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > stimuli_west_2.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                stimuli_west_2.tStop = t  # not accounting for scr refresh
                stimuli_west_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(stimuli_west_2, 'tStopRefresh')  # time at next scr refresh
                stimuli_west_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in start_spComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "start_sp"-------
    for thisComponent in start_spComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    SP_trials.addData('black_background13.started', black_background13.tStartRefresh)
    SP_trials.addData('black_background13.stopped', black_background13.tStopRefresh)
    SP_trials.addData('stimuli_north_2.started', stimuli_north_2.tStartRefresh)
    SP_trials.addData('stimuli_north_2.stopped', stimuli_north_2.tStopRefresh)
    SP_trials.addData('stimuli_east_2.started', stimuli_east_2.tStartRefresh)
    SP_trials.addData('stimuli_east_2.stopped', stimuli_east_2.tStopRefresh)
    SP_trials.addData('stimuli_south_2.started', stimuli_south_2.tStartRefresh)
    SP_trials.addData('stimuli_south_2.stopped', stimuli_south_2.tStopRefresh)
    SP_trials.addData('stimuli_west_2.started', stimuli_west_2.tStartRefresh)
    SP_trials.addData('stimuli_west_2.stopped', stimuli_west_2.tStopRefresh)
    
    # ------Prepare to start Routine "trial_SP"-------
    continueRoutine = True
    routineTimer.add(1.800000)
    # update component parameters for each repeat
    stimuli_north.setOpacity(opacity_north)
    stimuli_east.setOpacity(opacity_east)
    stimuli_south.setOpacity(opacity_south)
    stimuli_west.setOpacity(opacity_west)
    SP_fixation_target2.setOpacity(opacity_north)
    SP_fixation_target3.setOpacity(opacity_south)
    # keep track of which components have finished
    trial_SPComponents = [black_background14, stimuli_north, stimuli_east, stimuli_south, stimuli_west, SP_fixation_target2, SP_fixation_target3]
    for thisComponent in trial_SPComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trial_SPClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial_SP"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trial_SPClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trial_SPClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *black_background14* updates
        if black_background14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            black_background14.frameNStart = frameN  # exact frame index
            black_background14.tStart = t  # local t and not account for scr refresh
            black_background14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(black_background14, 'tStartRefresh')  # time at next scr refresh
            black_background14.setAutoDraw(True)
        if black_background14.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > black_background14.tStartRefresh + 1.8-frameTolerance:
                # keep track of stop time/frame for later
                black_background14.tStop = t  # not accounting for scr refresh
                black_background14.frameNStop = frameN  # exact frame index
                win.timeOnFlip(black_background14, 'tStopRefresh')  # time at next scr refresh
                black_background14.setAutoDraw(False)
        
        # *stimuli_north* updates
        if stimuli_north.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            stimuli_north.frameNStart = frameN  # exact frame index
            stimuli_north.tStart = t  # local t and not account for scr refresh
            stimuli_north.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stimuli_north, 'tStartRefresh')  # time at next scr refresh
            stimuli_north.setAutoDraw(True)
        if stimuli_north.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > stimuli_north.tStartRefresh + 1.25-frameTolerance:
                # keep track of stop time/frame for later
                stimuli_north.tStop = t  # not accounting for scr refresh
                stimuli_north.frameNStop = frameN  # exact frame index
                win.timeOnFlip(stimuli_north, 'tStopRefresh')  # time at next scr refresh
                stimuli_north.setAutoDraw(False)
        if stimuli_north.status == STARTED:  # only update if drawing
            stimuli_north.setPos((0, 6-t*10), log=False)
        
        # *stimuli_east* updates
        if stimuli_east.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            stimuli_east.frameNStart = frameN  # exact frame index
            stimuli_east.tStart = t  # local t and not account for scr refresh
            stimuli_east.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stimuli_east, 'tStartRefresh')  # time at next scr refresh
            stimuli_east.setAutoDraw(True)
        if stimuli_east.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > stimuli_east.tStartRefresh + 1.8-frameTolerance:
                # keep track of stop time/frame for later
                stimuli_east.tStop = t  # not accounting for scr refresh
                stimuli_east.frameNStop = frameN  # exact frame index
                win.timeOnFlip(stimuli_east, 'tStopRefresh')  # time at next scr refresh
                stimuli_east.setAutoDraw(False)
        if stimuli_east.status == STARTED:  # only update if drawing
            stimuli_east.setPos((6-t*10, 0), log=False)
        
        # *stimuli_south* updates
        if stimuli_south.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            stimuli_south.frameNStart = frameN  # exact frame index
            stimuli_south.tStart = t  # local t and not account for scr refresh
            stimuli_south.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stimuli_south, 'tStartRefresh')  # time at next scr refresh
            stimuli_south.setAutoDraw(True)
        if stimuli_south.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > stimuli_south.tStartRefresh + 1.25-frameTolerance:
                # keep track of stop time/frame for later
                stimuli_south.tStop = t  # not accounting for scr refresh
                stimuli_south.frameNStop = frameN  # exact frame index
                win.timeOnFlip(stimuli_south, 'tStopRefresh')  # time at next scr refresh
                stimuli_south.setAutoDraw(False)
        if stimuli_south.status == STARTED:  # only update if drawing
            stimuli_south.setPos((0,-6+t*10), log=False)
        
        # *stimuli_west* updates
        if stimuli_west.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            stimuli_west.frameNStart = frameN  # exact frame index
            stimuli_west.tStart = t  # local t and not account for scr refresh
            stimuli_west.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stimuli_west, 'tStartRefresh')  # time at next scr refresh
            stimuli_west.setAutoDraw(True)
        if stimuli_west.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > stimuli_west.tStartRefresh + 1.8-frameTolerance:
                # keep track of stop time/frame for later
                stimuli_west.tStop = t  # not accounting for scr refresh
                stimuli_west.frameNStop = frameN  # exact frame index
                win.timeOnFlip(stimuli_west, 'tStopRefresh')  # time at next scr refresh
                stimuli_west.setAutoDraw(False)
        if stimuli_west.status == STARTED:  # only update if drawing
            stimuli_west.setPos((-6+t*10, 0), log=False)
        
        # *SP_fixation_target2* updates
        if SP_fixation_target2.status == NOT_STARTED and tThisFlip >= 1.25-frameTolerance:
            # keep track of start time/frame for later
            SP_fixation_target2.frameNStart = frameN  # exact frame index
            SP_fixation_target2.tStart = t  # local t and not account for scr refresh
            SP_fixation_target2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(SP_fixation_target2, 'tStartRefresh')  # time at next scr refresh
            SP_fixation_target2.setAutoDraw(True)
        if SP_fixation_target2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > SP_fixation_target2.tStartRefresh + 0.55-frameTolerance:
                # keep track of stop time/frame for later
                SP_fixation_target2.tStop = t  # not accounting for scr refresh
                SP_fixation_target2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(SP_fixation_target2, 'tStopRefresh')  # time at next scr refresh
                SP_fixation_target2.setAutoDraw(False)
        
        # *SP_fixation_target3* updates
        if SP_fixation_target3.status == NOT_STARTED and tThisFlip >= 1.25-frameTolerance:
            # keep track of start time/frame for later
            SP_fixation_target3.frameNStart = frameN  # exact frame index
            SP_fixation_target3.tStart = t  # local t and not account for scr refresh
            SP_fixation_target3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(SP_fixation_target3, 'tStartRefresh')  # time at next scr refresh
            SP_fixation_target3.setAutoDraw(True)
        if SP_fixation_target3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > SP_fixation_target3.tStartRefresh + 0.55-frameTolerance:
                # keep track of stop time/frame for later
                SP_fixation_target3.tStop = t  # not accounting for scr refresh
                SP_fixation_target3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(SP_fixation_target3, 'tStopRefresh')  # time at next scr refresh
                SP_fixation_target3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial_SPComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial_SP"-------
    for thisComponent in trial_SPComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    SP_trials.addData('black_background14.started', black_background14.tStartRefresh)
    SP_trials.addData('black_background14.stopped', black_background14.tStopRefresh)
    SP_trials.addData('stimuli_north.started', stimuli_north.tStartRefresh)
    SP_trials.addData('stimuli_north.stopped', stimuli_north.tStopRefresh)
    SP_trials.addData('stimuli_east.started', stimuli_east.tStartRefresh)
    SP_trials.addData('stimuli_east.stopped', stimuli_east.tStopRefresh)
    SP_trials.addData('stimuli_south.started', stimuli_south.tStartRefresh)
    SP_trials.addData('stimuli_south.stopped', stimuli_south.tStopRefresh)
    SP_trials.addData('stimuli_west.started', stimuli_west.tStartRefresh)
    SP_trials.addData('stimuli_west.stopped', stimuli_west.tStopRefresh)
    SP_trials.addData('SP_fixation_target2.started', SP_fixation_target2.tStartRefresh)
    SP_trials.addData('SP_fixation_target2.stopped', SP_fixation_target2.tStopRefresh)
    SP_trials.addData('SP_fixation_target3.started', SP_fixation_target3.tStartRefresh)
    SP_trials.addData('SP_fixation_target3.stopped', SP_fixation_target3.tStopRefresh)
    thisExp.nextEntry()
    
# completed 5.0 repeats of 'SP_trials'

# get names of stimulus parameters
if SP_trials.trialList in ([], [None], None):
    params = []
else:
    params = SP_trials.trialList[0].keys()
# save data for this loop
SP_trials.saveAsExcel(filename + '.xlsx', sheetName='SP_trials',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "instr_free_view"-------
continueRoutine = True
# update component parameters for each repeat
FV_instructions_done.keys = []
FV_instructions_done.rt = []
_FV_instructions_done_allKeys = []
# keep track of which components have finished
instr_free_viewComponents = [black_background15, instructions_free_view, FV_instructions_done]
for thisComponent in instr_free_viewComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instr_free_viewClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instr_free_view"-------
while continueRoutine:
    # get current time
    t = instr_free_viewClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instr_free_viewClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *black_background15* updates
    if black_background15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        black_background15.frameNStart = frameN  # exact frame index
        black_background15.tStart = t  # local t and not account for scr refresh
        black_background15.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(black_background15, 'tStartRefresh')  # time at next scr refresh
        black_background15.setAutoDraw(True)
    
    # *instructions_free_view* updates
    if instructions_free_view.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions_free_view.frameNStart = frameN  # exact frame index
        instructions_free_view.tStart = t  # local t and not account for scr refresh
        instructions_free_view.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions_free_view, 'tStartRefresh')  # time at next scr refresh
        instructions_free_view.setAutoDraw(True)
    
    # *FV_instructions_done* updates
    waitOnFlip = False
    if FV_instructions_done.status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
        # keep track of start time/frame for later
        FV_instructions_done.frameNStart = frameN  # exact frame index
        FV_instructions_done.tStart = t  # local t and not account for scr refresh
        FV_instructions_done.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(FV_instructions_done, 'tStartRefresh')  # time at next scr refresh
        FV_instructions_done.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(FV_instructions_done.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(FV_instructions_done.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if FV_instructions_done.status == STARTED and not waitOnFlip:
        theseKeys = FV_instructions_done.getKeys(keyList=['y', 'n', 'left', 'right', 'space'], waitRelease=False)
        _FV_instructions_done_allKeys.extend(theseKeys)
        if len(_FV_instructions_done_allKeys):
            FV_instructions_done.keys = _FV_instructions_done_allKeys[-1].name  # just the last key pressed
            FV_instructions_done.rt = _FV_instructions_done_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr_free_viewComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr_free_view"-------
for thisComponent in instr_free_viewComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('black_background15.started', black_background15.tStartRefresh)
thisExp.addData('black_background15.stopped', black_background15.tStopRefresh)
thisExp.addData('instructions_free_view.started', instructions_free_view.tStartRefresh)
thisExp.addData('instructions_free_view.stopped', instructions_free_view.tStopRefresh)
# check responses
if FV_instructions_done.keys in ['', [], None]:  # No response was made
    FV_instructions_done.keys = None
thisExp.addData('FV_instructions_done.keys',FV_instructions_done.keys)
if FV_instructions_done.keys != None:  # we had a response
    thisExp.addData('FV_instructions_done.rt', FV_instructions_done.rt)
thisExp.addData('FV_instructions_done.started', FV_instructions_done.tStartRefresh)
thisExp.addData('FV_instructions_done.stopped', FV_instructions_done.tStopRefresh)
thisExp.nextEntry()
# the Routine "instr_free_view" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('FV_loop.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "free_viewing_photos"-------
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    FV_photo.setImage(Free_view_figs)
    # keep track of which components have finished
    free_viewing_photosComponents = [FV_photo]
    for thisComponent in free_viewing_photosComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    free_viewing_photosClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "free_viewing_photos"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = free_viewing_photosClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=free_viewing_photosClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *FV_photo* updates
        if FV_photo.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            FV_photo.frameNStart = frameN  # exact frame index
            FV_photo.tStart = t  # local t and not account for scr refresh
            FV_photo.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(FV_photo, 'tStartRefresh')  # time at next scr refresh
            FV_photo.setAutoDraw(True)
        if FV_photo.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > FV_photo.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                FV_photo.tStop = t  # not accounting for scr refresh
                FV_photo.frameNStop = frameN  # exact frame index
                win.timeOnFlip(FV_photo, 'tStopRefresh')  # time at next scr refresh
                FV_photo.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in free_viewing_photosComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "free_viewing_photos"-------
    for thisComponent in free_viewing_photosComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('FV_photo.started', FV_photo.tStartRefresh)
    trials.addData('FV_photo.stopped', FV_photo.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials'

# get names of stimulus parameters
if trials.trialList in ([], [None], None):
    params = []
else:
    params = trials.trialList[0].keys()
# save data for this loop
trials.saveAsExcel(filename + '.xlsx', sheetName='trials',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "break_3"-------
continueRoutine = True
# update component parameters for each repeat
break_over.keys = []
break_over.rt = []
_break_over_allKeys = []
# keep track of which components have finished
break_3Components = [black_background5, break1, break_over]
for thisComponent in break_3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
break_3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "break_3"-------
while continueRoutine:
    # get current time
    t = break_3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=break_3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *black_background5* updates
    if black_background5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        black_background5.frameNStart = frameN  # exact frame index
        black_background5.tStart = t  # local t and not account for scr refresh
        black_background5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(black_background5, 'tStartRefresh')  # time at next scr refresh
        black_background5.setAutoDraw(True)
    
    # *break1* updates
    if break1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        break1.frameNStart = frameN  # exact frame index
        break1.tStart = t  # local t and not account for scr refresh
        break1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(break1, 'tStartRefresh')  # time at next scr refresh
        break1.setAutoDraw(True)
    
    # *break_over* updates
    waitOnFlip = False
    if break_over.status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
        # keep track of start time/frame for later
        break_over.frameNStart = frameN  # exact frame index
        break_over.tStart = t  # local t and not account for scr refresh
        break_over.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(break_over, 'tStartRefresh')  # time at next scr refresh
        break_over.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(break_over.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(break_over.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if break_over.status == STARTED and not waitOnFlip:
        theseKeys = break_over.getKeys(keyList=['y', 'n', 'left', 'right', 'space', '1', '2', '3'], waitRelease=False)
        _break_over_allKeys.extend(theseKeys)
        if len(_break_over_allKeys):
            break_over.keys = _break_over_allKeys[-1].name  # just the last key pressed
            break_over.rt = _break_over_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in break_3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "break_3"-------
for thisComponent in break_3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('black_background5.started', black_background5.tStartRefresh)
thisExp.addData('black_background5.stopped', black_background5.tStopRefresh)
thisExp.addData('break1.started', break1.tStartRefresh)
thisExp.addData('break1.stopped', break1.tStopRefresh)
# check responses
if break_over.keys in ['', [], None]:  # No response was made
    break_over.keys = None
thisExp.addData('break_over.keys',break_over.keys)
if break_over.keys != None:  # we had a response
    thisExp.addData('break_over.rt', break_over.rt)
thisExp.addData('break_over.started', break_over.tStartRefresh)
thisExp.addData('break_over.stopped', break_over.tStopRefresh)
thisExp.nextEntry()
# the Routine "break_3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "FV_video"-------
continueRoutine = True
routineTimer.add(62.000000)
# update component parameters for each repeat
interrupt_video.keys = []
interrupt_video.rt = []
_interrupt_video_allKeys = []
# keep track of which components have finished
FV_videoComponents = [black_background17, interrupt_video, free_view_video]
for thisComponent in FV_videoComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
FV_videoClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "FV_video"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = FV_videoClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=FV_videoClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *black_background17* updates
    if black_background17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        black_background17.frameNStart = frameN  # exact frame index
        black_background17.tStart = t  # local t and not account for scr refresh
        black_background17.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(black_background17, 'tStartRefresh')  # time at next scr refresh
        black_background17.setAutoDraw(True)
    if black_background17.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > black_background17.tStartRefresh + 62-frameTolerance:
            # keep track of stop time/frame for later
            black_background17.tStop = t  # not accounting for scr refresh
            black_background17.frameNStop = frameN  # exact frame index
            win.timeOnFlip(black_background17, 'tStopRefresh')  # time at next scr refresh
            black_background17.setAutoDraw(False)
    
    # *interrupt_video* updates
    waitOnFlip = False
    if interrupt_video.status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
        # keep track of start time/frame for later
        interrupt_video.frameNStart = frameN  # exact frame index
        interrupt_video.tStart = t  # local t and not account for scr refresh
        interrupt_video.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(interrupt_video, 'tStartRefresh')  # time at next scr refresh
        interrupt_video.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(interrupt_video.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(interrupt_video.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if interrupt_video.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > interrupt_video.tStartRefresh + 57-frameTolerance:
            # keep track of stop time/frame for later
            interrupt_video.tStop = t  # not accounting for scr refresh
            interrupt_video.frameNStop = frameN  # exact frame index
            win.timeOnFlip(interrupt_video, 'tStopRefresh')  # time at next scr refresh
            interrupt_video.status = FINISHED
    if interrupt_video.status == STARTED and not waitOnFlip:
        theseKeys = interrupt_video.getKeys(keyList=['y', 'n', 'left', 'right', 'space'], waitRelease=False)
        _interrupt_video_allKeys.extend(theseKeys)
        if len(_interrupt_video_allKeys):
            interrupt_video.keys = _interrupt_video_allKeys[-1].name  # just the last key pressed
            interrupt_video.rt = _interrupt_video_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *free_view_video* updates
    if free_view_video.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
        # keep track of start time/frame for later
        free_view_video.frameNStart = frameN  # exact frame index
        free_view_video.tStart = t  # local t and not account for scr refresh
        free_view_video.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(free_view_video, 'tStartRefresh')  # time at next scr refresh
        free_view_video.setAutoDraw(True)
    if free_view_video.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > free_view_video.tStartRefresh + 60-frameTolerance:
            # keep track of stop time/frame for later
            free_view_video.tStop = t  # not accounting for scr refresh
            free_view_video.frameNStop = frameN  # exact frame index
            win.timeOnFlip(free_view_video, 'tStopRefresh')  # time at next scr refresh
            free_view_video.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in FV_videoComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "FV_video"-------
for thisComponent in FV_videoComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('black_background17.started', black_background17.tStartRefresh)
thisExp.addData('black_background17.stopped', black_background17.tStopRefresh)
# check responses
if interrupt_video.keys in ['', [], None]:  # No response was made
    interrupt_video.keys = None
thisExp.addData('interrupt_video.keys',interrupt_video.keys)
if interrupt_video.keys != None:  # we had a response
    thisExp.addData('interrupt_video.rt', interrupt_video.rt)
thisExp.addData('interrupt_video.started', interrupt_video.tStartRefresh)
thisExp.addData('interrupt_video.stopped', interrupt_video.tStopRefresh)
thisExp.nextEntry()
free_view_video.stop()

# ------Prepare to start Routine "done"-------
continueRoutine = True
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
doneComponents = [black_background16, done_txt]
for thisComponent in doneComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
doneClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "done"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = doneClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=doneClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *black_background16* updates
    if black_background16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        black_background16.frameNStart = frameN  # exact frame index
        black_background16.tStart = t  # local t and not account for scr refresh
        black_background16.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(black_background16, 'tStartRefresh')  # time at next scr refresh
        black_background16.setAutoDraw(True)
    if black_background16.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > black_background16.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            black_background16.tStop = t  # not accounting for scr refresh
            black_background16.frameNStop = frameN  # exact frame index
            win.timeOnFlip(black_background16, 'tStopRefresh')  # time at next scr refresh
            black_background16.setAutoDraw(False)
    
    # *done_txt* updates
    if done_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        done_txt.frameNStart = frameN  # exact frame index
        done_txt.tStart = t  # local t and not account for scr refresh
        done_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(done_txt, 'tStartRefresh')  # time at next scr refresh
        done_txt.setAutoDraw(True)
    if done_txt.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > done_txt.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            done_txt.tStop = t  # not accounting for scr refresh
            done_txt.frameNStop = frameN  # exact frame index
            win.timeOnFlip(done_txt, 'tStopRefresh')  # time at next scr refresh
            done_txt.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in doneComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "done"-------
for thisComponent in doneComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('black_background16.started', black_background16.tStartRefresh)
thisExp.addData('black_background16.stopped', black_background16.tStopRefresh)
thisExp.addData('done_txt.started', done_txt.tStartRefresh)
thisExp.addData('done_txt.stopped', done_txt.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
