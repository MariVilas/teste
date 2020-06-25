import re

nome = input('Qual o nome da sua cidade?: ')

if re.search('\\bSanto\\b', nome, re.IGNORECASE):
    print("A string tem o nome Santo")
else:
    print("A string não tem o nome Santo")
