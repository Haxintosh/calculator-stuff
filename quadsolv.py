print("Choose input")
print("1. as vertex form")
print("2. as general form")
print("3. as factorized form")

choice = int(input("Enter choice: "))

if choice == 1:
    a = float(input("Enter a: "))
    h = float(input("Enter h: "))
    k = float(input("Enter k: "))

    isReal = None
    print("Vertex form:")
    print("y = "+str(a)+"(x - "+str(h)+")^2 + "+str(k))

    if (-k / a < 0):
        print("no x-intercepts")
        isReal = False
        x1 = None
        x2 = None
    else:
        x1 = h + (-k / a) ** 0.5
        x2 = h - (-k / a) ** 0.5
        isReal = True

    if x1 !=None or x2 != None:
        if x1 > x2:
            x1, x2 = x2, x1
        if x1 == x2:
            print("x-intercept (only one): ", x1)
        else:
            print("x-intercepts: ", x1, x2)

        yInt = (0 - h) ** 2 * a + k
        print("y-intercept: (0,", yInt, ")")

    print("Vertex:", (h, k))
    print("Opens:", "up" if a > 0 else "down")

    if a > 0:
        print("Minimum: ", k)
        print("Image:", "["+str(k)+", inf[")
        if isReal:
            print("Positive:", "]-inf, "+str(x1)+"] U ["+str(x2)+", inf[")
            print("Negative:", "["+str(x1)+", "+str(x2)+"]")
        else:
            print("Positive:", "xER")
            print("Negative:", "none")
        print("Rising: ["+str(h)+", inf[")
        print("Falling: ]-inf, "+str(h)+"]")
    elif a < 0:
        print("Maximum: ", k)
        print("Image: ", f"]-inf, "+str(k)+"]")
        if (isReal):
            print("Positive:", f"["+str(x1)+", "+str(x2)+"]")
            print("Negative:", f"]-inf, "+str(x1)+"] U ["+str(x2)+", inf[")
        else:
            print("Positive:", f"none")
            print("Negative:", f"xER")
        print(f"Rising: ]-inf, "+str(h)+"]")
        print(f"Falling: ["+str(h)+", inf[")
    else:
        print("No minimum or maximum!")
    if x1 != None and x2 != None:
        print("Factorised form: ", a, "(x -", x1, ")(x -", x2, ")")
    elif x1 != None:
        print("Factorised form: ", a, "(x -", x1, ")^2")
    elif x2 != None:
        print("Factorised form: ", a, "(x -", x2, ")^2")
    else:
        print("No factorised form")
elif choice==2:
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))

    isReal = None
    print("General form:")
    print("y = "+str(a)+"x^2 + "+str(b)+"x + "+str(c))

    if (b ** 2 - 4 * a * c < 0):
        print("no x-intercepts")
        isReal = False
        x1 = None
        x2 = None
    else:
        x1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
        x2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
        isReal = True

    if x1 != None or x2 != None:
        if x1 > x2:
            x1, x2 = x2, x1
        if x1 == x2:
            print("x-intercept (only one): ", x1)
        else:
            print("x-intercepts: ", x1, x2)

        yInt = c
        print("y-intercept: (0,", yInt, ")")

    h = -b / (2 * a)
    k = a * h ** 2 + b * h + c
    print("Vertex:", (h, k))
    print("Opens:", "up" if a > 0 else "down")

    if a > 0:
        print("Minimum: " + str(k))
        print("Image: [" + str(k) + ", inf[")
        if isReal:
            print("Positive: ]-inf, " + str(x1) + "] U [" + str(x2) + ", inf[")
            print("Negative: [" + str(x1) + ", " + str(x2) + "]")
        else:
            print("Positive: xER")
            print("Negative: none")
        print("Rising: [" + str(h) + ", inf[")
        print("Falling: ]-inf, " + str(h) + "]")
    elif a < 0:
        print("Maximum: " + str(k))
        print("Image: ]-inf, " + str(k) + "]")
        if isReal:
            print("Positive: [" + str(x1) + ", " + str(x2) + "]")
    elif choice == 3:
        a = float(input("Enter a: "))
        b = float(input("Enter x1: "))
        c = float(input("Enter x2: "))

        isReal = None
        print("Factorized form:")
        print("y = " + str(a) + "(x - " + str(b) + ")(x - " + str(c) + ")")

    if b == c:
        print("x-intercept (only one): ", b)
    else:
        print("x-intercepts: ", b, c)

    yInt = a * b * c
    print("y-intercept: (0,", yInt, ")")

    h = (b + c) / 2
    k = a*(h-b)*(h-c)
    print("Vertex:", (h, k))
    print("Opens:", "up" if a > 0 else "down")

    if a > 0:
        print("Minimum: " + str(k))
        print("Image: " + "[" + str(k) + ", inf[")
        print("Positive: " + "]-inf, " + str(b) + "] U [" + str(c) + ", inf[")
        print("Negative: " + "[" + str(b) + ", " + str(c) + "]")
        print("Rising: [" + str(h) + ", inf[")
        print("Falling: ]-inf, " + str(h) + "]")
    elif a < 0:
        print("Maximum: " + str(k))
        print("Image: " + "]-inf, " + str(k) + "]")
        print("Positive: [" + str(b) + ", " + str(c) + "]")
        print("Negative: ]-inf, " + str(b) + "] U [" + str(c) + ", inf[")
        print("Rising: ]-inf, " + str(h) + "]")
        print("Falling: [" + str(h) + ", inf[")
    else:
        print("No minimum or maximum!")
