from psychopy import visual, event, core, gui, data
import time
from psychopy.visual import ShapeStim
import random
from psychopy.tools.filetools import fromFile, toFile


#user interface where we ask for ID and set the parameters
params = {'ID number':'1',
	 'frameRate':60,'duration':2, 'ISI': 0.02, 'fp': 1,'task':'Reverse_Stroop_Task'}


word_list = {'Blue':'0,0,1', 'Red':'1,0,0', 'Green':'0,1,0', 'Yellow':'1,1,0.6'}


# present a dialogue to change params
dlg = gui.DlgFromDict(params, title='Reverse_Stroop_Task', fixed=['dateStr'])
if dlg.OK:
    toFile('lastParams.pickle', params)#save params to file for next time
else:
    core.quit()#the user hit cancel so exit
    

## make a text file to save data
fileName = params['ID number']
dataFile = open(fileName+'.txt', 'a')#a simple text fil e with 'comma-separated-values'

dataFile.write('trial, word, color, accuracy, RT\n') 
word = ''
color = ''
acc = 0

clockRT = core.Clock() 
trialdur = 0

#create window & fixation & sounds
win = visual.Window(fullscr=False, allowGUI = True, monitor = 'testMonitor', units = 'deg')
fixation = visual.PatchStim(win, color=-1, tex=None, mask='circle',size=0.2, units='deg')


#create mouse
myMouse = event.Mouse(visible = True, win = win)
myMouse.clickReset()
event.clearEvents()
buttons = myMouse.getPressed()


#draw in window
SquareVert = [(-.2,-.2),(-.2,.2),(.2,.2),(.2,-.2)]
square1 = ShapeStim(win, vertices=SquareVert, fillColor='blue', lineWidth=0, size=5, pos=(-5, -5.5))
square2 = ShapeStim(win, vertices=SquareVert, fillColor='green', lineWidth=0, size=5, pos=(5, 5.5))
square3 = ShapeStim(win, vertices=SquareVert, fillColor='yellow', lineWidth=0, size=5, pos=(-5,5.5))
square4 = ShapeStim(win, vertices=SquareVert, fillColor='red', lineWidth=0, size=5, pos=(5, -5.5))

#define function that randomizes the trials (0=congruent, else or 1=incongruent). the function creates a lis, "order", to which it will append a number (either 0 or 1). Then it will shuffle the numbers in the list three times to be sure that the sequence of 0s and 1s is random.
def trial_init(nb_of_trials):
    order = []
    for i in range(2):
        if i == 0:
            for j in range(nb_of_trials):
                order.append(0)
        else:
            for j in range(nb_of_trials):
                order.append(1)
    random.shuffle(order)
    random.shuffle(order)
    random.shuffle(order)
    return(order)

#define two functions: one for the first block (word name) and one for the second block (word color)


win.close()
core.quit()








