import requests
url="https://previews.123rf.com/images/elvil/elvil1512/elvil151200003/50029278-gato-egipcio-negro-peligroso-vector-de-dibujo-gr%C3%A1fico-en-busca-de-tatuajes.jpg"
response=requests.get(url,stream=True)


with open('httptest/download.jpg','wb') as file:
    for pedazo in response.iter_content():    
        file.write(pedazo)

