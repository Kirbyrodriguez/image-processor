import cmpt120imageProj
import cmpt120imageManip
import tkinter.filedialog
import pygame
import os
os.environ["SDL_VIDEODRIVER"] = "dummy"
pygame.init()

# list of system options
system = [
            "Q: Quit",
            "O: Open image",
            "R: Reload image",
            "S: Save image"
         ]

# list of basic operation options
basic = [
          "1: Switch to Intermeidate Functions",
          "2: Switch to Advanced Functions"
         ]

# list of intermediate operation options
intermediate = [
                  "1: Switch to Basic Functions",
                  "2: Switch to Advanced Functions"
                 ]

# list of advanced operation options
advanced = [
                "1: Switch to Basic Functions",
                "2: Switch to Intermediate Functions"
             ]

# a helper function that generates a list of strings to be displayed in the interface
def generateMenu(state):
    """
    Input:  state - a dictionary containing the state values of the application
    Returns: a list of strings, each element represets a line in the interface
    """
    menuString = ["Welcome to CMPT 120 Image Processer!"]
    menuString.append("") # an empty line
    menuString.append("Choose the following options:")
    menuString.append("") # an empty line
    menuString += system
    menuString.append("") # an empty line

    # build the list differently depending on the mode attribute
    if state["mode"] == "basic":
        menuString.append("--Basic Mode--")
        menuString += basic
        menuString.append("")
        menuString.append("3. Invert the image")
        menuString.append("4. Flip horizental")
        menuString.append("5. Flip vertical")

    elif state["mode"] == "intermediate":
        menuString.append("--Intermediate Mode--")
        menuString += intermediate
        menuString.append("")
        menuString.append("3. Remove red channel")
        menuString.append("4. Remove green channel")
        menuString.append("5. Remvove blue channel")
        menuString.append("6. Convert to grayscale")
        menuString.append("7. Apply Sepia filter")
        menuString.append("8. Decrease brightness")
        menuString.append("9. Increase brightness")

    elif state["mode"] == "advanced":
        menuString.append("--Advanced Mode--")
        menuString += advanced
        menuString.append("")
        menuString.append("3. Rotate left")
        menuString.append("4. Rotate right")
        menuString.append("5. Pixelate")
        menuString.append("6. Binarize")

    else:
        menuString.append("Error: Unknown mode!")

    return menuString

