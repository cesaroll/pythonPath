""" Lucas Series """

def lucas():
    yield 2
    a = 2
    b = 1
    while True:
        yield b
        a, b = b, a + b

def run_lucas():
    count = 1000
    for x in lucas():
        print(x)
        count -= 1
        if count <= 0:
            break
        
if __name__ == '__main__':
    run_lucas()

    
