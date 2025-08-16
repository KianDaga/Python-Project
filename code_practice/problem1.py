# given 2 numbers x and y, swap them

def swap(x,y):
    print(f"x: {x} , y : {y}")
    #swap here
    x = x+y
    y = x-y
    x = x-y

    #swap end
    print(f"x: {x} , y : {y}")
    return (x,y)

def main():
    swap(200, 100)

    
    
    
    

if __name__ == "__main__":
    main()
a

   