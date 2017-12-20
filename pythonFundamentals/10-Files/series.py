"""Read and rpint an integer series."""

import sys

def read_series(fileName):
    try:
        f = open(fileName, mode='rt', encoding='utf-8')
        
        """ For Loop
        series = []
        for line in f:
            a = int(line.strip())
            series.append(a)
            
            
        return series
        """
        
        """ List comprehension """
        return [ int(line.strip()) for line in f]
        
    finally:
        f.close()

def main(fileName):
    series = read_series(fileName)
    print(series)
    
if __name__ == '__main__':
    main(sys.argv[1])