# 🧾 Inventário de Sistema em Python (via PowerShell)

Este repositório contém um script em Python para coletar e salvar informações detalhadas de hardware, rede e sistema operacional de um computador com **Windows**, utilizando **PowerShell** e a biblioteca `psutil`.

> ⚠️ **Este código foi gerado integralmente com o auxílio do ChatGPT (OpenAI).** Nenhuma linha foi escrita sem apoio da IA.

---

## ✅ Funcionalidades

- Coleta e salva automaticamente:
  - ✅ Fabricante do computador e da placa-mãe (MOBO)
  - ✅ Informações da CPU e GPU
  - ✅ Capacidade e quantidade de pentes de RAM
  - ✅ Modelo dos discos, espaço total e livre
  - ✅ Número de série (BIOS)
  - ✅ Endereço MAC e IP
  - ✅ DNS configurado
  - ✅ Status do DHCP (IP fixo ou dinâmico)
  - ✅ Nome do adaptador de rede
  - ✅ Hostname
  - ✅ Nome, versão e build do sistema operacional

- Gera um arquivo `.txt` com todas as informações organizadas.

---

## ▶️ Como usar

1. Tenha o **Python 3.6+** instalado.
2. Instale a biblioteca `psutil`, se ainda não tiver:
   ```bash
   pip install psutil
Execute o script:

bash
Copiar
Editar
python inventario.py
Digite seu nome quando solicitado. Um arquivo com o nome informado será salvo no mesmo diretório.

📄 Exemplo de saída
yaml
Copiar
Editar
Data e Hora da coleta: 2025-05-15 14:30:21

=== HARDWARE ===
Fabricante do PC: Dell Inc.
MOBO: 0F4GRK
CPU: Intel(R) Core(TM) i7-9700 CPU @ 3.00GHz
GPU: NVIDIA GeForce GTX 1650
RAM: 16.0 GB
Qtd. Pentes de RAM: 2
Disco(s): WDC SSD 500GB - Total: 500 GB / Livre: 200 GB
Número Serial: 1234ABCD5678

=== REDE ===
MAC Address: 00:1A:2B:3C:4D:5E
IP Address: 192.168.0.105
DNS: 8.8.8.8, 1.1.1.1
DHCP Status: DINÂMICO
Adaptador de Rede: Wi-Fi
Hostname: DESKTOP-XYZ123

=== SISTEMA ===
Sistema Operacional: Microsoft Windows 10 Pro (Build 19045, Release 22H2)
Versão do SO: 10.0.19045

📌 Observações
Compatível apenas com Windows (uso de comandos PowerShell).

Pode retornar "Não encontrado" em dispositivos com permissões restritas ou drivers ausentes.

Requer que o PowerShell esteja instalado e acessível via terminal.

📜 Licença
Distribuído sob a Licença MIT.
Sinta-se livre para usar, modificar e distribuir. Se manter a essência do projeto, considere manter a menção ao uso do ChatGPT 🤖.

