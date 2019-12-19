# PCBS_Reverse_Stroop

The aim of this project is to create a reverse stroop task. It is a variant of the Stroop task. The participants are shown a word (the name of a color) in either the same color or a different one. Around the word are 4 squares: one is the color of the word, one is the color of written color, and the 2 remaining squares are random colors. 
The experiment is composed of two blocks. 
In the first one, participants will be asked to click on the square whose color is the same as the written color. 
In the second one, participants will be asked to click on the square whose color is the same as the color of the word.
In each of these two blocks, I will vary the congruence of the word in the middle: either the color of the word and the written word will indicate the same color (i.e. "red" written in red) or they won't (i.e. "red" written in green).
The presentation of each stimulus will be random.
The participants will have to be quick, and I will be collecting their data in a separate txt file: the trial (written word or word color), the written color, the color of the word, the accuracy and the response time. This will all be saved in a data file under the participant's ID number that will be entered at the start of the experiment. 

# The GUI

At the start of the experiment, a dialog box will appear on the screen. It will ask for the ID of the participant, which the experimenter can enter manually. It will also give the possibility to change a few parameters of the experiment. 

# The data file

An csv file will be created which will contain the information collected during the experiment. 
The first parameter that will be included in this file is the block or trial. A column called "Trial" will be created and will specify whether the folowing information (RT, accuracy, ...) concern the first block (word name) or the second block (word color). 
The second parameter is the word name. It will allow us to see what word was printed in the middle of the screen during each trial. 
The third parameter is the word color. It will allow us to see what color the word was printed in, in the middle of the screen during each trial. 
The fourth parameter is accuracy. It will allow us to see whether the participant responded accurately or not in each trial.
The last parameter is response time. The response time will be collected thanks to a clock that will keep track of the time during the experiment and that will reset at the beginning of the trial. 

# Creating the window and the mouse event

For stimuli to be able to appear on the screen, we need to define a window. This is what I have done before I define any of my stimuli. Then, in order for the participants to be able to use the mouse, I had to create a mouse event. I defined a few parameters related to this mouse event (visibility, reset, clearevent) and I also created a variable, "buttons", which takes the value of the event of pressing on the mouse. 

# Creating the square stimuli

I created the four squares (blue, red, green, yellow) which will be invariable in size, shape, and placement on the screen. Randomizing the placement of the squares on the screen would have made it way too hard for me to handle considering that I am already randomizing other variables in my experiment and that my skills in programming are basic. 
Note that I only created the squares, I didnt draw them yet. 

# Defining the important functions
