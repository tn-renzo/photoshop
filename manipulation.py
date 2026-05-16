import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

"""
Notes:
    Numpy array: array[:, :, xxx]
     - channel 0 ... red
     - channel 1 ... green
     - channel 2 ... blue
"""

def load_image(image_path) -> np.ndarray:
    img = Image.open(image_path)
    return np.array(img)

def grayscale(image):
    pass

def invert(image):
    pass

def set_green(image: np.ndarray, rgb_value: int) -> np.ndarray:
    if rgb_value < 0 or rgb_value > 255:
        print("Invalid RGB Value")
        return image

    image[:, :, 1] = rgb_value
    return image

def set_red(image: np.ndarray, rgb_value: int) -> np.ndarray:
    if rgb_value < 0 or rgb_value > 255:
        print("Invalid RGB Value")
        return image

    image[:, : , 0] = rgb_value
    return image

def set_blue(image: np.ndarray, rgb_value: int) -> np.ndarray:
    if rgb_value < 0 or rgb_value > 255:
        print("Invalid RGB Value")
        return image

    image[:, :, 2] = rgb_value
    return image

def main() -> None:
    image_path: str = "images/example02.jpg"
    image_array = load_image(image_path)

   
    edit = image_array.copy()
    edit = set_green(edit, 34)
    edit = set_blue(edit, 84)
    plt.imshow(edit)
    plt.show()

if __name__ == '__main__':
    main()
