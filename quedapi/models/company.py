# coding: utf-8

"""
    Querido Diário

    API to access the gazettes from all Brazilian cities

    The version of the OpenAPI document: 0.17.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictStr

class Company(BaseModel):
    """
    Company
    """
    cnpj_basico: StrictStr = Field(...)
    cnpj_ordem: StrictStr = Field(...)
    cnpj_dv: StrictStr = Field(...)
    cnpj_completo: StrictStr = Field(...)
    cnpj_completo_apenas_numeros: StrictStr = Field(...)
    identificador_matriz_filial: Optional[StrictStr] = None
    nome_fantasia: Optional[StrictStr] = None
    situacao_cadastral: Optional[StrictStr] = None
    data_situacao_cadastral: Optional[StrictStr] = None
    motivo_situacao_cadastral: Optional[StrictStr] = None
    nome_cidade_exterior: Optional[StrictStr] = None
    data_inicio_atividade: Optional[StrictStr] = None
    cnae_fiscal_secundario: Optional[StrictStr] = None
    tipo_logradouro: Optional[StrictStr] = None
    logradouro: Optional[StrictStr] = None
    numero: Optional[StrictStr] = None
    complemento: Optional[StrictStr] = None
    bairro: Optional[StrictStr] = None
    cep: Optional[StrictStr] = None
    uf: Optional[StrictStr] = None
    ddd_telefone_1: Optional[StrictStr] = None
    ddd_telefone_2: Optional[StrictStr] = None
    ddd_telefone_fax: Optional[StrictStr] = None
    correio_eletronico: Optional[StrictStr] = None
    situacao_especial: Optional[StrictStr] = None
    data_situacao_especial: Optional[StrictStr] = None
    pais: Optional[StrictStr] = None
    municipio: Optional[StrictStr] = None
    razao_social: Optional[StrictStr] = None
    natureza_juridica: Optional[StrictStr] = None
    qualificacao_do_responsavel: Optional[StrictStr] = None
    capital_social: Optional[StrictStr] = None
    porte: Optional[StrictStr] = None
    ente_federativo_responsavel: Optional[StrictStr] = None
    opcao_pelo_simples: Optional[StrictStr] = None
    data_opcao_pelo_simples: Optional[StrictStr] = None
    data_exclusao_pelo_simples: Optional[StrictStr] = None
    opcao_pelo_mei: Optional[StrictStr] = None
    data_opcao_pelo_mei: Optional[StrictStr] = None
    data_exclusao_pelo_mei: Optional[StrictStr] = None
    cnae: Optional[StrictStr] = None
    __properties = ["cnpj_basico", "cnpj_ordem", "cnpj_dv", "cnpj_completo", "cnpj_completo_apenas_numeros", "identificador_matriz_filial", "nome_fantasia", "situacao_cadastral", "data_situacao_cadastral", "motivo_situacao_cadastral", "nome_cidade_exterior", "data_inicio_atividade", "cnae_fiscal_secundario", "tipo_logradouro", "logradouro", "numero", "complemento", "bairro", "cep", "uf", "ddd_telefone_1", "ddd_telefone_2", "ddd_telefone_fax", "correio_eletronico", "situacao_especial", "data_situacao_especial", "pais", "municipio", "razao_social", "natureza_juridica", "qualificacao_do_responsavel", "capital_social", "porte", "ente_federativo_responsavel", "opcao_pelo_simples", "data_opcao_pelo_simples", "data_exclusao_pelo_simples", "opcao_pelo_mei", "data_opcao_pelo_mei", "data_exclusao_pelo_mei", "cnae"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Company:
        """Create an instance of Company from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Company:
        """Create an instance of Company from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Company.parse_obj(obj)

        _obj = Company.parse_obj({
            "cnpj_basico": obj.get("cnpj_basico"),
            "cnpj_ordem": obj.get("cnpj_ordem"),
            "cnpj_dv": obj.get("cnpj_dv"),
            "cnpj_completo": obj.get("cnpj_completo"),
            "cnpj_completo_apenas_numeros": obj.get("cnpj_completo_apenas_numeros"),
            "identificador_matriz_filial": obj.get("identificador_matriz_filial"),
            "nome_fantasia": obj.get("nome_fantasia"),
            "situacao_cadastral": obj.get("situacao_cadastral"),
            "data_situacao_cadastral": obj.get("data_situacao_cadastral"),
            "motivo_situacao_cadastral": obj.get("motivo_situacao_cadastral"),
            "nome_cidade_exterior": obj.get("nome_cidade_exterior"),
            "data_inicio_atividade": obj.get("data_inicio_atividade"),
            "cnae_fiscal_secundario": obj.get("cnae_fiscal_secundario"),
            "tipo_logradouro": obj.get("tipo_logradouro"),
            "logradouro": obj.get("logradouro"),
            "numero": obj.get("numero"),
            "complemento": obj.get("complemento"),
            "bairro": obj.get("bairro"),
            "cep": obj.get("cep"),
            "uf": obj.get("uf"),
            "ddd_telefone_1": obj.get("ddd_telefone_1"),
            "ddd_telefone_2": obj.get("ddd_telefone_2"),
            "ddd_telefone_fax": obj.get("ddd_telefone_fax"),
            "correio_eletronico": obj.get("correio_eletronico"),
            "situacao_especial": obj.get("situacao_especial"),
            "data_situacao_especial": obj.get("data_situacao_especial"),
            "pais": obj.get("pais"),
            "municipio": obj.get("municipio"),
            "razao_social": obj.get("razao_social"),
            "natureza_juridica": obj.get("natureza_juridica"),
            "qualificacao_do_responsavel": obj.get("qualificacao_do_responsavel"),
            "capital_social": obj.get("capital_social"),
            "porte": obj.get("porte"),
            "ente_federativo_responsavel": obj.get("ente_federativo_responsavel"),
            "opcao_pelo_simples": obj.get("opcao_pelo_simples"),
            "data_opcao_pelo_simples": obj.get("data_opcao_pelo_simples"),
            "data_exclusao_pelo_simples": obj.get("data_exclusao_pelo_simples"),
            "opcao_pelo_mei": obj.get("opcao_pelo_mei"),
            "data_opcao_pelo_mei": obj.get("data_opcao_pelo_mei"),
            "data_exclusao_pelo_mei": obj.get("data_exclusao_pelo_mei"),
            "cnae": obj.get("cnae")
        })
        return _obj


