import random

chars = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

def passwordGenerator(leng):
    data = ""
    for i in range(leng):
        x = random.randint(0, 71)
        data += chars[x]
    print(data)


while True:
    print("Şifreniz Kaç Basamaklı Olsun")
    number = int(input())
    passwordGenerator(number)
