from PIL import Image

def text_to_binary(text):
    binary = ''.join(format(ord(c), '08b') for c in text)
    binary += '1111111111111110'  # EOF marker
    return binary

def encode_image(input_image_path, output_image_path):
    image = Image.open(input_image_path)
    secret_text = input("Enter the secret message: ")
    binary_data = text_to_binary(secret_text)

    if image.mode not in ('RGB', 'RGBA'):
        print("Only RGB or RGBA images are supported.")
        return

    pixels = list(image.getdata())
    new_pixels = []
    data_index = 0

    for pixel in pixels:
        pixel = list(pixel)
        for i in range(3):
            if data_index < len(binary_data):
                pixel[i] = pixel[i] & ~1 | int(binary_data[data_index])
                data_index += 1
        new_pixels.append(tuple(pixel))

    image.putdata(new_pixels)
    image.save(output_image_path)
    print("Message encoded successfully into", output_image_path)

# Usage
input_image = input("Enter input image path (e.g., input.png): ")
output_image = input("Enter output image path (e.g., output.png): ")
encode_image(input_image, output_image)
