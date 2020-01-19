# PCBS_Reverse_Stroop

The aim of this project is to create a reverse Stroop task. It is a variant of the Stroop task. The participants are shown a word (the name of a color) in either the same color or a different one. Around the word are 4 squares: one is the color of the word, one is the color of written color, and the 2 remaining squares are random colors. 
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

## The trial_init function

This function takes as an argument the number of trials. 
What I'm doing is creating an empty list, 'order', which I will fill. The way I fill this list is the following: I take a variable i in the range 0-2 (which technically means it's either 0 or 1). We will append the 0 to the list for x number of times, x being the number of trials that we would have defined. Then we will append 1 to the list for x number of times. The list 'order' now contains x times 0 and x times 1 in that order. So I now shuffle the numbers in the list three times so that the sequence of 0s and 1s is randomized. What this function is doing is specifying whether a trial is congruent or incongruent. A 0 indicates a congruent trial and a 1 indicates an incongruent trial. This will be helpful for the rest of the code. 

## The trial1 function

This function takes care of the word name condition. First, what I'm doing is redefining the relevant variables inside the function by specifying that they are global which means I could also access them from outside the function. I also redefine the mouse press event. Then, my function is divided in two: if I get a 0 (congruent trial) or if I get a 1 (incongruent trial) in the list. 
In the congruent trials, what happens is the following: I define a variable containing two values (a tuple) extracted from the previously defined dictionary of colors ('word_list') randomly. Then, I specify that the color name that will be printed in the middle of the screen will be congruent: its name and color will be the same ('red' written in red for example) since we define both variables by refering to the same pair of color-name (rdm_pair1). After this, I specify that as long as the mouse has not been pressed, the message (the color name) and the square will be printed/drawn in the window. Finally, I specify the conditions for a correct and a wrong answer: if the color of the square the participant clicked on matches the name of the color printed in the center of the screen, then it is a correct trial. Otherwise, it is an incorrect trial. The accuracy is stored in the variable 'acc'.
Now onto the incongruent trials. Here, it gets more complicated because instead of defining one random pair of word name and word color, we define two and we combine them. This means that we first randomly chose one pair of color and color name from word_list which we store in 'rdm_pair1', then we chose another pair and store it in 'rdm_pair2'. If rdm_pair1 and rdm_pair2 happen to be the same, then we chose another pair to store in rdm_pair2. After doing this, we specify the parameters of the message that will be printed on the screen (the color name). Unlike the congruent trials, here the text (the word name) will be a value stored in rdm_pair1 (key1) and the color (word color) will be a value stored in rdm_pair2. This way, the word name and the word color do not match. Then, the rest of the code for incongruent trials is the same as the one for congruent trials (mouse event, stimuli in window, accuracy).

## The trial2 function

This function is pretty similar to the previous one except that here, we are looking at the color of the word printed in the middle of the 4 squares, not at its name. So, what changes here is how we define a correct response. The rest is the same for congruent vs incongruent trials. A correct response here is when the color of the square the participant clicked on matches the color of the word in the middle of the screen.  

# Bringing it all together

After defining the variables, the stimuli, the events, the functions, ... we now have to use all of these in order to create the experiment. For this, I used a while loop. While we have not gone through each trial in the list (0s and 1s), the loop will keep going. For the index i in the range of the length of the 'order' list (which contains all the 0s and 1s in random order, which indicates whether the trial is congruent or not), we will define this trial as a 'wordname' trial and call the function trial1. It will take as arguments the 'order' list and an index i of that list. It will aslo draw a fixation point between one trial and the next, and save all the important variables to the data file (trial name, word name, word color, accuracy, response time). 
A second similar 'for' loop is also defined for the 'wordcolor' trials and it will call the function trial2.
Finally, we close the window and quit the experiment.

# My prior programming experience

Before this class, I have had very basic experience in programming. I did the baccalauréat spécialité informatique et sciences du numérique where I learned basic python skills. Then, during my bachelor degree in psychology, I worked with a psycholgist who guided me through the programming of a Flanker task on psychopy. 
