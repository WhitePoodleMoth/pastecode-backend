import requests

def main():
    try:
        response = requests.get('http://127.0.0.1:8000/api/explore/')
    
        if response.status_code == 200:
            content = response.json()
            print(content)
        else:
            print('Erro: ', response.status_code)
    except:
        print('Erro ao conectar com servidor')

if __name__=='__main__':
    main()
