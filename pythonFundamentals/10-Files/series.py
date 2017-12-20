"""Read and rpint an integer series."""

import sys

def read_series(fileName):
    """ Using Context Manager With-Block, Close call is no longer needed """
    with open(fileName, mode='rt', encoding='utf-8') as f:
        return [ int(line.strip()) for line in f]

def main(fileName):
    series = read_series(fileName)
    print(series)
    
if __name__ == '__main__':
    main(sys.argv[1])