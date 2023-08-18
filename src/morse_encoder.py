import os
import time

from playsound import playsound


class Encoder:
    def __init__(self):
        self.MORSE_DICT = {
            "A": ".-",
            "B": "-...",
            "C": "-.-.",
            "D": "-..",
            "E": ".",
            "F": "..-.",
            "G": "--.",
            "H": "....",
            "I": "..",
            "J": ".---",
            "K": "-.-",
            "L": ".-..",
            "M": "--",
            "N": "-.",
            "O": "---",
            "P": ".--.",
            "Q": "--.-",
            "R": ".-.",
            "S": "...",
            "T": "-",
            "U": "..-",
            "V": "...-",
            "W": ".--",
            "X": "-..-",
            "Y": "-.--",
            "Z": "--..",
            "0": "-----",
            "1": ".----",
            "2": "..---",
            "3": "...--",
            "4": "....-",
            "5": ".....",
            "6": "-....",
            "7": "--...",
            "8": "---..",
            "9": "----.",
            ".": ".-.-.-",
            ",": "--..--",
            "?": "..--..",
            "'": ".----.",
            "!": "-.-.--",
            "/": "-..-.",
            "(": "-.--.",
            ")": "-.--.-",
            "&": ".-...",
            ":": "---...",
            ";": "-.-.-.",
            "=": "-...-",
            "+": ".-.-.",
            "-": "-....-",
            "_": "..--.-",
            '"': ".-..-.",
            "＄": "...-..-",
            "@": ".--.-.",
            " ": "/",
        }

        self.short_path = os.path.join("src", "sounds", "short.mp3")
        self.long_path = os.path.join("src", "sounds", "long.mp3")

    def play_morse_code(self, message):
        self.morse_message = " ".join(self.MORSE_DICT[char] for char in message.upper())

        for char in self.morse_message: 
            if char == ".":
                playsound(self.short_path)
            elif char == "-":
                playsound(self.long_path)
            elif char == " ":
                time.sleep(0.2)
            elif char == "/":
                time.sleep(0.4)
            else:
                print("Invalid Character detected!")

        return self.morse_message
