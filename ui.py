from tkinter import *
from twilio.rest import Client
import data.converter as c
import pyperclip, os

BACKGROUND_COLOR = "#B1DDC6"
LABELFONT = ("Serif", 15, "bold")
RESULTFONT = ("Serif", 15, "normal")
ACCOUNT_SID = os.getenv('TWILIO_SID')
AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')

class UI():
    def __init__(self) -> None:
        self.window = Tk()
        self.convert = c.Converter()
        self.window.title("Morse Code Translator")
        self.window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
        self.displayArea = PhotoImage(file="./images/card_front.png")

        self.canvas = Canvas(width=600, height=394, highlightthickness=0, bg=BACKGROUND_COLOR)
        self.canvasImage = self.canvas.create_image(300, 197, image=self.displayArea)
        self.resultLabel = self.canvas.create_text(100, 60, text="Input Result:", font=LABELFONT)
        self.resultText = self.canvas.create_text(40, 100, text="", width=500,anchor='nw', font=RESULTFONT)
        self.canvas.grid(column=0, row=0, columnspan=2)

        self.inputLabel = Label(text="User Input:", bg=BACKGROUND_COLOR, anchor='w')
        self.inputLabel.grid(column=0,row=1)

        self.inputEntry = Entry(width=80)
        self.inputEntry.grid(column=1, row=1)

        self.numberLabel = Label(text="Phone Number:", bg=BACKGROUND_COLOR, anchor='w')
        self.numberLabel.grid(column=0,row=3)

        self.numberEntry = Entry(width=80)
        self.numberEntry.grid(column=1, row=3)

        self.radio_state = IntVar()
        self.encode = Radiobutton(text="Encode", value=1, variable=self.radio_state, bg=BACKGROUND_COLOR, highlightthickness=0)
        self.encode.grid(column=0,row=2)
        self.decode = Radiobutton(text="Decode", value=2, variable=self.radio_state, bg=BACKGROUND_COLOR)
        self.decode.grid(column=1, row=2)

        self.checked_state = IntVar()
        self.checkbox = Checkbutton(text="Text the number?",bg=BACKGROUND_COLOR, variable=self.checked_state)
        self.checkbox.grid(column=1, row=2, padx=(400,10))

        self.submit = Button(text="Translate", width=80, command=self.translate)
        self.submit.grid(column=0,row=4, columnspan=3)
        self.window.mainloop()

    def translate(self):
        userInput = self.inputEntry.get()
        translateType = self.radio_state.get()
        state = self.checked_state.get()
        if translateType == 1:
            self.inputEntry.delete(0, 'end')
            code = self.convert.convert(userInput)
            message = []
            for c in code:
                message.append(" ".join(c))

            result = "\n".join(message)
            pyperclip.copy(result)
            self.display(result)

        elif translateType == 2:
            self.inputEntry.delete(0, 'end')
            code = self.convert.decode(userInput)
            result = " ".join(code)
            self.display(result)
            pyperclip.copy(result)

        if state == 1:
            if self.numberEntry.get() == "" and not len(self.numberEntry.get()) == 10:
                print("yes")
            else:
                self.textNumber(result,self.numberEntry.get())
    
    def display(self, message):
        self.canvas.itemconfig(self.resultText, text=message)
        
    def textNumber(self, message, number):
        client = Client(ACCOUNT_SID, AUTH_TOKEN)
        client.messages \
                    .create(
                        body="{}".format(message),
                        from_='+13472271948',
                        to=f'+1{number}'
                    )