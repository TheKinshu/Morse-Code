"""
    UI Class
    -------------------------
    This creates all the UI elements that is require to function

    by: (Kelvin) Chun Kit Cho
    May 4, 2021

"""
# Import class from different sources
from tkinter import *
from twilio.rest import Client
import data.converter as c
import pyperclip, os

# Global Variables
BACKGROUND_COLOR = "#B1DDC6"
LABELFONT = ("Serif", 15, "bold")
RESULTFONT = ("Serif", 15, "normal")
ACCOUNT_SID = os.getenv('TWILIO_SID')
AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')

# Defining the UI Class
class UI():
    # Initializing All the require variables to create and GUI
    def __init__(self) -> None:

        # Create the window panel
        self.window = Tk()
        self.convert = c.Converter()
        self.window.title("Morse Code Translator")
        self.window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

        # Background Image
        self.displayArea = PhotoImage(file="./images/card_front.png")

        # Canvas
        self.canvas = Canvas(width=600, height=394, highlightthickness=0, bg=BACKGROUND_COLOR)
        self.canvasImage = self.canvas.create_image(300, 197, image=self.displayArea)
        self.resultLabel = self.canvas.create_text(100, 60, text="Input Result:", font=LABELFONT)
        self.resultText = self.canvas.create_text(40, 100, text="", width=500,anchor='nw', font=RESULTFONT)
        self.canvas.grid(column=0, row=0, columnspan=2)

        # User input field labels
        self.inputLabel = Label(text="User Input:", bg=BACKGROUND_COLOR, anchor='w')
        self.inputLabel.grid(column=0,row=1)

        self.inputEntry = Entry(width=80)
        self.inputEntry.grid(column=1, row=1)

        self.numberLabel = Label(text="Phone Number:", bg=BACKGROUND_COLOR, anchor='w')
        self.numberLabel.grid(column=0,row=3)

        self.numberEntry = Entry(width=80)
        self.numberEntry.grid(column=1, row=3)

        # Radio button thats selects encode or decode
        self.radio_state = IntVar()
        self.encode = Radiobutton(text="Encode", value=1, variable=self.radio_state, bg=BACKGROUND_COLOR, highlightthickness=0)
        self.encode.grid(column=0,row=2)
        self.decode = Radiobutton(text="Decode", value=2, variable=self.radio_state, bg=BACKGROUND_COLOR)
        self.decode.grid(column=1, row=2)

        # Checkbox that allow user to text a speific user the decoded or encoded messages
        self.checked_state = IntVar()
        self.checkbox = Checkbutton(text="Text the number?",bg=BACKGROUND_COLOR, variable=self.checked_state)
        self.checkbox.grid(column=1, row=2, padx=(400,10))

        # Button that collects the data after clicking 
        self.submit = Button(text="Translate", width=80, command=self.translate)
        self.submit.grid(column=0,row=4, columnspan=3)
        self.window.mainloop()

    # Method/Function that translate the message from either morse-code to standard character or vice-versa
    def translate(self):
        # Get the variable information from the input fields
        userInput = self.inputEntry.get()
        translateType = self.radio_state.get()
        state = self.checked_state.get()
        # Check what user want to translate from and to
        if translateType == 1:
            # Clear the message input field
            self.inputEntry.delete(0, 'end')
            # Sends the message to the convert class and 
            code = self.convert.convert(userInput)
            message = []
            for c in code:
                message.append(" ".join(c))

            result = "\n".join(message)
            # Copy the message to your clipboard 
            pyperclip.copy(result)
            # Send information to display
            self.display(result)

        elif translateType == 2:
            # Clear the message input field
            self.inputEntry.delete(0, 'end')
            code = self.convert.decode(userInput)
            result = " ".join(code)
            # Send information to display
            self.display(result)
            # Copy the message to your clipboard 
            pyperclip.copy(result)

        # Check if user selected send text message
        if state == 1:
            # Check if the number input field is empty or is less than 10 number length
            if self.numberEntry.get() == "" and not len(self.numberEntry.get()) == 10:
                pass
            else:
                self.textNumber(result,self.numberEntry.get())
    
    # Changes the display text to the message that was inputted
    def display(self, message):
        self.canvas.itemconfig(self.resultText, text=message)
    
    # If user is checked send message to the reciever phone number
    def textNumber(self, message, number):
        client = Client(ACCOUNT_SID, AUTH_TOKEN)
        client.messages \
                    .create(
                        body="{}".format(message),
                        from_='+13472271948',
                        to=f'+1{number}'
                    )