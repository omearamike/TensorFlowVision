import os.path
import cProfile
import sys
import os
import importlib
import classify_image as ci
import pathlib

# main function that is run
def run(image):
    return(ci.runtime(image))


def main():
    directory = '/Users/michaelomeara/Documents/Personal_Projects/Darknet_YOLO/darknet/targetDirectory/models/tutorials/image/imagenet/Benchmarks/Benchmark_Images/Group1/'
    for filename in os.listdir(directory):
        if filename.endswith(".png") or filename.endswith(".jpeg") or filename.endswith(".JPG"):
            image = directory + filename # creating a suitable path to the images
            imageContent = run(image) # running vision on images
            f = open('runtime.log','a')
            f.write('\n' + imageContent) # writing imageContent to file
            f.close()
            try:
                os.makedirs(directory + imageContent)
            except OSError:
                if not os.path.isdir(directory + imageContent):
                    raise
            # os.rename('/Users/michaelomeara/Desktop/Screen Shot 2018-02-21 at 12.47.45.png', '/Users/michaelomeara/Desktop/digital clock/Screen Shot 2018-02-21 at 12.47.45.png' )
            os.rename(image, directory + imageContent + '/' + filename)
        else:
            print("File " + filename + " was not able to be added")

cProfile.run('main()')
