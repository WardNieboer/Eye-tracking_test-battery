This test battery was developed by Ward Nieboer, Vrije Universiteit Amsterdam, with the aim to assess visual function in individuals with vision impairment. 
The eye tracker used with this test battery was the Pupil Invisible (Pupil Labs GmbH, Germany).
The test battery consists of 5 tests (in fixed order):
1) Visual search test
2) Fixation stability test
3) Saccades test
4) Smooth pursuit test
5) Free viewing (photos + video)
The test battery was developed based on the framework outlined in:
Nieboer, W., Ghiani, A., De Vries, R., Brenner, E., & Mann, D. L. (2023). Eye Tracking to Assess the Functional Consequences of Vision Impairment: A Systematic Review. Optometry and Vision Science, 100(12), 861-875.
The test battery was administered and validated among 46 individuals* with vision impairment (*Paralympic athletes with vision impairment):
Nieboer, W., Mann, D.L. (Submitted for publication). Eye tracking for the classification of visual function in individuals with vision impairment. Manuscript can be requested, see contact details below.

The test battery was developed and executed in PsychoPy Builder (free software: www.psychopy.org) and Python version 3.9:
Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. https://doi.org/10.3758/s13428-018-01193-y
Files you need to run the test in PsychoPy or Python:
- Nieboer_eye-tracking-test-battery.psyexp or .py
- calibration_opacity.xlsx - this file determines which stimuli is presented during calibration check.
- VS_figs folder - this folder contains the visual search figures
- VS_fam_loop.xlsx - this file determines which visual search figures are presented during familiarisation of the visual search test.
- VS_figs_loop.xlsx - this file determines which visual search figures are presented during visual search test.
- SACC_loop.xlsx - this file determines the location of the targets during the saccades test
- SP_loop.xlsx - this file determines the location of the targets during smooth pursuit test
- FV_figs folder - this folder contains the images presented during free viewing
- FV_loop.xlsx - this file determines which images are presented during free viewing
- Free-view_vid.mp4 - this file is the free viewing video.

Visual angles are determined by screen resolution, physical screen size, and participants distance to screen. You can use this tool: https://www.sr-research.com/visual-angle-calculator/ to make sure that all stimuli are presented at the correct visual angle (it may require an actual measuring tape, sorry!).

For questions, contact:
w.nieboer@vu.nl
ward.nieboer@paralympic.org

DATA ANALYSIS WILL BE AVAILABLE SOON!!!

Method section:

Apparatus and Materials
The eye movement data were collected using a Pupil Invisible head-mounted infrared eye-tracker (Pupil Labs GmbH, Germany). The eye-tracker recorded the eye movements of both participants' eyes at a sampling rate of 200 Hz. This eye-tracking system employs an artificial intelligence-based algorithm that automatically detects eye landmarks such as the pupil and corneal reflections, eliminating the need for manual calibration. Since calibration can be challenging for individuals with vision impairment, this setup was preferred for the study (Nieboer et al., 2023). We conducted a verification process to check the accuracy of the automated calibration. A grid of five circles, each with a diameter of approximately 14 degrees, was presented on a screen to the participants. Participants were instructed to fixate on each circle in the grid one by one. Any calibration offset observed during this verification process was manually corrected using the Pupil Invisible software.

The visual stimuli for the experiment were presented on an Acer Nitro xv273xb monitor, which had a screen size of 27 inches and a resolution of 1920 x 1080 pixels. When seated 60 away from the monitor, the screen subtends a visual angle of 55.3 degrees and 34.7 degrees in width and height, respectively. The monitor had a high refresh rate of 240 Hz, ensuring smooth and precise presentation of stimuli. The stimuli were presented using a custom-built tool developed in PsychoPy (version 2021.2.3).

Procedure
During the experiment, participants wore the head-mounted eye-tracker and sat 60 cm from the monitor. All tests and eye movement recordings were conducted binocularly. Participants were instructed to minimize their head movements, but their head was not restricted in any way. 

