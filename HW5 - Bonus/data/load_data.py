import pickle
import glob

path = './*.bin'

files = glob.glob(path)

for f in files:
    with open(f, 'rb') as fp:
        signal = pickle.load(fp)
        print ('First sample of the file:', signal[0])
