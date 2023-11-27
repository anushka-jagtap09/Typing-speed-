# from time import *
# import random as r
# def mistake(partest,usertest):
#
#     error=0
#     for i in range(len(partest)):
#         try:
#             if partest[i]!=usertest[i]:
#                 error+=1
#         except:
#             error+=1
#     return error
# def time_of_typing(s,e,w):
#     t_delay=e-s
#     t_round=round(t_delay,2)
#     speed=len(w)/t_round
#     return round(speed)
#
#
# test=["A paragram is self- contained unit","anushka is beautiful girl","khushi is smart girl"]
#
# test1=r.choice(test)
#
# print("******** Typing speed *********")
# print(test1)
# print()
# print()
# time_1=time()
# testinput=input("Enter:  ")
# time_2=time()
#
# print("speed : ",time_of_typing(time_1,time_2,testinput),"w/s")
# print("Error:  ", mistake(test1,testinput))

import tkinter as tk
import time

class TypingSpeedTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")

        self.text = "This is a simple typing speed test. Try to type this text as fast and accurately as possible."
        self.target_text = tk.StringVar(value=self.text)

        self.text_label = tk.Label(root, textvariable=self.target_text, wraplength=400, justify="left")
        self.text_label.pack(pady=20)

        self.entry = tk.Entry(root)
        self.entry.pack(pady=10)

        self.start_button = tk.Button(root, text="Start Test", command=self.start_test)
        self.start_button.pack()

        self.result_label = tk.Label(root, text="", font=("Arial", 12))
        self.result_label.pack(pady=10)

        self.start_time = 0

    def start_test(self):
        self.start_time = time.time()
        self.entry.config(state=tk.NORMAL)
        self.entry.delete(0, tk.END)
        self.entry.focus()
        self.start_button.config(state=tk.DISABLED)

    def calculate_speed(self, event):
        user_input = self.entry.get()
        elapsed_time = time.time() - self.start_time
        correct_chars = sum(1 for c1, c2 in zip(user_input, self.text) if c1 == c2)
        accuracy = (correct_chars / len(self.text)) * 100
        speed = (correct_chars / 5) / (elapsed_time / 60)  # Words per minute

        result = f"Speed: {speed:.2f} WPM | Accuracy: {accuracy:.2f}%"
        self.result_label.config(text=result)

        self.entry.config(state=tk.DISABLED)
        self.start_button.config(state=tk.NORMAL)

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTest(root)
    app.root.bind("<Return>", app.calculate_speed)  # Press Enter to calculate speed
    root.mainloop()
