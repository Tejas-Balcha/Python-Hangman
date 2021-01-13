import tkinter as tk
from tkinter import *
import random

global guessesUsed
guessesUsed = 0
letterFit = False
counter = 0
guessedLetterList = []
guessedWordList = []
chosenWord = ""
chosenWordList = []
wordOptionList = ["eyes","pet","distance","night","pies","arithmetic","dress","start","science","attack","soap","seed","expansion","building","squirrel","thing","finger","passenger","snail","oil","dinner","secretary","record","sponge","shape","balance","riddle","rake","trip","face","chance","feeling","toothbrush","reward","toes","oatmeal","offer","anger","cobweb","laugh","cough","lamp","fowl","bed","partner","house","flesh","thrill","creator","women","income","advertisement","birth","mask","rod","jeans","current","bite","brother","grandmother","bulb","harmony","box","grass","meat","mint","flowers","range","toys","machine","men","alarm","vein","snakes","crib","end","muscle","railway","memory","flower","relation","grade","hour","bit","back","profit","daughter","land","shake","sea","hole","minute","amusement","impulse","cheese","spiders","grandfather","rose","weight","stone"]
chosenWord = wordOptionList[random.randint(0,99)]
chosenWord = chosenWord.upper()
for i in chosenWord:
    chosenWordList.append("*")
print(chosenWord)

HEIGHT = 800
WIDTH = 900
myBlue = '#80c1ff'
root = tk.Tk()

def guessLetterCommand():
    counter = -1
    letterFit = False
    if len(entry.get()) == 1:
        if entry.get().upper() in guessedLetterList:
            feedbackLabel.config(text = "You already guessed that letter",fg='red')
        else:
            feedbackLabel.config(text = "You guessed " + str(entry.get()).upper(),fg='green')
            guessedLetterList.append(entry.get().upper())
            guessedLetterList.sort()
            guessedLetterLabel.config(text=guessedLetterList)
            if entry.get().upper() in chosenWord:
                for i in chosenWord:
                    counter = counter + 1
                    if entry.get().upper() == i:
                        chosenWordList[counter] = entry.get().upper()
                        correctWordLabel.config(text=chosenWordList)
                        letterFit = True
                if chosenWordList.count("*") == 0:
                    feedbackLabel.config(text="You Guessed the Word")
                    letterButton.config(state="disabled")
                    wordButton.config(state="disabled")
            if letterFit == False:
                global guessesUsed
                guessesUsed = guessesUsed + 1
                if guessesUsed == 1:
                    canvas.create_image(300,30,anchor=N, image=img1)
                elif guessesUsed == 2:
                    canvas.create_image(300,30,anchor=N, image=img2)
                elif guessesUsed == 3:
                    canvas.create_image(300,30,anchor=N, image=img3)
                elif guessesUsed == 4:
                   canvas.create_image(300,30,anchor=N, image=img4)
                elif guessesUsed == 5:
                    canvas.create_image(300,30,anchor=N, image=img5)
                elif guessesUsed == 6:
                    canvas.create_image(300,30,anchor=N, image=imgF)
                    feedbackLabel.config(text="You Lost",fg='red')
                    letterButton.config(state="disabled")
                    wordButton.config(state="disabled")
    else:
        feedbackLabel.config(text = "Invalid Guess",fg='red')
def guessWordCommand():
    if len(entry.get()) > 0:
        if entry.get().upper() in guessedWordList:
            feedbackLabel.config(text = "You already guessed that word",fg='red')
        else:
            feedbackLabel.config(text = "You guessed " + str(entry.get().upper()),fg='green')
            guessedWordList.append(entry.get().upper())
            guessedWordList.sort()
            guessedWordLabel.config(text=entry.get().upper())
            if entry.get().upper() == chosenWord :
                correctWordLabel.config(text=chosenWord)
                feedbackLabel.config(text="You Guessed the Word")
                letterButton.config(state="disabled")
                wordButton.config(state="disabled")
            else:
                global guessesUsed
                guessesUsed = guessesUsed + 1
                if guessesUsed == 1:
                    canvas.create_image(300,30,anchor=N, image=img1)
                elif guessesUsed == 2:
                    canvas.create_image(300,30,anchor=N, image=img2)
                elif guessesUsed == 3:
                    canvas.create_image(300,30,anchor=N, image=img3)
                elif guessesUsed == 4:
                   canvas.create_image(300,30,anchor=N, image=img4)
                elif guessesUsed == 5:
                   canvas.create_image(300,30,anchor=N, image=img5)
                elif guessesUsed == 6:
                    canvas.create_image(300,30,anchor=N, image=imgF)
                    feedbackLabel.config(text="You Lost",fg='red')
                    letterButton.config(state="disabled")
                    wordButton.config(state="disabled")
    else:
        feedbackLabel.config(text = "Invalid Guess",fg='red')
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH,bg= myBlue)
canvas.pack()

imgF = PhotoImage(file="hangmanFinal.ppm")
img0 = PhotoImage(file="hangman0.ppm")
img1= PhotoImage(file="hangman1.ppm")
img2 = PhotoImage(file="hangman2.ppm")
img3= PhotoImage(file="hangman3.ppm")
img4 = PhotoImage(file="hangman4.ppm")
img5 = PhotoImage(file="hangman5.ppm")
canvas.create_image(300,30,anchor=N, image=img0)
#x=630, y=400

guessedLetterLabel = tk.Label(canvas, bg = 'white', font=40,text="Guessed Letters")
guessedLetterLabel.place(relx=0.6,rely=0.04,relwidth=0.35,relheight=0.22)
guessedWordLabel = tk.Label(canvas, bg = 'white', font=40,text="Last Guessed Word")
guessedWordLabel.place(relx=0.6,rely=0.31,relwidth=0.35,relheight=0.22)

frame = tk.Frame(root, bg= myBlue)
frame.place(relx=0.5,rely=0.55,relwidth=0.7,relheight=0.4,anchor='n')

correctWordLabel = tk.Label(frame,bg=myBlue,font=40,text=chosenWordList)
correctWordLabel.place(relx=0.5,rely=0.3,relwidth=1,relheight=0.1,anchor='n')

feedbackLabel = tk.Label(frame, bg = myBlue, font = 40, text = "")
feedbackLabel.place(relx=0.5,rely=0.45,relwidth=1,relheight=0.1,anchor='n')

entry = tk.Entry(frame, bg = 'white',font=40)
entry.place(relx=0.5,rely=0.6,relwidth=0.5,relheight=0.1,anchor='n')

letterButton = tk.Button(frame, text="Guess Letter",command = guessLetterCommand)
letterButton.place(relx=0.38,rely=0.75,relwidth=0.2,relheight=0.1,anchor='n')
wordButton = tk.Button(frame, text="Guess Word",command = guessWordCommand)
wordButton.place(relx=0.62,rely=0.75,relwidth=0.2,relheight=0.1,anchor='n')

root.mainloop()
