# Boto3 Snapshot Manager

![Python](https://img.shields.io/badge/python-3.7%2C%203.8%2C%203.9-blue)
![License](https://img.shields.io/github/license/gabrielsantos-cloud/boto3-snapshot-manager)

Este repositório contém um script em Python para gerenciar snapshots (instantâneos) de volumes EBS (Elastic Block Store) na AWS utilizando o SDK Boto3.

## Funcionalidades

- **Criação de Snapshots:** Cria um snapshot para cada volume EBS especificado nas regiões da AWS configuradas.
- **Backup Automático:** Pode ser configurado para executar backups automáticos em intervalos definidos.
- **Limpeza de Snapshots Antigos:** Remove snapshots mais antigos que uma determinada idade configurável para gerenciar custos e otimizar o armazenamento.

## Requisitos

- Python 3.7 ou superior
- Pacotes necessários: boto3, datetime

## Configuração

1. **Instalação de Dependências:**
   ```bash
   pip install boto3
