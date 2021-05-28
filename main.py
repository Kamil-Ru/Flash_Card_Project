from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = None
list_to_learn_word = None

try:
    file = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    file = pandas.read_csv("data/french_words.csv")
finally:
    list_to_learn_word = file.to_dict(orient="records")
    print(list_to_learn_word)


# --------------------------------------------- FUNCTION - NEW WORD ----------------------------------- #

def new_word():
    global current_card, filip_timer
    window.after_cancel(filip_timer)
    current_card = random.choice(list_to_learn_word)
    print(current_card)
    french_word = current_card["French"]
    canvas.itemconfig(canvas_language, text="French", fill='black')
    canvas.itemconfig(canvas_word, text=french_word, fill='black')

    canvas.itemconfig(canvas_image, image=card_front_image)
    filip_timer = window.after(3000, card_back)


# --------------------------------------------- FUNCTION - SHOW BACK CARD ----------------------------- #
def card_back():
    english_word = current_card["English"]
    canvas.itemconfig(canvas_language, text="English", fill='white')
    canvas.itemconfig(canvas_word, text=english_word, fill='white')
    canvas.itemconfig(canvas_image, image=card_back_image)


# ------------------------------------- FUNCTION - REMOVE WORD FROM CSV ----------------------------- #
def remove_word():
    global list_to_learn_word
    list_to_learn_word.remove(current_card)
    file_update = pandas.DataFrame(list_to_learn_word)
    file_update.to_csv("data/words_to_learn.csv", index=False)
    new_word()


# --------------------------------------------- UI  --------------------------------------------- #

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
filip_timer = window.after(3000, card_back)

# Canvas - main
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front_image)

canvas.grid(column=0, row=0, columnspan=2)

canvas_language = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
canvas_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))

# Buttom 1 - wrong
button_wrong_image = PhotoImage(file="images/wrong.png")
button_wrong = Button(image=button_wrong_image, highlightthickness=0, relief=FLAT, bg=BACKGROUND_COLOR,
                      command=new_word)
button_wrong.grid(column=0, row=1)

# Buttom 2 - right
button_right_image = PhotoImage(file="images/right.png")
button_right = Button(image=button_right_image, highlightthickness=0, relief=FLAT, bg=BACKGROUND_COLOR,
                      command=remove_word)
button_right.grid(column=1, row=1)
new_word()

window.mainloop()
