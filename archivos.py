file = open("textoprueba1.txt")


print(file.read())

file.close
file = open("textoprueba1.txt")

for line in file:
    print(line)

file.close

file2 = open("textoprueba2.txt",'w')
file3 = open("textoprueba3.txt", 'a')

file2.writelines('hola mundo')
file3.writelines('hola mundo 3')
file3.write('\nPrueba Hola Mundo linea nueva')



file2.close
file3.close

file2 = open("textoprueba2.txt",'r')
file3 = open("textoprueba3.txt", 'r')

print('archivo 1',file2.read())
print('archivo 2',file3.read())

file2.close
file3.close