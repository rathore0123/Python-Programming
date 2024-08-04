import time
timestamp = time.strftime('%H:%M:%S')
hour = int(time.strftime('%H'))

name = input("Enter your Name: ")
if(0<=hour<12):
    print(f"Good Morning {name} Sir!")
elif(12<=hour<17):
    print(f"Good Afternonn {name} Sir!")
elif(17<=hour<21):
    print(f"Good Evening {name} Sir!")
else:
    print(f"Good Night {name} Sir!")
