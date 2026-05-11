import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

class EditedImage:
    def __init__(self, path):
        self.path = path
        self.image: np.ndarray
        self.load_image()

    def load_image(self):
        img = Image.open(self.path).convert("RGB")
        self.image = np.array(img)

    def set_red(self, r):
        self.image[:, :, 0] = r

    def set_green(self, g):
        self.image[:, :, 1] = g

    def set_blue(self, b):
        self.image[:, :, 2] = b

    def return_img(self):
        return self.image

"""
    Numpy array: array[:, :, xxx]
     - channel 0 ... red
     - channel 1 ... green
     - channel 2 ... blue
"""

def main() -> None:
    image = EditedImage(path="images/example02.jpg")

    image.set_blue(255)
    image.set_red(255)
    image.set_green(255)

    plt.imshow(image.return_img())
    plt.show()

if __name__ == '__main__':
    main()
