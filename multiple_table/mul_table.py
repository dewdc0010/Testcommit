while True:
    num = input("enter multiplication table [x to exit]: ")
    if num == 'x' :
        exit()
    if num.isdecimal():
     for i in range (1,13):
        print(int(num),"x",i,"=",int(num)*i)
    else:
        print("Enter number only !!!, try again")