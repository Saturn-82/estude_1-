#print("Vruuum! Projeto Estude 1% iniciado com sucesso! 🚀")
from src.user_auth import criar_tabela_usuarios, cadastrar_usuario, login_usuario

criar_tabela_usuarios()

# Cadastrar um usuário de teste
#cadastrar_usuario("Saturno", "saturno@lua.com", "123456")

# Fazer login
login_usuario("saturno@lua.com", "123456")
