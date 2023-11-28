from datetime import datetime

def horario_atual():
    agora = datetime.now()
    data_formatada_email = agora.strftime("%d/%m/%Y")
    hora_formatada_email = agora.strftime("%H:%M")

    return data_formatada_email, hora_formatada_email
