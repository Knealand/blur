import os
import fleep
from PIL import Image
import argparse


def check_output_dir() -> bool:
    #TODO
    return True

def identify_file(content):
    try:
        info = fleep.get(content)
        ex = None
        if len(info.extension) > 0:
            ex = info.extension[0]
        return ex
    except Exception as e:
        print(f"An error occurred: {e}")
    
def embed_jpg(file_path, image_path):
    file_content = bytearray()
    try:
        with open(file_path, 'rb') as file:
            file_content = file.read()
        print("File Content as String:")
        print(file_content)
    except FileNotFoundError:
        print(f"The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    
    try:
        temp_path = os.getcwd() + "/output/blur.jpg"
        original_image = Image.open(image_path)

        # Save a copy of the image
        original_image.save(temp_path)

        with open(temp_path, 'ab') as image:
            image.write(file_content)
        

    except Exception as e:
        print(f"An error occurred: {e}")
    except FileNotFoundError:
        print(f"The image '{image_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def decode_jpg(image_path):
    try:
        with open(image_path, 'rb') as file:
            content = file.read()  
            jpg_offest = content.index(bytes.fromhex('FFD9'))
            file.seek(jpg_offest + 2)
            data = file.read()
            extension = identify_file(data)

            temp_path = os.getcwd() + "/output/blur_decode."

            if extension is not None:
                temp_path += extension
               
            else:
                print("Unable to detect file type")
                print("outputing content to .txt file")
            temp_path += "txt"
            with open(temp_path, 'wb') as decoded_file:
                    decoded_file.write(data)
    except Exception as e:
        print(f"An error occurred: {e}")
    except FileNotFoundError:
        print(f"The image '{image_path}' was not found.")

def embed_text(image_path, data):
    try:
        temp_path = os.getcwd() + "/output/blur.jpg"
        original_image = Image.open(image_path)

        # Save a copy of the image
        original_image.save(temp_path)

        with open(temp_path, 'ab') as image:
            image.write(bytearray(data, 'utf-8'))
        

    except Exception as e:
        print(f"An error occurred: {e}")
    except FileNotFoundError:
        print(f"The image '{image_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def validate_file_path(file_path):
    file_path = os.path.abspath(file_path)
    if not os.path.isfile(file_path):
        raise argparse.ArgumentTypeError(f"{file_path} is not a valid file.")
    else:
        return file_path
    
def validate_image(image_path):
    try:
        image_path = os.path.abspath(image_path)
        with Image.open(image_path) as img:
            img.verify()  # Attempt to open and verify the image
        return image_path
    except Exception as e:
        raise argparse.ArgumentTypeError(f"{image_path} is not a valid image file. Error: {e}")
    

def main():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument('-f', '--file', type=validate_file_path, help='Input file to embed path')
    parser.add_argument('-i', '--image',type=validate_image, help='image host path')
    parser.add_argument('-t', '--text', help='Text to embed')
    parser.add_argument('-d', '--decode', action='store_true', help='decode a given image')
    
    args = parser.parse_args()

    input_file = args.file
    text_to_embed = args.text
    image_file = args.image
    decode_mode = args.decode

    if decode_mode:
        print("entering decode mode...")
        if image_file:
            decode_jpg(image_file)
        else:
            print("An image path -i is required.")
            exit()
    else:
        if image_file:
            if input_file:
                print("embeding file...")
                embed_jpg(input_file, image_file)
            elif text_to_embed:
                print("embeding text...")
                embed_text(image_file, text_to_embed)
            else:
                print("No file path or text, -t or -f is required.")
                exit()  
        else:
            print("An image path -i is required.")
            exit()


if __name__ == '__main__':
    main()