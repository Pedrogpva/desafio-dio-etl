import pandas as pd
import json

arquivo_excel = 'dados.xlsx'
dados = pd.read_excel(arquivo_excel)

# Extract
df = pd.read_csv("SDW2023.csv")
user_ids = df['UserID'].tolist()
print(user_ids)

# Função para guardar a list de usuarios e exibilas
def get_user(id):
    user_data = dados[dados['id'] == id]
    return user_data.to_dict(orient='records')[0] if not user_data.empty else None

users = [user for id in user_ids if (user := get_user(id)) is not None]

# Imprimir a lista de usuários
print(json.dumps(users, indent=2))

# Transfomr
# Função para gerar mensagens com base no status
def gera_mensagens(users):
    for user in users:
        if user['status'] == 'ativado':
            user['mensagem'] = 'Parabens! seu perfil foi ativado'
        elif user['status'] == 'desativado':
            user['mensagem'] = 'Que pena! seu perfil ainda nao foi ativado'
        else:
            user['mensagem'] = 'Algo deu errado! refaca a operacao'

# Chamar a função para gerar mensagens
gera_mensagens(users)

#Função para atualizar a tabela
def update(users):
    for user in users:
        user_id = user['id']
        mensagem = user['mensagem']
        dados.loc[dados['id'] == user_id, 'mensagens'] = mensagem

    dados.to_excel(arquivo_excel, index=False)

update(users)