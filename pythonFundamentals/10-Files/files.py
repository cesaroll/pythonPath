from pprint import pprint as pp

def write_file(fileName):
    f = open(fileName, mode='wt', encoding='utf-8')
    f.write('What are the roots that clutch, ')
    f.write('what branches grow\n')
    f.write('Out of this stony rubbish? ')
    f.close()
    

def read_file(fileName):
    g = open(fileName, mode='rt', encoding='utf-8')
    data = g.read(32) #reads 32 characters and advances the file pointer to the end of what was read
    print(data)
    print()
    
    data += g.read() # reads remaining text in file
    print(data)
    print()
    
    g.seek(0) #move the file pointer to the beginning of the file using zero offset, return value is new file pointer position
    
    #read line by line:
    
    print(g.readline())
    print(g.readline())
    print()
    
    g.seek(0)
    
    #read all lines into list of strings
    pp(g.readlines())
    
    g.close()

def read_allfile(fielName):
    f = open(fileName, mode='rt', encoding='utf-8')
    print()
    print(f.read())
    f.close()

def append_file(fileName):
    f = open(fileName, mode='at', encoding='utf-8')
    f.writelines([
        'Son of man,\n',
        'You cannot say, or guess, ',
        'for you know only,\n',
        'A heap of broken images, ',
        'where the sun beats\n'])
    f.close()
    

if __name__ == '__main__':
    fileName = "wasteland.txt"
    write_file(fileName)
    read_file(fileName)
    append_file(fileName)
    read_allfile(fileName)
    