The test battery   consisted of five different tests of eye movement paradigms, all of which were completed by the participants. These paradigms included tests of: i) fixation stability, ii) smooth pursuit, iii) saccades, iv) free viewing, v) visual search. The tests were also administered in this order. Participants were given short breaks between each test to rest. The total duration of all tests combined, including breaks, was approximately thirty minutes.

Fixation stability
The test of fixation stability assessed the ability to maintain steady fixation on a target (Bellmann et al., 2004; Crossland et al., 2004; Ghasia et al., 2018; Murray et al., 2022; Tarita-Nistor et al., 2017). The fixation target was a white cross consisting of a single horizontal and vertical line (thickness = 1 degree of visual angle) that spanned the full width and height of the screen respectively, and within the white cross, an inner black cross with lines of 0.4 degrees visual angle. The background was black. The design of the target allowed participants to locate and direct their gaze towards the centre of the cross even in the presence of a central scotoma. Participants were instructed to maintain steady fixation on the centre of the cross until it disappeared, the cross was presented for thirty seconds. Participants were also instructed to limit their head movements and minimize blinking during the task.

Stability was measured using the Bivariate Contour Ellipse Area (BCEA). The BCEA quantifies the spread of fixations by calculating the area of an ellipse which encompasses fixation points for a given proportion of eye positions during the test. A lower BCEA indicates greater fixation stability. The BCEA was computed using Equation (1), where σ_h represents the standard deviation of gaze coordinates in the x direction, σ_v represents the standard deviation of gaze coordinates in the y direction, ρ represents the product-moment correlation of these two position components, and k is a constant (set at 1.14) representing the chosen probability area of 68% of eye positions during a trial (Crossland et al., 2004).
BCEA=2kπσ_h σ_v 〖(1-ρ^2  )〗^(1/2)							(1)
The other outcome variable for fixation stability was the number of saccades, which are labelled as intrusive saccades since they are unwanted during a period of steady fixation and can be a consequence of vision impairment. The initial two seconds of the test were excluded from analysis in case participants were still locating the centre of the cross during that period.

Smooth pursuit
We employed a step-ramp paradigm to test smooth pursuit eye movements (Gonzalez et al., 2018; Raashid et al., 2016; Shanidze et al., 2017; Shanidze et al., 2020). Initially, a white fixation dot (diameter 1 degree) was presented at the centre of the screen, against a black background, for a duration of 1.5 if the target moved vertically over the screen or 2 seconds if the target moved horizontally. Subsequently, the fixation dot disappeared, and a target dot with a diameter of 1 degree appeared at a location 6 degrees away from the fixation point, either at 0, 90, 180, or 270 degrees.

After a delay of 0.5 seconds, the target dot began to move in the direction of the centre of the screen with a constant velocity of 10 degrees per second. If the target moved vertically, its duration was set to 1.25 seconds, while for horizontally moving targets, the duration was 1.75 seconds to optimally use the size of the screen in both directions. Following the specified duration, the target dot vanished, and the fixation dot reappeared, marking the start of a new trial. 

During the test, each target location was presented five times, in a random order, resulting in a total of 20 trials. Participants were instructed to shift their gaze from the fixation dot to the target dot and to track the target dot when it started moving.

Smooth pursuit performance was assessed by calculating the gain, which in this case represents the ratio of eye velocity during target pursuit to the velocity of the target. A gain of 1.0 indicates perfect pursuit. The number of catch-up saccades, which typically occur when the eye's velocity is insufficient to track the target, was counted, and the amplitudes of these catch-up saccades were determined.

Saccades
A step paradigm was used to assess saccades (Fayel et al., 2014; Giacomelli et al., 2020; Niechwiej-Szwedo et al., 2012). The paradigm begun with a white fixation dot (diameter 1 degree) initially displayed at the centre of the screen against a black background. The dot remained visible for 1.5 seconds before it disappeared and immediately reappeared as a target dot at a specific location away from the centre of the screen, remained visible for two seconds, then disappeared again. The dot then immediately reappeared at the centre of the screen as a fixation dot, marking the beginning of a new trial. There were 16 possible locations for the target dot to appear away from the centre of the screen, positioned either 6 degrees or 10 degrees away from the centre in one of eight directions from the fixation dot (i.e., at 0, 45, 90, 135, 180, 225, 270, and 315 degrees). 

