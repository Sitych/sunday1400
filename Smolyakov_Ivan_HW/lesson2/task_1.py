string = input("строка: ")
understring = input ("подстрока: ")
newstring = input("новая строка: ")
lenstring = len(understring)

while string.find(understring) > 0:
    i = string.find(understring)
    string = string [:i] + newstring + string[i+lenstring:]

print(string)
    
    
    
