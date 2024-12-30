import pyodbc

def criar_conexao():
    try:
        conexao = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=192.168.210.66;'
            'DATABASE=robo_consultar_adimplencia;'
            'UID=sa;'
            'PWD=fpto@123;'
        )
        print('Conexão estabelecida com sucesso! ')
        return conexao
    except pyodbc.Error as e:
        print(f'Erro ao conectar com o banco de dados: {e}')
        return None
    
    
criar_conexao()
        