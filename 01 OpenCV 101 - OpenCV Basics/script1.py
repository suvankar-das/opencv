import argparse
import os
import cv2


def run():
    # construct the argument parser and parse the argument
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="path to input image")
    # python script1.py --image image_name.extension
    args = vars(ap.parse_args())
    print('args ==',args)
    # load the image from the disk via imread() of cv2 and then
    # grab the spatial dimension incl. width , height and number of channels
    image = cv2.imread(args["image"])
    print('image.shape gives ==>', image.shape)
    # Understanding image dimensions
    # Height, Width, and Channels

    # Height: Refers to the number of rows or pixels vertically in the image
    # Width: Refers to the number of columns or pixels horizontally in the image
    # Channels: Indicates the number of color channels in the image (e.g., 3 for RGB images)
    # image.shape[:3] captures the values of height, width, and channels of the image

    (height, width, channel) = image.shape[:3]

    # display height width and channel
    print("Width: {} in pixels", format(width))
    print("Height: {} in pixels", format(height))
    print("Channels: ", format(channel))

    # show the image and wait for keypress
    cv2.imshow("Image", image)
    cv2.waitKey(0)

    # Save the image back to the disk
    output_dir = "D:/Babai/Learning/opencv/codes/01 OpenCV 101 - OpenCV Basics/output_dir/"
    if not os.path.exists(output_dir):
        print('path exist')
        os.makedirs(output_dir)
    output_file = os.path.join(output_dir, "newimage.jpg")
    print('output file',output_file)
    cv2.imwrite(output_file, image)

run()
