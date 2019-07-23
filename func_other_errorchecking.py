#!/usr/bin/python3
import os
a=os.system('cls||clear')

def checkinput(number,char,min,max,userinput,listinput=""):

    '''
    Used to valdate user input if i want a number checked between 1 and 10
    number=y,char=n,min=1,max=10,userinput=x)
    mainly used in draft where userinput is needed
    listinput="" if incoming data is a list (we are presuming userinput is a number)
    '''

#abc=input("Please enter something...")

    if listinput !="" and number=="y":
        try: 
            userinput=int(userinput)
        except:
                result="False"
                return result
        else:
            if userinput in listinput:
                result="True"
            else:
                result="False"
            return result
            
        
    
    
    else:
        usertest = 0
        result ="False"
        while True:
          try:
            usertest = int(userinput) 
          except ValueError:

            if char=="y":
                result="True"
            break
          else:
            if number=="y":
                userinput=int(userinput)
                if min <= userinput <=max:
                    result="True"
            break

        return result


if __name__=="__main__":
    
    #abc=input("Enter something")

    #result=checkinput(number="y",char="n",min=1,max=10,userinput=abc)
    #print (result)
    
    abc=input("Enter something")

    a=[1, 4, 6, 8, 11, 17, 18, 19, 20, 21]
    result=checkinput(number="y",char="n",min=1,max=24,userinput=abc,listinput=a)
    print (result)
     