# a helper function that returns the result image as a result of the operation chosen by the user
# it also updates the state values when necessary (e.g, the mode attribute if the user switches mode)
def handleUserInput(state, img):
    """
        Input:  state - a dictionary containing the state values of the application
                img - the 2d array of RGB values to be operated on
        Returns: the 2d array of RGB vales of the result image of an operation chosen by the user
    """
    userInput = state["lastUserInput"].upper()
    # handle the system functionalities
    if userInput.isalpha(): # check if the input is an alphabet
        print("Log: Doing system functionalities " + userInput)
        if userInput == "Q":
            print("Log: Quitting...")
        # ***add the rest to handle other system functionalities***
        elif userInput == "O":
            tkinter.Tk().withdraw()
            openFilename = tkinter.filedialog.askopenfilename()
            img = cmpt120imageProj.getImage(openFilename)
            cmpt120imageProj.showInterface(img, "Image", generateMenu(appStateValues))
            appStateValues["lastOpenFilename"] = openFilename
        elif userInput == "R":
            img = cmpt120imageProj.getImage(appStateValues["lastOpenFilename"])
            cmpt120imageProj.showInterface(img, "Image", generateMenu(appStateValues))
        elif userInput == "S":
            tkinter.Tk().withdraw()
            saveFilename = tkinter.filedialog.asksaveasfilename()
            cmpt120imageProj.saveImage(img, saveFilename)
            appStateValues["lastSaveFilename"] = saveFilename
            cmpt120imageProj.showInterface(img, "Image", generateMenu(appStateValues))
            #FIX THIS


    # or handle the manipulation functionalities based on which mode the application is in
    elif userInput.isdigit(): # has to be a digit for manipulation options
        print("Log: Doing manipulation functionalities " + userInput)
        # ***add the rest to handle other manipulation functionalities***
        if appStateValues["mode"] == "basic":
            if userInput == "1":
                state["mode"] = "intermediate"
                cmpt120imageProj.showInterface(img, "Intermediate", generateMenu(appStateValues))
            elif userInput == "2":
                state["mode"] = "advanced"
                cmpt120imageProj.showInterface(img, "Advanced", generateMenu(appStateValues))
            elif userInput == "3":
                img = cmpt120imageManip.invert(img)
                cmpt120imageProj.showInterface(img, "Invert", generateMenu(appStateValues))
            elif userInput == "4":
                img = cmpt120imageManip.fliph(img)
                cmpt120imageProj.showInterface(img, "Flipped Horizental", generateMenu(appStateValues))
            elif userInput == "5":
                img = cmpt120imageManip.flipv(img)
                cmpt120imageProj.showInterface(img, "Flipped Vertical", generateMenu(appStateValues))

        elif appStateValues["mode"] == "intermediate":
            if userInput == "1":
                state["mode"] = "basic"
                cmpt120imageProj.showInterface(img, "Basic", generateMenu(appStateValues))
            elif userInput == "2":
                state["mode"] = "advanced"
                cmpt120imageProj.showInterface(img, "Advanced", generateMenu(appStateValues))
            elif userInput == "3":
                img = cmpt120imageManip.removered(img)
                cmpt120imageProj.showInterface(img, "Remove Red", generateMenu(appStateValues))
            elif userInput == "4":
                img = cmpt120imageManip.removegreen(img)
                cmpt120imageProj.showInterface(img, "Remove Green", generateMenu(appStateValues))
            elif userInput == "5":
                img = cmpt120imageManip.removeblue(img)
                cmpt120imageProj.showInterface(img, "Remove Blue", generateMenu(appStateValues))
            elif userInput == "6":
                img = cmpt120imageManip.grayscale(img)
                cmpt120imageProj.showInterface(img, "Grayscale", generateMenu(appStateValues))
            elif userInput == "7":
                img = cmpt120imageManip.sepia(img)
                cmpt120imageProj.showInterface(img, "Sepia", generateMenu(appStateValues))
            elif userInput == "8":
                img = cmpt120imageManip.dbrightness(img)
                cmpt120imageProj.showInterface(img, "Decrease Brightness", generateMenu(appStateValues))
            elif userInput == "9":
                img = cmpt120imageManip.ibrightness(img)
                cmpt120imageProj.showInterface(img, "Increase Brightness", generateMenu(appStateValues))

        elif appStateValues["mode"] == "advanced":
            if userInput == "1":
                state["mode"] = "basic"
                cmpt120imageProj.showInterface(img, "Basic", generateMenu(appStateValues))
            elif userInput == "2":
                state["mode"] = "intermediate"
                cmpt120imageProj.showInterface(img, "Intermediate", generateMenu(appStateValues))
            elif userInput == "3":
                img = cmpt120imageManip.rotateleft(img)
                cmpt120imageProj.showInterface(img, "Rotate Left", generateMenu(appStateValues))
            elif userInput == "4":
                img = cmpt120imageManip.rotateright(img)
                cmpt120imageProj.showInterface(img, "Rotate Right", generateMenu(appStateValues))
            elif userInput == "5":
                img = cmpt120imageManip.pixelate(img)
                cmpt120imageProj.showInterface(img, "Pixelate", generateMenu(appStateValues))
            elif userInput == "6":
                img = cmpt120imageManip.binarize(img)
                cmpt120imageProj.showInterface(img, "Binarize", generateMenu(appStateValues))

    else: # unrecognized user input
            print("Log: Unrecognized user input: " + userInput)
    return img


# use a dictionary to remember several state values of the application
appStateValues = {
                    "mode": "basic",
                    "lastOpenFilename": "",
                    "lastSaveFilename": "",
                    "lastUserInput": ""
                 }

currentImg = cmpt120imageProj.createBlackImage(600, 400) # create a default 600 x 400 black image
cmpt120imageProj.showInterface(currentImg, "No Image", generateMenu(appStateValues)) # note how it is used

# ***this is the event-loop of the application. Keep the remainder of the code unmodified***
keepRunning = True
# a while-loop getting events from pygame
while keepRunning:
    ### use the pygame event handling system ###
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            appStateValues["lastUserInput"] = pygame.key.name(event.key)
            # prepare to quit the loop if user inputs "q" or "Q"
            if appStateValues["lastUserInput"].upper() == "Q":
                keepRunning = False
            # otherwise let the helper function handle the input
            else:
                currentImg = handleUserInput(appStateValues, currentImg)
        elif event.type == pygame.QUIT: #another way to quit the program is to click the close botton
            keepRunning = False

# shutdown everything from the pygame package
pygame.quit()

print("Log: Program Quit")