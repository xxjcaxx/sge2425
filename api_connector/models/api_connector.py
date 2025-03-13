import requests
import json
from odoo import models, fields, api

class APIConnector(models.Model):
    _name = 'api.connector'
    _description = 'Conector a API externa'

    name = fields.Char(string="Nombre")
    response_data = fields.Text(string="Respuesta")

    @api.model
    def call_api(self):
        url = "https://api.ejemplo.com/datos"
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer TU_TOKEN'
        }
        payload = {
            'param1': 'valor1',
            'param2': 'valor2'
        }
        response = requests.post(url, data=json.dumps(payload), headers=headers)

        if response.status_code == 200:
            self.create({'name': 'Llamada API', 'response_data': response.text})
            return response.json()
        else:
            return {'error': response.text}
