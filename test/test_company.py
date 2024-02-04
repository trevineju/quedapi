# coding: utf-8

"""
    Querido Diário

    API to access the gazettes from all Brazilian cities

    The version of the OpenAPI document: 0.17.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from openapi_client.models.company import Company  # noqa: E501

class TestCompany(unittest.TestCase):
    """Company unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Company:
        """Test Company
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Company`
        """
        model = Company()  # noqa: E501
        if include_optional:
            return Company(
                cnpj_basico = '',
                cnpj_ordem = '',
                cnpj_dv = '',
                cnpj_completo = '',
                cnpj_completo_apenas_numeros = '',
                identificador_matriz_filial = '',
                nome_fantasia = '',
                situacao_cadastral = '',
                data_situacao_cadastral = '',
                motivo_situacao_cadastral = '',
                nome_cidade_exterior = '',
                data_inicio_atividade = '',
                cnae_fiscal_secundario = '',
                tipo_logradouro = '',
                logradouro = '',
                numero = '',
                complemento = '',
                bairro = '',
                cep = '',
                uf = '',
                ddd_telefone_1 = '',
                ddd_telefone_2 = '',
                ddd_telefone_fax = '',
                correio_eletronico = '',
                situacao_especial = '',
                data_situacao_especial = '',
                pais = '',
                municipio = '',
                razao_social = '',
                natureza_juridica = '',
                qualificacao_do_responsavel = '',
                capital_social = '',
                porte = '',
                ente_federativo_responsavel = '',
                opcao_pelo_simples = '',
                data_opcao_pelo_simples = '',
                data_exclusao_pelo_simples = '',
                opcao_pelo_mei = '',
                data_opcao_pelo_mei = '',
                data_exclusao_pelo_mei = '',
                cnae = ''
            )
        else:
            return Company(
                cnpj_basico = '',
                cnpj_ordem = '',
                cnpj_dv = '',
                cnpj_completo = '',
                cnpj_completo_apenas_numeros = '',
        )
        """

    def testCompany(self):
        """Test Company"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()