#magic_8_Ball

import random

a = random.randint(0,19)

if a == 0:
    print("As I see it, yes.")
elif a == 1:
    print("Ask again later.")
elif a == 2:
    print("Better not tell you now.")
elif a == 3:
    print("Cannot predict now.")
elif a == 4:
    print("Concentrate and ask again.")
elif a == 5:
    print("Don’t count on it.")
elif a == 6:
    print("It is certain.")
elif a == 7:
    print("It is decidedly so.")
elif a == 8:
    print("Most likely.")
elif a == 9:
    print("My reply is no.")
elif a == 10:
    print("My sources say no.")
elif a == 11:
    print("Outlook not so good.")
elif a == 12:
    print("Outlook good.")
elif a == 13:
    print("Reply hazy, try again.")
elif a == 14:
    print("Signs point to yes.")
elif a == 15:
    print("Very doubtful.")
elif a == 16:
    print("Without a doubt.")
elif a == 17:
    print("Yes.")
elif a == 18:
    print("Yes – definitely.")
else:
    print("You may rely on it.")