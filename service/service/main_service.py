import time
import json


from loguru import logger
from service.constants import mensagens
import pandas as pd
import requests


from service.util.doc_swagger import INPUT_MAIN_SERVICE


class BancoDeDadosServico():

    def __init__(self):
        logger.debug(mensagens.INICIO_LOAD_SERVICO)
        self.load_servico()

    def load_servico(self):
        """"
        Carrega o serviço
        """

        logger.debug(mensagens.FIM_LOAD_SERVICO)

    def executar_rest(self, texts):
        response = {}

        logger.debug(mensagens.INICIO_SERVICO)
        start_time = time.time()

       
        userdata = texts
        requisicao = requests.post("https://projetofinalcoreibm-default-rtdb.firebaseio.com/.json", json=userdata)
        print(requisicao)
        print(requisicao.json)

        
        logger.debug(mensagens.FIM_SERVICO)
        logger.debug(f"Fim de todas as predições em {time.time()-start_time}")

        df_response = pd.DataFrame(texts)
        
        #df_response = df_response.drop(columns=['nome'])

        response = {
                     "cadastro": json.loads(df_response.to_json(
                                                                orient='records', force_ascii=True))}

        return response


    

    