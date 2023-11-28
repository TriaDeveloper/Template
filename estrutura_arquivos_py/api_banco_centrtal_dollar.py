import requests
from datetime import date, timedelta, datetime

class ApiBancoCenrtal:
    
    def _obter_cotacoes_dolar():
        # Obtém a data atual        
        data_formatada = ApiBancoCenrtal._verifica_dia_da_semana()
        data_objeto = datetime.strptime(data_formatada[2], '%m-%d-%Y')

        while True:
            # Formata a data no formato esperado pela API
            url = f"https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarDia(dataCotacao=@dataCotacao)?@dataCotacao='{data_objeto.strftime('%m-%d-%Y')}'&$top=100&$format=json&$select=cotacaoCompra,cotacaoVenda"

            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()
                if 'value' in data and len(data['value']) > 0:
                    cotacao_compra = data['value'][0]['cotacaoCompra']
                    cotacao_venda = data['value'][0]['cotacaoVenda']

                    print('Câmbio de compra {}'.format(cotacao_compra))
                    print('Câmbio de venda {}'.format(cotacao_venda))
                    print('Data do câmbio {}'.format(data_objeto.strftime('%m-%d-%Y')))

                    #return cotacao_compra, cotacao_venda, data_atual
                    return cotacao_compra, cotacao_venda, data_objeto
                else:
                    # Diminui um dia da data atual             
                    data_objeto = ApiBancoCenrtal._data_retroativa(data=data_objeto, semana=data_formatada[0])
            else:
                # Outros erros, finaliza o loop
                break
    
    def _trata_resposta_dolar() -> list:          
        data_formatada = ApiBancoCenrtal._verifica_dia_da_semana()            
        cotacao_compra, cotacao_venda, data_atual = ApiBancoCenrtal._obter_cotacoes_dolar()
        cot_g = "{:.4f}".format(cotacao_compra)
        cot_b = "{:.4f}".format(cotacao_venda)
        cot_m = (cotacao_compra + cotacao_venda) / 2
        cot_m = "{:.4f}".format(cot_m)
        cot_p = (cotacao_compra + cotacao_venda) / 2
        cot_p = "{:.4f}".format(cot_p)
        
        # Verifica se é Sabado ou Domingo
        if data_formatada[0] == 5:
            data_atual += timedelta(days=1)
        elif data_formatada[0] == 6:
            data_atual += timedelta(days=2)              
        
        data_cambio = data_atual.strftime("%d.%m.%Y")
        
        oData_cambio = [{
                    "c" : "G",
                    "cot": f"{cot_g}",
                    "data": f"{data_cambio}"
                },
                {               
                    "c" : "B",     
                    "cot": f"{cot_b}",
                    "data": f"{data_cambio}"
                },
                {                
                    "c" : "M",    
                    "cot": f"{cot_m}",
                    "data": f"{data_cambio}"
                },
                {        
                    "c" : "P",            
                    "cot": f"{cot_p}",
                    "data": f"{data_cambio}"
                }]
        
        return oData_cambio    
    
    def retorna_payloads() -> list:  
        oData_cambio = ApiBancoCenrtal._trata_resposta_dolar()
        oData = []
        for cambio in oData_cambio:
            oData.append({
                "Kurst" : f"{cambio['c']}",
                "Fcurr" : "USD",
                "Tcurr" : "BRL",
                "Gdatu" : f"{cambio['data']}",
                "Ukurs" : f"{cambio['cot']}"
                })
        return oData
    
    @staticmethod
    def _verifica_dia_da_semana():     
        semana = ("Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo")  
         
        data_atual = datetime.now().strftime("%m-%d-%Y")        
        
        dia_da_semana = datetime.now().weekday()
        data_atual_formatada = datetime.now().strftime("%d/%m/%Y")
        
        print('Hoje é {}, dia {}!'.format(semana[dia_da_semana], data_atual_formatada))
        
        return [dia_da_semana, semana[dia_da_semana], data_atual]
    
    def _data_retroativa(data, semana):
        if semana == 6:    
            return  data - timedelta(days=2)
        else:
            return data - timedelta(days=1)
        

