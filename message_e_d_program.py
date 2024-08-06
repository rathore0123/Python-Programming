import random
       
       
def enc():
    message = input("Enter you message: ")
    list = message.split(" ")
    def ranchar(length):
        char = ""
        for i in range(length):
            string = 'abcdefghijklmnopqrstuvwxyz'
            ranIndex = random.randint(1,24)
            char += string[ranIndex]
        return char

    encmessage = ""
    for i, word in enumerate(list):
        if(i>0):
            encmessage += " " 
        if(len(word)<3 and len(word)>0):
            encmessage += word[::-1]
        else:
            encmessage += ranchar(3) + word[1:len(word)] + word[0] + ranchar(3)
    return encmessage

encodedmessage = enc()
print(encodedmessage)

def dec():
    message = encodedmessage
    list = message.split(" ")
    
    decmessage = ""
    for i, word in enumerate(list):
        if(i>0):
            decmessage += " " 
        if(len(word)<3 and len(word)>0):
            decmessage += word[::-1]
        else:
            decmessage += word[3:len(word)-3]

    list2 = decmessage.split(" ")
    findecmessage = ""
    for i, word in enumerate(list2):
        if(i>0):
            findecmessage += " "
        findecmessage += word[-1] + word[0:len(word)-1]
    return findecmessage
decodedmessage = dec()
print(decodedmessage)