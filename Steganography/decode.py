from PIL import Image

def binary_to_text(binary):
    chars = [binary[i:i+8] for i in range(0, len(binary), 8)]
    message = ""
    for byte in chars:
        if byte == '11111110':
            break
        message += chr(int(byte, 2))
    return message

def decode_image(stego_image_path):
    image = Image.open(stego_image_path)

    if image.mode not in ('RGB', 'RGBA'):
        print("Only RGB or RGBA images are supported.")
        return

    pixels = list(image.getdata())
    binary_data = ""

    for pixel in pixels:
        for i in range(3):
            binary_data += str(pixel[i] & 1)

    hidden_message = binary_to_text(binary_data)
    print("Decoded message:", hidden_message)

# Usage
stego_image = input("Enter image path to decode (e.g., output.png): ")
decode_image(stego_image)
