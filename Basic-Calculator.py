import time
import math
time.sleep(1)
print("Hello!! \nHope you are having a Good Day!! \nLet's start Calculating!")
time.sleep(2)
def error():
    print("Sorry, Something went wrong :( \nPlease try again..")
    time.sleep(1)
    maincalc()
def loopcalc():
    time.sleep(1)
    anothercalc=input("Have another question? (Yes/No)")
    if anothercalc== 'Yes':
        maincalc()
    if anothercalc== 'yes':
        maincalc()
    if anothercalc== 'No':
        print("Alright! \nBye Bye! Have a nice day!")
    if anothercalc== 'no':
        print("Alright! \nBye Bye! Have a nice day!")
    else:
        error()
def add():
    n1=input('Enter the First Number: ')
    n2=input('Enter the Second Number: ')
    moren=input('Do you have a Third Number? (Yes/No)')
    if moren== "Yes":
        n3=input('Enter the Third Number here: ')
        print("It's", float(n1)+float(n2)+float(n3))
        loopcalc()   
    if moren== "yes":
        n3=input('Enter the Third Number here: ')
        print("It's", float(n1)+float(n2)+float(n3))
        loopcalc()
    if moren== 'No':
        print("It's", float(n1)+float(n2))
        loopcalc()
    if moren== 'no':
        print("It's", float(n1)+float(n2))
        loopcalc()
def subtract():
    n1=input('Enter the First Number: ')
    n2=input('Enter the Second Number: ')
    moren=input('Do you have a Third Number? (Yes/No)')
    if moren== "Yes":
        n3=input('Enter the Third Number here:')
        print("It's", int(n1)-int(n2)-int(n3))
        loopcalc()
    if moren== "yes":
        n3=input('Enter the Third Number here:')
        print("It's", int(n1)-int(n2)-int(n3))
        loopcalc()
    if moren== 'No':
        print("It's", int(n1)-int(n2))
        loopcalc()
    if moren== 'no':
        print("It's", int(n1)-int(n2))
        loopcalc()
def multiply():
    n1=input('Enter the First Number: ')
    n2=input('Enter the Second Number: ')
    moren=input('Do you have a Third Number? (Yes/No)')
    if moren== "Yes":
        n3=input('Enter the Third Number here: ')
        print("It's", float(n1)*float(n2)*float(n3))
        loopcalc()
    if moren== "yes":
        n3=input('Enter the Third Number here: ')
        print("It's", float(n1)*float(n2)*float(n3))
        loopcalc()
    if moren== 'No':
        print("It's", float(n1)*float(n2))
        loopcalc()
    if moren== 'no':
        print("It's", float(n1)*float(n2))
        loopcalc()
def divide():
    n1=input('Enter the First Number: ')
    n2=input('Enter the Second Number: ')
    moren=input('Do you have a Third Number? (Yes/No)')
    if moren== "Yes":
        n3=input('Enter the Third Number here: ')
        print("It's", float(n1)/float(n2)/float(n3))
        loopcalc()
    if moren== "yes":
        n3=input('Enter the Third Number here:')
        print("It's", float(n1)/float(n2)/float(n3))
        loopcalc()
    if moren== 'No':
        print("It's", float(n1)/float(n2))
        loopcalc()
    if moren== 'no':
        print("It's", float(n1)/float(n2))
        loopcalc()
def exponents():
    n1=input("Enter the Base number: ")
    n2=input("Enter the Exponential number: ")
    print("It's", int(n1)**int(n2))
    time.sleep(1)
    anothercalc=input("Have another question? (Yes/No)")
    if anothercalc== 'Yes':
        maincalc()
    if anothercalc== 'yes':
        maincalc()
    if anothercalc== 'No':
        print("Alright! \nBye Bye! Have a nice day!")
    if anothercalc== 'no':
        print("Alright! \nBye Bye! Have a nice day!")
def root():
    n1=input("Enter the Base number: ")
    n1=int(n1)
    print("It's", math.sqrt(n1))
    time.sleep(1)
    loopcalc()
def tsin():
    n1=input('Enter the Angle (degrees):')
    n1=int(n1)
    print("It's", math.sin(math.radians(n1)))
    loopcalc()
