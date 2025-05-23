#função len().
# exemplo:
String1 = "Python"
print(len(String1))

#  método upper()
# exemplo:
String1 = "Python"
String2 = String1.upper()
print(String2)

# método lower()
#Exemplo:
string1 = "Python"
string2 = string1.lower()
print(string2)

# método capitalize()
string1 = "python é uma linguagem de programação"
print(string1.capitalize())

# método title()
#exemplo:
string1 = "python é uma linguagem de programação"
print(string1.title())

# método strip()
#Exemplo:
string1 = "  Olá Python   "
print(string1.strip()) 

#método replace()
#exemplo:
String = "Olá Mundo"
String = String.replace("Mundo", "Python")

# método split()
# exemplo:
String5 = "Olá Mundo"
lista2 = String5.split(" ")
print(lista2) 

# método join()
lista = ["Olá", "Mundo"]
String = " ".join(lista)
print(String)

# método find()
# exemplo:
String1 = "Python Python Python"
print(String1.find("Python"))

# método count()
# exemplo:
String1 = "Python Python Python"
print(String1.count("Python"))

# método startswith()
#Exemplo
String1 = "Python"
print(String1.startswith("Py"))

# método endswith()
String1 = "Python"
print(String1.endswith("on"))

# método isalpha()
#Exemplo:
string1 = "Python123"
print(string1.isalpha())

# método isdigit()
#Exemplo:
string1 = "12345"
print(string1.isdigit()) 

# método isalnum()
#Exemplo:
string1 = "Python"
print(string1.isalnum())

# método isspace()
string1 = "   "
print(string1.isspace())

# método swapcase()
#Exemplo:
string1 = "Python"
print(string1.swapcase())

# método zfill()
#  exemplo:
string1 = "42"
print(string1.zfill(5))