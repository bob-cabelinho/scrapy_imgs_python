'''Script que varre uma URL e busca por componentes.'''
import os
import time
import argparse
import requests
from bs4 import BeautifulSoup as bs

#pylint: disable=invalid-name

#Tratamento dos argumentos
parser = argparse.ArgumentParser(description='Script que varre uma URL e busca por componentes.')
parser.add_argument('--url', action='store',
                    dest='url', required=True,
                    help='URL do Site que deseja varrer.')

parser.add_argument('--quant', action='store',
                    dest='quant', required=True,
                    help='Quantidade de imagens que deseja baixar.')

arguments = parser.parse_args()

#website URL with gifs
try:
    request = requests.get(arguments.url)
    soup = bs(request.text, 'html.parser')
except:
    print('Erro na response do site')

#Localizar todas as tags <img>
images = soup.find_all('img')

#Criação do diretorio para salvar as imagens
if not os.path.exists('images'):
    os.makedirs('images')
os.chdir('images')

for index, image in enumerate(images, start=1):
    if index <= int(arguments.quant):
        try:
            url = image['src']
            source = requests.get(url)
            if source.status_code == 200:
                with open('image-' + str(index) + '.jpg', 'wb') as f:
                    f.write(requests.get(url).content)
                    print(f'Downloaded Image {index}')
        except :
            pass
        time.sleep(5)
    else:
        print('Download Completo!!')
        break
