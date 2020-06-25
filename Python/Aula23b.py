from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
try:
    html = urlopen("http://www.pudim.com/")
except HTTPError as e:
    print(e)
except URLError:
    print("Não consegui conectar")
else:
    print("Conectado")
