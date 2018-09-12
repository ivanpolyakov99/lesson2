def task1():
    try:
        n = int(input("Input numb to convert: "))
    except ValueError:
        print("Not numb, try again")
    else:
        a = input("Convert into bytes (b) or kilobytes (kb) :")
        if a == 'b':
            print("%d Kb = %d bytes " % (n, n * 1024))
        elif a == 'kb':
            print("%d bytes = %d Kb" % (n, n / 1024))
    pass
    
    
def task2():
    try:
        n = int(input("Input numb : "))
    except ValueError:
        print("Not numb, try again")
    else:
        s = 0
        c = 1
        while n > 0:
            s = s + n % 10
            c = c * (n % 10)
            n = n // 10
        print("Amount :", int(s), "\nComposition :", int(c))
    pass
    
    
def task3():
    try:
        b = float(input("Begin : "))
        e = float(input("End : "))
        s = float(input("Step : "))
    except ValueError:
        print("It not numb, again")
    else:
        while b <= e:
            y = -1.24 * b ** 2 + b
            print(b, "---", y)
            b = b + s
    pass


def task4():
    try:
        a = int(input("Numb : "))
    except ValueError:
        print("Again")
    else:
        i = 1
        prov = True
        for j in str(a)[-i]:
            if j != str(a)[-i]:
                prov = False
            i = i + 1
        print("Number", a, "is palindrom ?\n", prov)
    pass


def task5():
    arr = [-1, 5, 2, 0, 8]
    s = 0
    par = 0
    for i in range[arr]:
        if arr[i] > 0:
            s = s + arr[i]
            par = par + 1
    end = s / par
    print("Average :", end)
    pass
