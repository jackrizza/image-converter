from PIL import Image
import glob, os
import sys
import thread
import multiprocessing
from multiprocessing import Pool

fileNumber = 0
_FNA = [] 
cpu = multiprocessing.cpu_count()

def image(junk) :
      for file in glob.glob("../*.*"):
            filepath = os.path.realpath(file)
            im = Image.open(file)
            file = file.strip("../")
            filepath = filepath.strip(file)
            file = file.strip('.jpeg')
            print(file)
            if not os.path.exists(filepath + "output"):
                  os.makedirs(filepath + "output")
            im.save(filepath + "output/" + file + ".jpg", "JPEG")


for file in glob.glob("../*.*"):
      fileNumber = fileNumber + 1
      _FNA.append(fileNumber)


if __name__ == '__main__':
      p = Pool(1)
      p.map(image, _FNA)
