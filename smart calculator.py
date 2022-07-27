'''def hcf(x,y):
    if x>y:
        smaller=x
    else:
        smaller=y
    for i in range(1,smaller+1):
        if((x%i==0) and (y%i==0)):
            hcf=i
    return hcf
num1=int(input('Enter first number:'))
num2=int(input('Enter second number:'))
print('The H.C.F of ',num1,'and', num2,'is',hcf(num1,num2))
'''
responces=['Welcome to smart calculator','My name is smart calc','Thanks','Sorry this is beyond my scope']
def extract_numbers_from_text(text):
    l=[]
    for t in text.split(' '):
        try:
            l.append(float(t))
        except ValueError:
                pass
    return(l)

def lcm(x,y):
    if(x>y):
        greater=x
    else:
        greater=y
    while(True):
        if ((greater %x==0)and (greater %y==0)):
            lcm=greater
            break
        greater+=1
    return lcm

def hcf(x,y):
    if x>y:
        smaller=x
    else:
        smaller=y
    for i in range(1,smaller+1):
        if((x%i==0) and (y%i==0)):
            hcf=i
    return hcf

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def multiply(a,b):
    return a*b

def division(a,b):
    return a/b

def end():
    print(responces[2])

def myname():
    print(responces[2])
    input('Press Enter Key To Exit')
    exit()

def sorry():
    print(responce[3])

operations={"LCM":lcm,"HCF":hcf,"PLUS":add,"ADDITION":add,"ADD":add,"SUM":add,"MINUS":sub,"SUBTRACTION":sub,"SUBTRACT":sub,"DIFFERENCE":sub,"PRODUCT":multiply,
                      "MULTIPLICATION":multiply,"MULTIPLY":multiply,"DIVIDE":division}

commands={"NAME":myname,"END":end,"EXIT":end,"CLOSE":end}

print(responces[0])
print(responces[1])

while (True):
    print()
    text=input('Enter Some Text:')
    for word in text.split(' '):
        if (word.upper() in operations.keys()):
            try  :
                l=extract_numbers_from_text(text)
                r=operations[word.upper()](l[0],l[1])
                print(r)
            except :
                print('Something Is Wrong Please Try:')
            finally:
                break
        elif word.upper() in commands.keys():
            commands[word.upper()]()
            break
        

