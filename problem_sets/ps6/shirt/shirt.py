import sys
from PIL import Image
from PIL import ImageOps

def main():
    return 

def check_args(arg):
    if len(arg) > 3:
        sys.exit('Too many arguments')
    elif len(arg) < 3:
        sys.exit('Too few arguments')
    try: 
        Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit('File does not exist') 

def shirt_pic(input_image, output_image):
    image1 = Image.open(input_image)
    image2 = output_image
    ImageOps.fit(image1)
    edit = image2.paste(image1)
    
    image1 = Image.SAVE(edit)
    
    

    
    


if __name__ == '__main__':
    main()