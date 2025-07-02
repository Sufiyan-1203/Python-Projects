# Steganography: Image Text Encoder & Decoder

## Overview
This project allows you to hide (encode) a secret text message inside an image and later extract (decode) it using Python and the Pillow library. The message is hidden in the least significant bits of the image's pixels.

## Features
- Encode a secret message into an image (supports PNG and other RGB/RGBA formats).
- Decode and reveal the hidden message from an image.
- Uses a binary EOF marker to indicate the end of the hidden message.
- Simple command-line interface.

## How to Run

### Prerequisites
- Python 3
- Pillow library  
  Install with:
  ```bash
  pip install pillow

## Encoding a Message
1. Place encode.py in your working directory.
2. Prepare an input image (e.g., input.png).
3. Run the script: python encode.py
4. Enter the input image path, output image path, and your secret message when prompted.
5. The output image will contain your hidden message.

## Decoding a Message
1. Place decode.py in your working directory.
2. Run the script: python decode.py
3. Enter the path to the image containing the hidden message (e.g., output.png).
3. The decoded message will be displayed.

## Example
# Encoding:
    Enter input image path (e.g., input.png): input.png
    Enter output image path (e.g., output.png): output.png
    Enter the secret message: Hello, world!
    Message encoded successfully into output.png
# Decoding:
    Enter image path to decode (e.g., output.png): output.png
    Decoded message: Hello, world!

## Notes
1. Only RGB or RGBA images are supported.
2. The image must be large enough to store the entire message.
3. The EOF marker used is 1111111111111110 (16 bits).

## License
    This project is open-source and free to use.

## Author
Created by **MOHAMMED SUFIYAN ALI**.

Enjoy hiding your messages!


