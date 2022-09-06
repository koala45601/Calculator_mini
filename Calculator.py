import time
sum = 0
while True:
    a = int(input("Input 1 : "))
    x = (input("Optios  : "))
    b = int(input("Input 2 : "))
    def select(a,b):
        if a != None and b != None:    
            if x == '+':
                sum = a + b
            elif x == '-':
                sum = a - b
            elif x == '*':
                    sum = a * b
            elif x == '/':
                    sum = a / b
            else:
                print("Invalid input. Please input (+,-,*,/) only.")   
        #print(f"Sum in function : {sum}")
        time_1 = time.time()
        #print(f"Time in function :{time_1}"%2f)
        return sum

    print(f"Sum in Loop : {select(a,b)}")
        