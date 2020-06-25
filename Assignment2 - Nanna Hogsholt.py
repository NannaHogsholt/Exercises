###Assignment 2 - Reading experiment
###Experimental methods 1
###Nanna Høgsholt
###30/10/2019

#load molues
from psychopy import visual, event, core, gui
#Gets the filenames from a folder
import glob
#alows you to work in two different dataframes. 'as' renames the package
import pandas as pd

##########

#Defining which collums should be in my logfile
logfile = pd.DataFrame(columns = ["ID", "Age", "Gender", "Stimulus", "Reading_time", "Condition"])

###Creating text for the experiment

#Introduction text
IntroText = ("Welcome to the reading experiment.\n\nPress any key to get instructions.")

#Instructions text
IntructionText =("You will now read a story word by word, carefully.\n\nWhen you have read the word presented on the screen press 'space' and a new word will be presented to you.\n\nLet's try a short story first.\n\nPress any key when you are ready.")

#Test story is defined and created as a list to be read word by word
testA = ("Somewhere out there is a girl in a bright yellow raincoat with matching boots, waiting for the bus.")
Listtest = testA.split()

#Test feedback text
TestFeed =("Great job! Now lets start the real story. Press any key to get started.")

#Creating StoryA as a list
StoryA = ("Once upon a time there lived a lion in a forest. One day after a heavy meal. It was sleeping under a tree. After a while, there came a mouse and it started to play on the lion. Suddenly the lion got up with anger and looked for those who disturbed its nice sleep. Then it saw a small mouse standing trembling with fear. The lion jumped on it and started to kill it. The mouse requested the lion to forgive it. The lion felt pity and left it. The mouse ran away. On another day, the lion was caught in a net by a hunter. The mouse came there and cut the net. Thus it escaped. There after, the mouse and the lion became friends. They lived happily in the forest afterwards.")
ListA = StoryA.split()
 
#Creating StoryB as list (Word changed friends (-8) -> famous) 
StoryB = ("Once upon a time there lived a lion in a forest. One day after a heavy meal. It was sleeping under a tree. After a while, there came a mouse and it started to play on the lion. Suddenly the lion got up with anger and looked for those who disturbed its nice sleep. Then it saw a small mouse standing trembling with fear. The lion jumped on it and started to kill it. The mouse requested the lion to forgive it. The lion felt pity and left it. The mouse ran away. On another day, the lion was caught in a net by a hunter. The mouse came there and cut the net. Thus it escaped. There after, the mouse and the lion became famous. They lived happily in the forest afterwards.")
ListB = StoryB.split()

#Final message text
ThankYou =("You are AWESOME! \n\nThank you for participating. \n\nPress 'any' key to quit the experiment")

##########

#Creating a popup window to collect participant data
popup = gui.Dlg(title ="Welcome to the reading Experiment")
#Defining the data to collect (ID, Age, Gender and Condition of the story)
popup.addField("ID: ")
popup.addField("Age: ")
popup.addField("Gender: ", choices = ["Female","Male","other"])
popup.addField("Condition: ", choices = ["StoryA", "StoryB"])
#Showing the popup window
popup.show()

#Collecting data
if popup.OK:
    ID=popup.data[0]
    Age=popup.data[1]
    Gender=popup.data[2]
    Condition=popup.data[3]
    #if pressed cancel quit the experiment
elif popup.Cancel:
    core.quit()

####Starting the experiment

#Defining window
win = visual.Window(color="black", fullscr=True)

#Starting stopwatch
stopwatch = core.Clock()

#Show the introdoction text in the window
msg = visual.TextStim(win, text = IntroText , color="#4287f5" )
msg.draw()
win.flip()
#Wait until any key is pressed
event.waitKeys()

#Show the instruction text in the window
msg = visual.TextStim(win, text = IntructionText , color="#4287f5")
msg.draw()
win.flip()
#Wait until any key is pressed
event.waitKeys()

#Running test story, word by word. 
for word in Listtest:
    msg = visual.TextStim(win, text = word)
    msg.draw()
    win.flip()
    #Creating key response for 'space' to loop and print word and 'q' to quit
    key = event.waitKeys(keyList = ["q","space"])
    if key[0] == "space":
        print(word)
    elif key[0] == "q":
        core.quit()
        print("quit")

 
#Show feedback text and wait until any key is pressed
msg = visual.TextStim(win, text = TestFeed, color="#4287f5")
msg.draw()
win.flip()
event.waitKeys()


#StoryA 
#If Story A is selected in the popup window run StoryA
if popup.data[3] =="StoryA":
    #Presenting Story A in a loop word by word by reading ListA
    for word in ListA:
        msg = visual.TextStim(win, text = word)
        msg.draw()
        win.flip()
        #Reset stopwatch evertime loop is run
        stopwatch.reset()
        #Creating key response
        key = event.waitKeys(keyList = ["q","space"])
        #collecting response/reading time
        Reading_time = stopwatch.getTime()
        print(Reading_time)
        print(word)
        #If response is'space' loop ListA and print word. If response is 'q' quit experiment
        if key[0] == "space":
            print(word) 
        elif key[0] == "q":
            core.quit()
            print("quit")
        #Placing the data in a logfile
        logfile=logfile.append({
        "ID": ID,  
        "Age": Age, 
        "Gender": Gender, 
        "Stimulus": word, 
        "Reading_time": Reading_time,
        "Condition": Condition}, ignore_index = True )

#StoryB
#If Story B is selected in the popup window run StoryB
if popup.data[3] =="StoryB":
    #Presenting Story b in a loop word by word by reading ListB
    for word in ListB:
        msg = visual.TextStim(win, text = word)
        msg.draw()
        win.flip()
        #Reset stopwatch evertime loop is run
        stopwatch.reset()
        #Creating key response
        key = event.waitKeys(keyList = ["q","space"])
        #collecting response/reading time
        Reading_time = stopwatch.getTime()
        print(Reading_time) 
        print(word)
        #If response is'space' loop ListB and print word. If response is 'q' quit experiment
        if key[0] == "space":
            print(word) 
        elif key[0] == "q":
            core.quit()
            print("quit")
        #Placing the data in a logfile
        logfile=logfile.append({
        "ID": ID,  
        "Age": Age, 
        "Gender": Gender,
        "Stimulus": word, 
        "Reading_time": Reading_time,
        "Condition": Condition}, ignore_index = True )


#Show final message
msg = visual.TextStim(win, text = ThankYou , color="#4287f5")
msg.draw()
win.flip()
#Wait until any key is pressed
event.waitKeys() 


#Save the logfile in the "logfiles"-folder with the name logfile_ followed by participant ID
logfile_name = "logfiles/logfile_{}.csv".format(ID)
logfile.to_csv(logfile_name)  


