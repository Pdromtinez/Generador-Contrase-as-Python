import string 
import random

length = int(input("ingrese el tamaño de la contraseña: "))

characters = string.ascii_letters + string.digits + string.punctuation

password =  "".join(random.choice(characters) for i in range(length))


print("The generated password is: " + password)