During the test, each target location was presented twice, presented in a random order, resulting in a total of 32 trials. Participants were instructed to shift their gaze from the fixation dot to the target dot when it appeared, and vice versa.

From the saccade paradigm, the number of saccades per trial was extracted. While one saccade per trial is expected in a healthy population, multiple saccades per trial suggest difficulties in locating peripheral targets (e.g., peripheral vision loss). Additional variables extracted from the saccade data included peak velocity, saccadic reaction time (the time delay between target onset and saccade onset), and saccadic gain. Saccadic gain was calculated by summing the amplitudes of all saccades during a trial and dividing it by the amplitude of the target step. A gain above 1.0 indicates overshoot, while a gain below 1.0 indicates undershoot of the saccade(s).

Free viewing
The free-viewing paradigm was divided into two parts (Asfaw et al., 2018; Gameiro et al., 2018; Gestefeld et al., 2021; Smith et al., 2012). In the first part, participants were presented with a series of thirty photos, each displayed for a duration of three seconds. The photos encompassed a diverse range of themes, including scenes from nature landscapes, cityscapes, and sport events. The photos varied in composition, with some featuring cluttered scenes and others focusing on central objects or individuals. The majority of the photos were in full colour (n=27), while the remainder were black and white. Each photo occupied the entire screen, with dimensions of 1920 by 1080 pixels. The selection of photos ensured a wide range of saliency across different regions of the screen, capturing participants' attention and prompting exploratory eye movements.

The second part, participants watched a single video of planes taxiing, preparing for take-off, and stationary planes, while various vehicles, such as fuelling cars, moved between the planes at different speeds. The video content was highly dynamic, featuring objects appearing on the screen from various directions. The dynamic nature of the video was designed to elicit reactionary and tracking eye movements. The video lasted 52 seconds and was displayed in full screen. 
Participants were instructed to simply watch the photos and videos without any specific task or response required from them.

From the paradigm, the following eye movement measures were extracted per trial: average number of fixations, average duration of fixations, average number of saccades, average duration of saccades, amplitude of the largest saccade and average amplitude of saccades. The scan path, which quantifies the exploration of the scene, was calculated by summing the amplitudes of all saccades. Additionally, we calculated the BCEA (Equation 1), in this case, representing the area of the screen explored by the participants (Smith et al., 2012).

Visual search
An existing test of visual search was adopted specifically designed for individuals with vision impairment (Fortin-Guichard et al., 2022; Krabben et al., 2021). The test assesses the ability to identify the presence of a circle among a grid of squares. The visual search test comprised three levels of difficulty. In the easiest level, participants were presented with a 3 by 3 grid of white shapes on a black background. Each shape subtended an angle of 8.3 degrees of visual angle (equivalent to 2.0 logMAR). In the second level, an 8 by 8 grid was used, with shapes subtending an angle of 2.6 degrees of visual angle (equivalent to 1.5 logMAR). The third and most challenging level consisted of a 15 by 15 grid, with shapes subtending an angle of 0.83 degrees of visual angle (equivalent to 1.0 logMAR).

During each trial, the stimuli were presented for a maximum of thirty seconds. Participants were required to respond whether a circle was present or not as quickly as possible by pressing the left or right key on a keyboard respectively. Prior to the full test, participants completed six familiarization trials using the easiest test level, where the circle was present four times.

The full test consisted of 18 trials for each level of difficulty, with the circle being present in 12 of the 18 trials. The order of the trials was randomised between participants. For data analysis, the most difficult level completed by each participant was used. A level was considered completed if the participant responded within the given time without reporting to be guessing. Measures of performance were the number of correct answers, level completed, and the average response time. Additionally, eye movements during the search were extracted, these included: average number of fixations per second, average duration of fixations, average number of saccades per second, average duration of saccades, amplitude of the largest saccade, average amplitude of saccades, and scan path in degrees per second.
