import random
import string

def random_pass(length_input):
    lowers = string.ascii_lowercase
    uppers = string.ascii_uppercase
    nums = string.digits
    symbols = string.punctuation

    use_all_characters = lowers + uppers + nums + symbols
    
    temp = random.sample(use_all_characters, length_input)

    password= "".join(temp)
    return password

length = int(input('Please enter a length for the password >'))
return_password = random_pass(length)
print(return_password)
