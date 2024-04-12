from urllib import request
from urllib.error import URLError

palabras_of = ["puto", "coño", "bobo"]

def palabras_ofensivas(url):
    try:
        f =request.urlopen(url)
    except URLError:
        print(f"¡La url '{url}' no existe!")
    else:
        contenido = f.read()
        palabras = contenido.split()
        palabras_encontradas = []

        for po in palabras_of:
            for pa in palabras:
                if po in pa.decode():
                    palabras_encontradas.append(po)
        return palabras_encontradas

url = 'https://es.wikipedia.org'
print(palabras_ofensivas(url))