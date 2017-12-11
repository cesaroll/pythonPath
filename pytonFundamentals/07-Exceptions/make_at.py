import os
import sys

def make_at(path, dir_name):
    original_path = os.getcwd()
    
    try:
        os.chdir(path)
        os.mkdir(dir_name)
    except OSError as e:
        print(e, file=sys.stderr)
        raise
    finally:
        os.chdir(original_path)
        
def main():
    make_at("/home/ec2-user/environment/pythonPath/pytonFundamentals", "test")
    
if __name__ == '__main__':
    main()