import pyscreenshot as ImageGrab
import os,sys
from PIL import Image
from time import time

def capture(): #estimated run time = 0.13 seconds
	return ImageGrab.grab()

def usage():
	sys.exit("Usage: python screenShot.py [images]")

def main():
	Cycles = 100 # Average time per cycle ~1/4 sec
	args = len(sys.argv)
	if args > 2:
		usage()
	try:
		if args > 1:
			Cycles = int(sys.argv[1])
	except:
		usage()
	Directory = os.getcwd()

	if Cycles <= 0:
		return None
	start = time()
	Im = capture()
	for i in range(Cycles - 1):
		alpha = 1.0 / (i + 2)
		Im = Image.blend(Im,capture(),alpha)
	total = time() - start

	print "Total run time of {} sec with an average of {} sec per image".format( total, round(total / float(Cycles), 2 ) )

	path = os.path.join(Directory,"{}.png".format(time()))
	Im.save(path,method="w+")


if __name__ == "__main__":
	main()