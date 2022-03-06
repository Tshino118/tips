import glob
import os
from tqdm import tqdm
from pandas import read_csv

######################
#Please set "rename.csv" files and the dirctory in target file when running this code.
targetDict='data21'
######################
df = read_csv('./tips/rename.csv',dtype='str')
beforeNames = list(df['before'])
affterNames = list(df['after'])
namedict=dict(zip(beforeNames,affterNames))

beforeFileNames=[_ for _ in glob.iglob(f"./{targetDict}/*")]
afterFileNames=[]
for file in tqdm(beforeFileNames):
    if (os.path.isfile(file)==True):
        dir=os.path.dirname(file)
        fileName,ext=os.path.splitext(os.path.basename(file))
        print(fileName)
        fileNameSplited=fileName.split('_')
        beforeName=fileNameSplited[0]
        print(beforeName)
        fileNameSplited[0]=namedict[beforeName]
        print(fileNameSplited)
        afterfileName='_'.join(fileNameSplited)
        afterFileNames+=[f'{dir}/{afterfileName}{ext}']

for before,after in zip(beforeFileNames,afterFileNames):
    os.rename(before,after)
            
