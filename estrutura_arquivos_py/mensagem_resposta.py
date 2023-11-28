

class Mensagem:
    def __init__(self, value, payload):
        self._value = value
        self._payload = payload
     
    def assunto_email(ambiente):
        return f'Print de Evidência Câmbio do Dólar! Ambiente {ambiente}'
    
    def mensagem_sucesso(self):
        return f'''
        <p>Prezados,</p>
        <p>o valor e a data fornecida pela Banco Central, foi Registrado no SAP com Sucesso.</p>
        <p>Status da operação = {self._value[1]}</p>
        <p>{self._payload}</p>
        <p>Siga os prints de Evidencia</p>
        <p>Atenciosamente RPA, Tekno Kroma!</p>
        '''
                
    def mensagem_erro(self):
        return f'''
        <p>Prezados,</p>
        <p>O valor e a data fornecida pela Banco Central, não foi registrado no SAP.</p>
        <p>Item já incluído anteriormente</p>
        <p>Status da operação = {self._value[1]}</p>
        <p>{self._payload}</p>
        <p>Atenciosamente RPA, Tekno Kroma!</p>
        '''