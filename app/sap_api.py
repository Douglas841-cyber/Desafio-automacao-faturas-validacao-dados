

def criar_po_sap(dados_fatura):
    # Simula envio e retorno da API SAP
    print(f"Simulando envio da PO com dados: {dados_fatura}")
    return {"status": 200, "message": "PO criada (simulada)"}


### Estrutura para usar a API do SAP
'''
import requests
import json

def criar_po_sap(dados):
    url = "https://sap-api.fake/purchase-orders"
    headers = {"Content-Type": "application/json"}

    body = {
        "cnpj": dados["cnpj"],
        "numero_contrato": dados["contrato"],
        "valor": dados["valor"],
        "data_vencimento": dados["vencimento"]
    }

    response = requests.post(url, headers=headers, data=json.dumps(body))
    return response.status_code, response.text

'''