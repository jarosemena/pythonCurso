file = open("textoprueba1.txt")
file2 = open("textoprueba2.txt",'w')
file3 = open("textoprueba3.txt", 'a')

print(file.read())

file2.writelines('hola mundo')
file3.writelines('hola mundo 3')