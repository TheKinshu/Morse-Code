"""
    Converter Class
    ---------------
    This class handles all the conversion from text to morse and vice-versa

    By: (Kelvin) Chun Kit Cho
    May 4, 2021
"""

# Importing the morse code data
import data.morse_code as morse

# Creating the Converter class
class Converter():
    # Initializing the variable for the class
    def __init__(self) -> None:
        self.alphaKey = [key for key in morse.morse_code_alpha.keys()]
        self.alphaList = [value for value in morse.morse_code_alpha.values()]

        self.numKey = [key for key in morse.morse_code_num.keys()]
        self.numList = [value for value in morse.morse_code_num.values()]

        self.puncKey = [key for key in morse.morse_code_punc.keys()]
        self.puncList = [value for value in morse.morse_code_punc.values()]

    # Decoding the message that was sent from the user
    def decode(self, code):
        list = code.split()
        message = []
        # Loops through the message and decode each section of the morse code
        for char in list:
            # Check if character is a alphabet
            if char in self.alphaList:
                index = self.alphaList.index(char)
                message.append(self.alphaKey[index])
            # Check if character is a number
            elif char in self.numList:
                index = self.numList.index(char)
                message.append(self.numKey[index])
            # Check if character is a punctuation
            elif char in self.puncList:
                index = self.puncList.index(char)
                message.append(self.puncKey[index])
        # Returning the result
        return message

    # Encoding the message that was sent from the user
    def convert(self, text):
        message = []
        code = []
        # Loops through the message and convert each character to a valid morse-code
        for char in text:
            # Check if character is a number
            if char.isnumeric():
                code.append(morse.morse_code_num[char])
            # Check if character is a alphabet
            elif char.isalpha():
                code.append(morse.morse_code_alpha[char.lower()])
            # Check if character is a punctuation
            elif char in self.puncKey:
                code.append(morse.morse_code_punc[char])   
            # If character could not be found it will end the word and start a new word             
            else:
                message.append(code)
                code = []
        # Check if last code was in the message 
        if code in message:
            # If the code is in the message end the message
            message.append(" ")
        else:
            # If the code is not in the message end it to the end of the message
            message.append(code)
        # Return the result of the conversion
        return message