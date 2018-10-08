from argparse import ArgumentParser
from PIL import Image, ImageOps
import os
import sys

def setupArgs():
    parser = ArgumentParser()
    parser.add_argument("-s", "--source-directory", dest="sourceDir",
                         help="source directory containing image files", metavar="DIRECTORY")

    parser.add_argument("-w", "--width", dest="fileWidth",
                         help="width of output image" )

    parser.add_argument("-l", "--height", dest="fileHeight",
                         help="height of output image" )

    parser.add_argument("-d", "--directory", dest="destDir", default="./output",
                        help="destination directory where the images are dropped, default is" 
                        " current directory", metavar="DIRECTORY")

    parser.add_argument("-e", "--extension", dest="extension", default="jpg",
                        help="type of image extension") 
                        
    parser.add_argument("-q", "--quiet", 
                        action="store_false", dest="verbose", default=True,
                        help="Dont' print status messages to stdout")

    return parser.parse_args()


def resizeImage():
    args = setupArgs()
    dimensions = int(args.fileWidth), int(args.fileHeight)

    for fileName in os.listdir(args.sourceDir):
        fullFilePath = args.sourceDir + '/' + fileName
        if fileName.endswith(".jpg") or fileName.endswith(".png"):
            outputFile = os.path.splitext(fileName)[0] + '.' + args.extension
            try:
                img = Image.open(fullFilePath)
                newImg = ImageOps.fit(img, dimensions, Image.ANTIALIAS)
                dest = args.destDir + '/' + outputFile
                newImg.save(dest, "JPEG") 
            except  IOError:
                     print 'Failed to shrink image file ', fileName 


resizeImage()
    


