from flask import Flask, request, jsonify


app = Flask(__name__) #Cria uma instância da aplicação Flask
#o argumento __name__ indica o nome do módulo atual, usado para identificar o ponto de entrada

# Dados simulados com CPFs e CNPJs
dados_mock = {
    "123.456.789-00": {"Cpf": "123.456.789-00", "SituacaoAdimplencia": "ADIMPLENTE"},
    "987.654.321-00": {"Cpf": "987.654.321-00", "SituacaoAdimplencia": "INADIMPLENTE"},
    "456.123.789-99": {"Cpf": "456.123.789-99", "SituacaoAdimplencia": "ADIMPLENTE"},
    "789.456.123-11": {"Cpf": "789.456.123-11", "SituacaoAdimplencia": "INADIMPLENTE"},
    "12.345.678/0001-99": {"Cpf": "12.345.678/0001-99", "SituacaoAdimplencia": "ADIMPLENTE"},
    "98.765.432/0001-55": {"Cpf": "98.765.432/0001-55", "SituacaoAdimplencia": "INADIMPLENTE"},
    "321.654.987-00": {"Cpf": "321.654.987-00", "SituacaoAdimplencia": "ADIMPLENTE"},
    "111.222.333-44": {"Cpf": "111.222.333-44", "SituacaoAdimplencia": "INADIMPLENTE"},
    "10.234.567/0001-88": {"Cpf": "10.234.567/0001-88", "SituacaoAdimplencia": "ADIMPLENTE"},
    "222.333.444-55": {"Cpf": "222.333.444-55", "SituacaoAdimplencia": "ADIMPLENTE"},
    "56.789.012/0001-22": {"Cpf": "56.789.012/0001-22", "SituacaoAdimplencia": "INADIMPLENTE"},
    "333.444.555-66": {"Cpf": "333.444.555-66", "SituacaoAdimplencia": "ADIMPLENTE"},
    "22.334.556/0001-99": {"Cpf": "22.334.556/0001-99", "SituacaoAdimplencia": "INADIMPLENTE"},
    "11.223.344/0001-77": {"Cpf": "11.223.344/0001-77", "SituacaoAdimplencia": "ADIMPLENTE"},
    "444.555.666-77": {"Cpf": "444.555.666-77", "SituacaoAdimplencia": "INADIMPLENTE"}
}

