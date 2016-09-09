from PIL import Image
import glob, os
import sys


class Image(filePath):
      filePath = filePath

      def __init__ (self) :
            for file in glob.glob(filePath + "/*.*"):
                  filepath = os.path.realpath(file)
                  im = Image.open(file)
                  file = file.strip("../")
                  filepath = filepath.strip(file)
                  file = file.strip('.jpeg')
                  print(file)
                  if not os.path.exists(filepath + "output"):
                        os.makedirs(filepath + "output")
                  im.save(filepath + "output/" + file + ".jpg", "JPEG")
