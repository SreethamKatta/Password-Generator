import string
import random
if __name__ == "__main__":
    set1 = string.ascii_lowercase
    set2 = string.ascii_uppercase
    set3 = string.digits
    set4 = string.punctuation
    pwdlen = int(input("Enter password length:\n"))
    set = []
    set.extend(list(set1))
    set.extend(list(set2))
    set.extend(list(set3))
    set.extend(list(set4))
    random.shuffle(set)
    print ("Your Password is : ")   
    print("".join(random.sample(set,pwdlen)))


