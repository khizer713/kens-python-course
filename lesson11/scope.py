name="Ken"
count=1

def another():
    color="blue"    
    #count+=1
    global count
    count+=1

    print(count)

    def greeting(name):
        nonlocal color
        color="Red"

        print(name)
        print(color)
        
    greeting("Dave")

another()