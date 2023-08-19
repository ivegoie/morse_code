import pyttsx3


class Decoder:
    def __init__(self):
        self.MORSE_DICT = {
            ".-": "A",
            "-...": "B",
            "-.-.": "C",
            "-..": "D",
            ".": "E",
            "..-.": "F",
            "--.": "G",
            "....": "H",
            "..": "I",
            ".---": "J",
            "-.-": "K",
            ".-..": "L",
            "--": "M",
            "-.": "N",
            "---": "O",
            ".--.": "P",
            "--.-": "Q",
            ".-.": "R",
            "...": "S",
            "-": "T",
            "..-": "U",
            "...-": "V",
            ".--": "W",
            "-..-": "X",
            "-.--": "Y",
            "--..": "Z",
            "-----": "0",
            ".----": "1",
            "..---": "2",
            "...--": "3",
            "....-": "4",
            ".....": "5",
            "-....": "6",
            "--...": "7",
            "---..": "8",
            "----.": "9",
            ".-.-.-": ".",
            "--..--": ",",
            "..--..": "?",
            ".----.": "'",
            "-.-.--": "!",
            "-..-.": "/",
            "-.--.": "(",
            "-.--.-": ")",
            ".-...": "&",
            "---...": ":",
            "-.-.-.": ";",
            "-...-": "=",
            ".-.-.": "+",
            "-....-": "-",
            "..--.-": "_",
            ".-..-.": '"',
            "...-..-": "＄",
            ".--.-.": "@",
            "/": " ",
        }

    def morse_to_chars(self, message):
        words = message.split(" / ")
        plain_message = []
        for word in words:
            chars = word.split(" ")
            for char in chars:
                plain_message.append(self.MORSE_DICT.get(char, ""))
            plain_message.append(" ")

        self.text_message = "".join(plain_message)
        print(self.text_message)

        return self.text_message.lower().capitalize()
