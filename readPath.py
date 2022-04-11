import imp
import sys
import glob
import csv

def read_path(inputDir,outputDir):
    filenames=[_ for _ in glob.iglob(f"{inputDir}/*")]
    with open(f'{outputDir}/read_path.csv', 'w') as f:
        writer = csv.writer(f)
        writeRow=writer.writerow
        [writeRow(i,path) for i,path in enumerate(filenames)]
    return filenames

if __name__ == '__main__':
    args = sys.argv
    inDir=args[1]
    print('input Folder:{arg[1]}')
    outDir=args[2]
    print('output Folder:{arg[2]}')
    read_path(inDir,outDir)

