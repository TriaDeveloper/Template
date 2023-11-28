import win32com.client as win32

class SendEmail():
    def __init__(self, TO, assunto, caminhos_anexos, mensagem):
        self._to = TO
        self._assunto = assunto
        self._caminhos_anexos = caminhos_anexos
        self._mensagem = mensagem
            
    def __str__(self):
        try:
            outlook = win32.DispatchEx('outlook.application')
            message = outlook.CreateItem(0)
            message.To = str(self._to)
            message.Subject = str(self._assunto)
            message.HTMLBody = self._mensagem
            if not self._caminhos_anexos is None:
                for anexo in self._caminhos_anexos:
                    message.Attachments.Add(anexo)   
                
            # message.Display()
            message.Send()
            resposta = "E-Mail envia com sucesso."
        except Exception as a:
            resposta = a
        finally:
            return resposta
        

