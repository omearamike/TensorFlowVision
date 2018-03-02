from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import os.path
import re
import sys
import tarfile
# import os
import numpy as np
from six.moves import urllib
import tensorflow as tf
import importlib
import classify_image as ci

# main function that is run
def run(image):
    return(ci.runtime(image))

directory = '/Users/michaelomeara/Desktop/'
for filename in os.listdir(directory):
    if filename.endswith(".png") or filename.endswith(".jpeg"):
        image = directory + filename
        f = open('helloworld.txt','a')
        f.write('\n' + run(image))
        f.close()
    else:
        print('Not a suitable Image')
