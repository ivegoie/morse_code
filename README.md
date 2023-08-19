# Morse Code Encoder || Decoder

This is a simple Python application for encoding and decoding Morse code messages using a graphical user interface (GUI). It utilizes the PySide6 library for the GUI components.

![Morse Code](https://i.ibb.co/YZF1rDv/morse-code-decode-encode-showcase.png)

## Features

- Encode Messages: You can input text and encode it into Morse code.
- Decode Messages: You can input Morse code and decode it into text.
- Clipboard Integration: Easily copy the encoded or decoded message to your clipboard.

## Requirements
Before you can use this application, ensure that you have the following dependencies installed on your system:

- `Python` 3.x
- `PySide6` library
- `Playsound` library
- `Montserrat` font

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/ivegoie/climate_sense.git
   cd climate_sense
   ```

2. Install the required libraries using pip:
    ```bash
    pip install playsound PySide6
    ```
3. Run the main.py script:
    ```bash
    python main.py
    ```
## Usage

1. Encoding Messages:
    - Enter the text you want to encode into the "Message to Encode" input field.
    - Click the "Encode" button to convert the text to Morse code.
    - The encoded message will be displayed, and you can copy it to your clipboard using the "Copy Encoded Message" button.

2. Decoding Messages:
    - Enter the Morse code you want to decode into the "Morse Code to Decode" input field.
    - Click the "Decode" button to convert the Morse code to text.
    - The decoded message will be displayed, and you can copy it to your clipboard using the "Copy Decoded Message" button.

## License
This project is licensed under the [MIT License](LICENSE).