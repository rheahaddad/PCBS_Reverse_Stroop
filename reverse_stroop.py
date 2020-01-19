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
squares = [square1, square2, square3, square4]


done = False
nb_trials = 4
counter = 0
section = 0

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


def trial1(order, index): # word name
    global word
    global color
    global acc
    global trialdur
    buttons = myMouse.getPressed()
    if order[index]==0: # Congruent 
        rdm_pair1 = key, val = random.choice(list(word_list.items()))
        msg = visual.TextStim(win, text=key, color = (key))
        word = key
        color = key
        clockRT.reset()
        while buttons == [0,0,0]:
            myMouse.clickReset()
            buttons = myMouse.getPressed()
            msg.draw()
            square1.draw()
            square2.draw()
            square3.draw()
            square4.draw()
            win.update()
        trialdur = clockRT.getTime()
        if key == 'Blue':
            if myMouse.isPressedIn(square1):
                print("Success")
                acc = 1
            else:
                print("Failure")
                acc = 0
        if key == 'Green':
            if myMouse.isPressedIn(square2):
                print("Success")
                acc = 1
            else:
                print("Failure")
                acc = 0
        if key == 'Yellow':
            if myMouse.isPressedIn(square3):
                print("Success")
                acc = 1
            else:
                print("Failure")
                acc = 0
        if key == 'Red':
            if myMouse.isPressedIn(square4):
                print("Success")
                acc = 1
            else:
                print("Failure")
                acc = 0
                
        buttons = myMouse.getPressed()
        
    if order[index]==1: #Incongruent
        rdm_pair1 = key1, val1 = random.choice(list(word_list.items()))
        rdm_pair2 = key2, val2 = random.choice(list(word_list.items()))
        while rdm_pair1==rdm_pair2:
            rdm_pair2 = key2, val2 = random.choice(list(word_list.items()))
        msg = visual.TextStim(win, text=key1, color = (key2))
        word = key1
        color = key2
        clockRT.reset()
        while buttons == [0,0,0]:
            myMouse.clickReset()
            buttons = myMouse.getPressed()
            msg.draw()
            square1.draw()
            square2.draw()
            square3.draw()
            square4.draw()
            win.update()
        trialdur = clockRT.getTime()
        if key1 == 'Blue':
            if myMouse.isPressedIn(square1):
                print("Success")
                acc = 1
            else:
                print("Failure")
                acc = 0
        if key1 == 'Green':
            if myMouse.isPressedIn(square2):
                print("Success")
                acc = 1
            else:
                print("Failure")
                acc = 0
        if key1 == 'Yellow':
            if myMouse.isPressedIn(square3):
                print("Success")
                acc = 1
            else:
                print("Failure")
                acc = 0
        if key1 == 'Red':
            if myMouse.isPressedIn(square4):
                print("Success")
                acc = 1
            else:
                print("Failure")
                acc = 0
                
        buttons = myMouse.getPressed()
    return


def trial2(order, index): # word color
    global word
    global color
    global acc
    global trialdur

    buttons = myMouse.getPressed()
    if order[index]==0: #Congruent
        rdm_pair1 = key, val = random.choice(list(word_list.items()))
        msg = visual.TextStim(win, text=key, color = (key))
        word = key
        color = key
        clockRT.reset()
        while buttons == [0,0,0]:
            myMouse.clickReset()
            buttons = myMouse.getPressed()
            msg.draw()
            square1.draw()
            square2.draw()
            square3.draw()
            square4.draw()
            win.update()
        trialdur = clockRT.getTime()
        if key == 'Blue':
            if myMouse.isPressedIn(square1):
                print("Success")
                acc = 1
            else:
                print("Failure")
                acc = 0
        if key == 'Green':
            if myMouse.isPressedIn(square2):
                print("Success")
                acc = 1
            else:
                print("Failure")
                acc = 0
        if key == 'Yellow':
            if myMouse.isPressedIn(square3):
                print("Success")
                acc = 1
            else:
                print("Failure")
                acc = 0
        if key == 'Red':
            if myMouse.isPressedIn(square4):
                print("Success")
                acc = 1
            else:
                print("Failure")
                acc = 0
                
        buttons = myMouse.getPressed()
        
    if order[index]==1: #Incongruent
        rdm_pair1 = key1, val1 = random.choice(list(word_list.items()))
        rdm_pair2 = key2, val2 = random.choice(list(word_list.items()))
        while rdm_pair1==rdm_pair2:
            rdm_pair2 = key2, val2 = random.choice(list(word_list.items()))
        msg = visual.TextStim(win, text=key1, color = (key2))
        word = key1
        color = key2
        clockRT.reset()
        while buttons == [0,0,0]:
            myMouse.clickReset()
            buttons = myMouse.getPressed()
            msg.draw()
            square1.draw()
            square2.draw()
            square3.draw()
            square4.draw()
            win.update()
        trialdur = clockRT.getTime()
        if key2 == 'Blue':
            if myMouse.isPressedIn(square1):
                print("Success")
                acc = 1
            else:
                print("Failure")
                acc = 0
        if key2 == 'Green':
            if myMouse.isPressedIn(square2):
                print("Success")
                acc = 1
            else:
                print("Failure")
                acc = 0
        if key2 == 'Yellow':
            if myMouse.isPressedIn(square3):
                print("Success")
                acc = 1
            else:
                print("Failure")
                acc = 0
        if key2 == 'Red':
            if myMouse.isPressedIn(square4):
                print("Success")
                acc = 1
            else:
                print("Failure")
                acc = 0
                
        buttons = myMouse.getPressed()
    return


while not done:
    
    order = trial_init(nb_trials)
    
    instructions = TextBox.setText(win, "This is a reverse stroop task. You will have to click on the appropriate colored square depending on the instructions you will get. Press enter to start.")
    instructions.draw()
    win.flip()
        

    for i in range(len(order)):
        trial = "WordName"
        trial1(order, i)
        fixation.draw()
        win.flip()
        core.wait(1)
        core.checkPygletDuringWait = False
        buttons = myMouse.getPressed()
        dataFile.write('%s %s %s %s %s\n'%(trial, word, color, acc, round(trialdur, 3)))
    
    order = trial_init(nb_trials)
    
    for i in range(len(order)):
        trial = "WordColor"
        trial2(order, i)
        fixation.draw()
        win.flip()
        core.wait(1)
        core.checkPygletDuringWait = False
        buttons = myMouse.getPressed()
        dataFile.write('%s %s %s %s %s\n'%(trial, word, color, acc, round(trialdur, 3)))

    done = True

win.close()
core.quit()








