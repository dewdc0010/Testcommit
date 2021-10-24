while True:
    try:
        num = input("enter multiplication table [x to exit]: ")
        for i in range (1,13):
            print(int(num),"x",i,"=",int(num)*i)
    except :
        if str(num) != 'x' :
            print("Enter number only !!!, try again")
        else:
            exit()