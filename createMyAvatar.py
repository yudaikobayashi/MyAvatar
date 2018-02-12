import sys
import numpy as np
import cv2

def main():
    """This program will create my avatar image."""
    if len(sys.argv) != 3:
        print("Usage: python3", sys.argv[0], "<output.png> < size>")
        sys.exit(1)
    if getExtension(sys.argv[1]) != "png":
        print("Specify .png files.")
        sys.exit(1)

    try:
        size = int(sys.argv[2])
        if size % 8 != 0:
            print("Specify size in multiple of 8.")
            sys.exit(1)
    except ValueError:
        print("Enter size in an integer.")
        sys.exit(1)

    img = np.zeros((size,size,3))

    # Forehead
    for i in range(size // 4):
        for j in range(size):
            img[i,j] = [0,0,255]

    # Upper Glasses
    for i in range(size // 4, size * 3 // 8):
        for j in range(size * 3 // 8):
            img[i,j] = [0,0,0]
        for j in range(size * 3 // 8, size * 5 // 8):
            img[i,j] = [0,0,255]
        for j in range(size * 5 // 8, size):
            img[i,j] = [0,0,0]

    # Middle Glasses
    for i in range(size * 3 // 8, size // 2):
        for j in range(size // 8):
            img[i,j] = [0,0,0]
        for j in range(size // 8, size // 4):
            img[i,j] = [0,0,255]
        for j in range(size // 4, size * 3 // 4):
            img[i,j] = [0,0,0]
        for j in range(size * 3 // 4, size * 7 // 8):
            img[i,j] = [0,0,255]
        for j in range(size * 7 // 8, size // 8):
            img[i,j] = [0,0,0]

    # Lower Glasses
    for i in range(size // 2, size * 5 // 8):
        for j in range(size * 3 // 8):
            img[i,j] = [0,0,0]
        for j in range(size * 3 // 8, size * 5 // 8):
            img[i,j] = [0,0,255]
        for j in range(size * 5 // 8, size):
            img[i,j] = [0,0,0]

    # Underpart
    for i in range(size * 5 // 8, size):
        for j in range(size):
            img[i,j] = [0,0,255]

    cv2.imwrite(sys.argv[1], img)


def getExtension(filename):
    if len(filename.split(".")) == 1:
        return "no extension"
    else:
        return filename.split(".")[-1]


if __name__ == "__main__":
    main()
