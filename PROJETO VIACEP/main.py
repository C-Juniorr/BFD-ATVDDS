import requests
import mysql.connector

def salvar_cep(dados):
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234567",
        database="ceps"
    )
    cursor = conexao.cursor()

    cursor.execute("INSERT INTO cep (cep, logradouro, bairro, localidade, uf) VALUES (%s, %s, %s, %s, %s)", (dados['cep'].replace("-", ""), dados['logradouro'], dados['bairro'], dados['localidade'], dados['uf']))

    conexao.commit()

    print("CEP salvo com sucesso no banco!")

    cursor.close()
    conexao.close()
    
def reqcep():
    while True:
        cep = input("digite seu cep: ")
        cep = cep.replace("-", "")
        cep = cep.replace(" ", "")
        
        if len(cep) != 8:
            print("DIGITE UM CEP VALIDO")
            
        else:
            r = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
            if r.status_code == 200:
                dadoscep = r.json()
                if "erro" in dadoscep:
                    print("CEP não encontrado.")
                else:
                    print("CEP encontrado:", dadoscep)
                    salvar_cep(dadoscep)
                    break
            else:
                print("Erro na requisição!")
                    #cep logradouro bairro localidades uf
reqcep()