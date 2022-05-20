def extraerNombres(url):
        empresa= ''
        condicion=False
        cont=0
        i=0
        while i < len(url):
            if url[i] == '.' and cont ==0:
                condicion = True
                cont+=1
                i+=1
            elif condicion and url[i]!='.' and cont==1:
                empresa+=url[i]
                i+=1
            elif condicion and url[i] == '.' and cont==1:
                i=len(url)
            else:
                i+=1
        return empresa   

print(extraerNombres('https://www.miro.es/reloj-pulsera-xiaomi-mi-watch-lite.html'))