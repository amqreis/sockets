# Estudo de Sockets em Python - Comunicação TCP

Este projeto faz parte do meu portfólio de estudos em **Fundamentos de Redes para DevOps**, focado em infraestrutura de redes e comunicação entre processos em ambiente Linux (WSL2).

## 🎯 Objetivos da Aula
* Implementar um servidor socket utilizando a biblioteca nativa `socket` do Python.
* Compreender o fluxo de comunicação **TCP/IP** (Handshake, Escuta e Recebimento de Dados).
* Praticar a depuração de serviços de rede e gestão de processos no Linux.

## 🛠️ Tecnologias e Ferramentas
* **Linguagem:** Python 3.
* **Ambiente:** VS Code com integração **WSL: Ubuntu**.
* **Ferramentas de Redes:** `nc` (Netcat) para testes de conectividade e `ss` / `lsof` para monitoramento de portas.

## 🚀 O que foi desenvolvido
### 1. Servidor Socket (`server.py`)
Desenvolvimento de um script que atua na camada de transporte (TCP), configurado para processar múltiplas mensagens e exibir dinamicamente o host de origem (IP e porta efêmera).

### 2. Troubleshooting Aplicado
* **Gestão de Portas Ocupadas:** Uso de `lsof` e `kill -9` para liberar portas travadas.
* **Depuração de Lógica:** Ajuste de indentação para garantir o fluxo de recepção de dados.
* **Permissões Linux:** Configuração de execução via `chmod +x`.
