# 🖥️ Hardware Check - Windows

Este script em Python coleta uma variedade de informações detalhadas de um computador com sistema operacional **Windows**, organizando os dados de **hardware**, **rede** e **sistema operacional** em um arquivo `.txt`, feito com o intuito de coletar e gerenciar informações de hardware.

---

> **🧠 Projeto inteiramente desenvolvido com auxílio do ChatGPT**  
> A construção completa deste projeto — HTML, CSS e JavaScript — foi feita através de instruções dadas por mim ao ChatGPT.
> Nenhuma linha de código foi copiada de outro lugar ou template pronto. Todo o layout, lógica e estilo foram moldados a partir dos meus prompts e ideias.

---

## ⚙️ Funcionalidades

O script coleta as seguintes informações:

### Nome
- Primeiramente, pergunte o nome da pessoa
  
### 🔧 Hardware
- Fabricante do computador  
- Placa-mãe (MOBO)  
- CPU  
- GPU  
- Quantidade de RAM total  
- Quantidade de pentes de RAM  
- Discos (modelo, tamanho total e espaço livre)  
- Número de série do equipamento  

### 🌐 Rede
- Endereço MAC  
- Endereço IP  
- Servidores DNS  
- Status do DHCP (dinâmico ou fixo)  
- Nome do adaptador de rede ativo  
- Nome do host (hostname)  

### 🖥️ Sistema Operacional
- Nome e versão do sistema operacional  
- Build e release do Windows  

---

## 📁 Saída

Após a execução, será gerado um arquivo `.txt` no mesmo diretório do script, com nome baseado no nome digitado pelo usuário (ex: `joao.txt`). Esse arquivo contém todas as informações organizadas por seção:

```
=== HARDWARE ===
Fabricante do PC: ...
MOBO: ...
CPU: ...
GPU: ...
RAM: ...
Qtd. Pentes de RAM: ...
Disco(s): ...
Número Serial: ...

=== REDE ===
MAC Address: ...
IP Address: ...
DNS: ...
DHCP Status: ...
Adaptador de Rede: ...
Hostname: ...

=== SISTEMA ===
Sistema Operacional: ...
Versão do SO: ...
```
---

## Módulos Python

- os  
- platform  
- socket  
- uuid  
- psutil  
- subprocess  
- datetime

---

## 📌 Observações Técnicas

- O script faz chamadas ao PowerShell para coletar informações via WMI e comandos nativos do Windows.  
- O script trata erros de forma simples, retornando "Não encontrado" caso algo falhe.  
- As informações são formatadas de forma legível e separadas por categoria.

---

## 📝 Licença

Este projeto é de uso livre para fins pessoais e educacionais.  
Caso deseje contribuir ou aprimorar, fique à vontade.
