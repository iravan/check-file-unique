from os import listdir
from os.path import isfile, join
import sys, argparse , hashlib  , time , glob

def main(path): 
    file_check_map = {}
    onlyfiles = glob.glob(path + '/**/*', recursive=True) 

    #for f in listdir(path) :
    #    if isfile(join(path, f)):
    #        onlyfiles.append(f)
    #    else:


    for f_path in onlyfiles:
        open_path = f_path
        if isfile(open_path) == False:
            continue
        f = open(open_path , "rb")
        data = f.read()
        h = hashlib.md5()
        h.update(data) 
        checksum = h.hexdigest()
        if checksum in file_check_map:
            print("Duplicated file : "+open_path+" with "+file_check_map[checksum])
            continue
        file_check_map[checksum] = open_path
        print(checksum +" : "+open_path)
        time.sleep(0.1)
        




    #print(onlyfiles)

if __name__ == "__main__": 
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', help='Specify the path needs to check files uniqueness')
    args = parser.parse_args() 
    if args.path != None:
        main(args.path)
