import os
import time

from playsound import playsound

MORSE_DICT = {
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

text_message = "Test"
morse_message = " ".join(MORSE_DICT[char] for char in text_message.upper())


def play_morse_code(message):
    short_path = os.path.join("sounds", "short.mp3")
    long_path = os.path.join("sounds", "long.mp3")
    for char in message:
        if char == ".":
            playsound(short_path)
        elif char == "-":
            playsound(long_path)
        elif char == " ":
            time.sleep(0.2)
        elif char == "/":
            time.sleep(0.4)
        else:
            print("Invalid Characted detected!")


play_morse_code(morse_message)
