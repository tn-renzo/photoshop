import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def load_image(image_path) -> np.ndarray:
    img = Image.open(image_path)
    return np.array(img)

def grayscale(image):
    pass

def invert(image):
    pass

"""
    Numpy array: array[:, :, xxx]
     - channel 0 ... red
     - channel 1 ... green
     - channel 2 ... blue
"""
def set_green(image: np.ndarray, rgb_value: int) -> np.ndarray:
    if rgb_value < 0 or rgb_value < 255:
        print("Invalid RGB Value")
        # TODO: Add a return type or try/except for this


    image[:, :, 1] = rgb_value
    return image

def main() -> None:
    IMAGE_PATH: str = "images/example02.jpg" 
    image_array = load_image(IMAGE_PATH)

   
    edit = image_array.copy()
    edit = set_green(edit, 255)
    plt.imshow(edit)
    plt.show()
    
if __name__ == '__main__':
    main()