def tcos():
    n1=input('Enter the Angle (degrees):')
    n1=int(n1)
    print("It's", math.cos(math.radians(n1)))
    loopcalc()
def ttan():
    n1=input('Enter the Angle (degrees):')
    n1=int(n1)
    print("It's", math.tan(math.radians(n1)))
    loopcalc()
def trignocalc():
    trig=input("So.. \n-->Sin Angle      (Sin) \n-->Cos Angle      (Cos) \n-->Tan Angle      (Tan) \nWhat would you like to do?:")
    if trig== "Sin":
        tsin()
    if trig== "sin":
        tsin()
    if trig== "Cos":
        tcos()
    if trig== "cos":
        tcos()
    if trig== "Tan":
        ttan()
    if trig== "tan":
        ttan()
def log():
    n1=input("Enter the First number: ")
    n1=int(n1)
    print("It's", math.log(n1))
    loopcalc()
def ap():
    n1=input("Enter the First number: ")
    n2=input("Enter the Second number: ")
    n1=int(n1)
    n2=int(n2)
    cd=n2-n1
    cd=int(cd)
    print("The Common diffenrence is", cd)
    apnterms=n1, n2, n2+cd, n2+(2*cd), n2+(3*cd), n2+(4*cd), n2+(5*cd), n2+(6*cd), n2+(7*cd)
    print("The Next 10 terms are: ", apnterms)
    nsum=input("Number of Terms for Sum: ")
    nsum=int(nsum)
    sum=(nsum/2)*((2*n1)+(nsum-1)*cd)
    print("The sum of", nsum, "is", sum)
    loopcalc()
def gp():
    n1=input("Enter the First number: ")
    n2=input("Enter the Second number: ")
    n1=int(n1)
    n2=int(n2)
    cd=n2/n1
    cd=float(cd)
    print("The Common Ratio is", cd)
    apnterms=n1, n2, n2*cd, n2*(cd**2), n2*(cd**3), n2*(cd**4), n2*(cd**5), n2*(cd**6), n2*(cd**7)
    print("The Next 10 terms are: ", apnterms)
    nsum=input("Number of Terms for Sum: ")
    nsum=int(nsum)
    GPform=cd>1
    if GPform==True:
        sum=n1*(1-(cd**nsum))/(1-cd)
    elif GPform==False:
        sum=n1*((cd**nsum)-1)/(cd-1)
    print("The sum of", nsum, "is", sum)
    loopcalc()
def maincalc():
    calc=input('So.. \n--> Add           (+) \n--> Subtract      (-) \n--> Multiply      (*) \n--> Divide        (/) \n--> Exponent      (^) \n--> Root          (&) \n--> Trignometry   (#) \n--> Log           (|) \n--> AP            (!) \n--> GP            (!!)\nWhat would you like to do?: ')
    if calc== "Add":
        add()
    if calc== "add":
        add()
    if calc== "+":
        add()
    if calc== "Subtract":
        subtract()
    if calc== "subtract":
        subtract()
    if calc== "Sub":
        subtract()
    if calc== "sub":
        subtract()
    if calc== "-":
        subtract()
    if calc== "Multiply":
        multiply()
    if calc== "multiply":
        multiply()
    if calc== "*":
        multiply()
    if calc== "Divide":
        divide()
    if calc== "divide":
        divide()
    if calc== "/":
        divide()
    if calc== "Exponent":
        exponents()
    if calc== "Exponents":
        exponents()
    if calc== "exponent":
        exponents()
    if calc== "exponents":
        exponents()
    if calc== "^":
        exponents()
    if calc== "Root":
        root()
    if calc== "root":
        root()
    if calc== "&":
        root()
    if calc== "Trigno":
        trignocalc()
    if calc== "trigno":
        trignocalc()
    if calc== "Trignometry":
        trignocalc()
    if calc== "trignometry":
        trignocalc()
    if calc== "#":
        trignocalc()
    if calc== "Log":
        log()
    if calc== "log":
        log()
    if calc== "|":
        log()
    if calc== "AP":
        ap()
    if calc== "Ap":
        ap()
    if calc== "ap":
        ap()
    if calc== "|":
        ap()
    if calc== "GP":
        gp()
    if calc== "Gp":
        gp()
    if calc== "gp":
        gp()
    if calc== "||":
        gp()
maincalc()