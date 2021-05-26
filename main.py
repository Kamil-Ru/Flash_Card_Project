from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
GLOBAL_dict_word = None

# try:
file = pandas.read_csv("data/french_words.csv")
# except FileNotFoundError:

# french_words.csv
# words_to_learn.csv

file_dict = file.to_dict(orient="records")




# --------------------------------------------- FUNCTION --------------------------------------------- #




# --------------------------------------------- FUNCTION - NEW WORD ----------------------------------- #

def new_word():
    global GLOBAL_dict_word
    GLOBAL_dict_word = random.choice(file_dict)
    french_word = GLOBAL_dict_word["French"]
    canvas.itemconfig(canvas_language, text="French", fill='black')
    canvas.itemconfig(canvas_word, text=french_word, fill='black')

    canvas.itemconfig(canvas_image, image=card_front_image)
    widow.after(3000, card_back)

# --------------------------------------------- FUNCTION - SHOW BACK CARD ----------------------------- #

def card_back():
    english_word = GLOBAL_dict_word["English"]
    canvas.itemconfig(canvas_language, text="English", fill='white')
    canvas.itemconfig(canvas_word, text=english_word, fill='white')
    canvas.itemconfig(canvas_image, image=card_back_image)





# --------------------------------------------- UI  --------------------------------------------- #

widow = Tk()
widow.title("Flashy")
widow.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Canvas _ main
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front_image)

canvas.grid(column=0, row=0, columnspan=2)

canvas_language = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
canvas_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))



# Bottom_1 - X (wrong)
button_wrong_image = PhotoImage(file="images/wrong.png")
button_wrong = Button(image=button_wrong_image,highlightthickness=0, relief=FLAT, bg=BACKGROUND_COLOR, command=new_word)
button_wrong.grid(column=0, row=1)

# Bottom_2 - X (right)
button_right_image = PhotoImage(file="images/right.png")
button_right = Button(image=button_right_image,highlightthickness=0, relief=FLAT, bg=BACKGROUND_COLOR, command=new_word)
button_right.grid(column=1, row=1)
new_word()



widow.after(3000, card_back)











widow.mainloop()