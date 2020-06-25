import re

nome = input('Qual o seu nome?: ')

if re.search('\\bSilva\\b', nome, re.IGNORECASE):
    print("O seu nome tem Silva")
else:
    print("O seu nome não tem Silva")