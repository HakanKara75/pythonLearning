import random

print(random.randint(1,10))

print(random.random()) #float

answer=random.randint(1,3)

if answer==1:
    print("Yes")
if answer==2:
    print("No")
else:
    print("Maybe")

    lucky_number=random.randint(1,100)

    fortune_number=random.randint(1,3)
    fortune_text=""
    if fortune_number==1:
        fortune_text="You will have a great day"
        if fortune_number ==2:
            fortune_text = "Today will be though ....but worth it"
            if fortune_number == 3:
                fortune_text = "You will get married this year"

    print(f"{fortune_text} Your lucky number is: {lucky_number}") #f harfi metin icine degisken eklememize imkan verdi


