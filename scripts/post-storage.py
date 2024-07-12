import requests, json

def main():
    try:
        title = str(input('Titulo: '))
        content = str(input('Conteudo: '))
        password = str(input('Senha: '))
        if password:
            data = {
                'title': title,
                'content': content,
                'password': password
            }
        else:
            data = {
                'title': title,
                'content': content,
            }

        response = requests.post('http://127.0.0.1:8000/api/storage/', data=json.dumps(data))
    
        if response.status_code == 201:
            content = response.json()
            print(content)
        else:
            print('Erro: ', response.status_code)
    except:
        print('Erro ao conectar com servidor')

if __name__=='__main__':
    main()
