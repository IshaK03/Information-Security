import random
import string


def generateCaptcha(R1):
    ans = ''
    alphabet = string.ascii_lowercase + string.ascii_uppercase
    R2_list = []

    for i in range(R1):
        R2 = random.randint(0,9)
        R2_list.append(R2)
        if(R2 < 6):
            ans += str(random.randint(0,9))
        else:
            ans += random.choice(alphabet)
    
    print("R2 Values generated are: ", R2_list)
    return ans


R1 = int(input("Enter length of Captcha: "))
captcha = generateCaptcha(R1)
print("Generated CAPTCHA is: ", captcha)
input = input("Validate CAPTCHA: ")
print("Correct!") if (input == captcha) else print("Incorrect Input!")