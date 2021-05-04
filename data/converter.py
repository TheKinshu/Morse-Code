import data.morse_code as morse

class Converter():
    def __init__(self) -> None:
        self.alphaKey = [key for key in morse.morse_code_alpha.keys()]
        self.alphaList = [value for value in morse.morse_code_alpha.values()]

        self.numKey = [key for key in morse.morse_code_num.keys()]
        self.numList = [value for value in morse.morse_code_num.values()]

        self.puncKey = [key for key in morse.morse_code_punc.keys()]
        self.puncList = [value for value in morse.morse_code_punc.values()]

    def decode(self, code):

        #···· · ·−·· ·−·· −−−
        list = code.split()
        message = []

        for char in list:
            if char in self.alphaList:
                index = self.alphaList.index(char)
                message.append(self.alphaKey[index])
            elif char in self.numList:
                index = self.numList.index(char)
                message.append(self.numKey[index])
            elif char in self.puncList:
                index = self.puncList.index(char)
                message.append(self.puncKey[index])

        return message

    def convert(self, text):
        message = []
        code = []
        for char in text:
            if char.isnumeric():
                code.append(morse.morse_code_num[char])
            elif char.isalpha():
                code.append(morse.morse_code_alpha[char.lower()])
            elif char in self.puncKey:
                code.append(morse.morse_code_punc[char])                
            else:
                message.append(code)
                code = []
        if code in message:
            message.append(" ")
        else:
            message.append(code)
        return message