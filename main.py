import string
import tkinter
from pathlib import Path
import json
import random
import logging
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

logging.basicConfig(level=logging.DEBUG)
def load_words():
    path = Path('words.json')

    try:
        contents = path.read_text()
    except FileNotFoundError:
        logging.warning("The File is not found")
        logging.debug("Thanks for using this program")
    else:
        data = json.loads(contents)
        words = [w.lower() for w in data['data']]
        return words

def random_word(words):
    return random.choice(words)


def start_game():

    def exit():
        root.destroy()

    root = Tk()
    root.geometry('1280x720')
    root.title('HANG MAN GAME')
    root.config(bg='#80c4b7')

    button_exit = tkinter.Button(master=root, text="Exit", command=exit,font=('Helveltica bold',20))
    button_exit.place(x=1150, y=15)

    canvas = Canvas(root,bd=0,highlightthickness=0,width=420,height=450)
    canvas.pack()

    images = [
        ImageTk.PhotoImage(Image.open("resources/Attempt0.png")),
        ImageTk.PhotoImage(Image.open("resources/Attempt1.png")),
        ImageTk.PhotoImage(Image.open("resources/Attempt2.png")),
        ImageTk.PhotoImage(Image.open("resources/Attempt3.png")),
        ImageTk.PhotoImage(Image.open("resources/Attempt4.png")),
        ImageTk.PhotoImage(Image.open("resources/Attempt5.png"))
    ]


    words = load_words()
    characters = list(string.ascii_lowercase) + ['0','1','2','3','4','5','6','7','8','9']
    attempts = 5
    warnings = 3

    if words != None:
        word = random_word(words)
        word_list = [l for l in word]
        guess_list= []
        for l in word_list:
            if(l == " "):
                guess_list.append(" ")
            else:
                guess_list.append("_")


        while attempts > 0:
            canvas.create_image(240,200,image=images[attempts])

            label_guesslist = tkinter.Label(master=root, text=" ".join(guess_list), bg='#80c4b7',
                                            font=('Helveltica bold', 40))
            label_guesslist.place(x=480, y=500)

            label_attempts = tkinter.Label(master=root, text=f"Attempts: {attempts}", bg='#80c4b7',
                                           font=('Helveltica bold', 20))
            label_attempts.place(x=10, y=10)

            label_warnings = tkinter.Label(master=root, text=f"Warnings: {warnings}", bg='#80c4b7',
                                           font=('Helveltica bold', 20))
            label_warnings.place(x=10, y=50)

            label_1 = tkinter.Label(master=root, text=f"Write a letter: ", bg='#80c4b7',
                                           font=('Helveltica bold', 20))
            label_1.place(x=10,y=650)


            def get_input():
                global input_character
                input_character = entry.get()
                input_character = input_character.lower()
                entry_var.set(1)

            entry_var = tkinter.IntVar()
            entry = tkinter.Entry(master=root, font=('Helveltica bold',20),width=2)
            entry.place(x=200,y=650)

            button_enter = tkinter.Button(master=root, text="Enter",font=('Helveltica bold',18),command=get_input)
            button_enter.place(x=250,y=650)
            root.update()
            root.wait_variable(entry_var)


            if input_character in characters:
                if input_character in word_list:
                    for i in range(len(word_list)):
                        if input_character == word_list[i]:
                            guess_list[i] = input_character



                    if '_' not in guess_list:
                        label_guesslist = tkinter.Label(master=root, text=" ".join(guess_list), bg='#80c4b7',
                                                        font=('Helveltica bold', 40))
                        label_guesslist.place(x=480, y=500)

                        messagebox.showinfo("Congratulations!", "You Win")

                        break

                else:
                    attempts -= 1

                characters.remove(input_character)

            else:
                warnings -= 1
                if warnings <0:
                    messagebox.showwarning("Warning!","You were warned.")
                    break

        if attempts <= 0:
            label_attempts = tkinter.Label(master=root, text=f"Attempts: {attempts}", bg='#80c4b7',
                                           font=('Helveltica bold', 20))
            label_attempts.place(x=10, y=10)
            canvas.create_image(240, 200, image=images[attempts])

            messagebox.showerror(":(","GAME OVER")

    root.mainloop()

start_game()


