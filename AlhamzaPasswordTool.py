import random
import string
print("!....𝘼𝙇𝙃𝘼𝙈𝙕𝘼 𝙋𝘼𝙎𝙎𝙒𝙊𝙍𝘿𝙎 𝙏𝙊𝙊𝙇....!")
input("PRESS ENTER TO START !")
x = input("Enter the lenght of password : 8 , 12 , 16 , 20 ..... ")
def rand_pass(lenght):
    ch = string.ascii_uppercase+string.ascii_lowercase+string.digits + string.punctuation
    random_string = "".join(random.choices(ch , k=lenght))

    return random_string

result = rand_pass(int(x));
print(f"The Lenght of the password is {len(result)}")
print(f"Your password is : {result}");
