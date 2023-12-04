
import hashlib


str_pass = "iwrupvqb"


counter = 0
while True:
    temp_pass = str_pass + str(counter)
    result = hashlib.md5(temp_pass.encode())
    if result.hexdigest().startswith("000000"):
        print("The byte equivalent of hash is : ", end="\n")
        print(result.hexdigest())
        print(counter)
        break
    else:
        counter += 1


