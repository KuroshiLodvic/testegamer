usuarios = {'usuario': ['Ana', 'Bob', 'Claudio'], 
            'email': ['ana@gmail.com', 'bob@hotmail.com', 'claudio@bol.com'], 
            'senha': ['ana123', '123bob', 'clau!*']}

login = {}

email = input('Digite seu e-mail:\n')
login[email] = email

senha = input('Digite sua senha:\n')
login[senha] = senha

def verificador_registro(login:dict) -> str:
  
    for i in range(len(usuarios['email'])):
        if usuarios['email'][i] == login[email] and usuarios['senha'][i] == login[senha]:
            return print(f'O usuário {usuarios['usuario'][i]} foi identificado.')
            
    return print('Nenhum usuário foi identificado.')

verificador_registro(login)