import shutil
import glob
import os
from tqdm import tqdm

beforeDict='data21'
afterDict='data21'
for dir in tqdm(glob.iglob(f"./{beforeDict}/*")):
    if (os.path.isdir(dir)==True):
        for path in glob.iglob(f"{dir}/*"):
            dest = shutil.move(path, f"./{afterDict}/")
