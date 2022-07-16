import time
from random import randint
import tkinter as tk

texts = ["Removing pollutants from wastewater to render it safe for drinking is an industrial scale process. \n"
         "Various methods are used in treating including physical and chemical processes. Chemicals are used in the \n"
         "treatment of wastewater – to restore it to a safe state.\n",
         "In this day and age when crisis seems to strike anywhere, there's no better way to stay safe and secure than \n"
         "learning how to save money. Experts agree that no matter how one looks at it, there will be always ways to \n"
         "save money if the person has the will do so.\n",
         "Being emotionally healthy does not imply that one is happy all the time. It means you are well aware of \n"
         "your emotions. You can deal with it, whether they are positive or negative.Key Facts of WHO states that \n"
         "the effects of not treating adolescent mental health issues extend to adulthood, impairing both physical\n "
         "and psychological health, and restricting opportunities to live a meaningful life as ad\n"
         ]
random_text = texts[randint(0, 2)]
character = len(random_text)
st_time = 1

root = tk.Tk()
root.title('Type Testing')
root.geometry('1530x500')


class TypeSpeed:
    time = 0
    end_time = 0

    def __init__(self):
        self.time = time.time()
        print(self.time)

    def loop_quit(self):
        self.end_time = time.time()


def TempFun(m):
    global st_time
    if m == "start":
        st_time = time.time()
    if m == "end":
        if st_time == 1:
            text_label = tk.Label(root, text='First click on start button')
            text_label.grid(row=9, column=1)
        end_time = time.time()
        time_taken = end_time - st_time
        text_label = tk.Label(root, text=f'Time taken was {time_taken} seconds and wpm is {(character/5)/(time_taken/60)}', font=("Times", 24))
        text_label.grid(row=9, column=1)
        st_time = 1


text_label = tk.Label(root, text=random_text, font=("Times", 24))
text_label.grid(row=2, column=1, padx=40, pady=40)

text = tk.Entry(root, width=150)
text.config(justify='center')
text.grid(row=4, column=1)

start_button = tk.Button(root, text='Start', command=lambda m="start": TempFun(m))
start_button.grid(row=5, column=1)

submit_button = tk.Button(root, text='Submit', command=lambda m="end": TempFun(m))
submit_button.grid(row=7, column=1)

root.mainloop()

