import sys

def main(fileName):
    f = open(fileName, mode='rt', encoding='utf-8')
    for line in f:
        #print(line)
        sys.stdout.write(line)
    f.close()
    
if __name__ == '__main__':
    main(sys.argv[1])