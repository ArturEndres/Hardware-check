# 🖥️ Coletor de Informações do Sistema (Windows)

Este script em Python coleta uma variedade de informações detalhadas de um computador com sistema operacional **Windows**, organizando os dados de **hardware**, **rede** e **sistema operacional** em um arquivo `.txt`, feito com o intuito de coletar e gerenciar informações de hardware.

---

## 💡 Sobre o Projeto

> Este projeto foi idealizado por **Artur** e todo o código foi implementado com **auxílio do ChatGPT**, a partir das minhas ideias. O objetivo é criar uma ferramenta prática para levantamento técnico de máquinas com Windows, útil especialmente para inventários de TI, suporte técnico e manutenção.

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

```txt
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

## 🚀 Como Usar

1. Clone este repositório ou copie o arquivo `.py` para o seu computador.  
2. Execute o script com Python.  
3. Digite o nome quando solicitado.  
4. O relatório será salvo na mesma pasta com o nome `seunome.txt`.

---

## 📌 Observações Técnicas

- O script faz chamadas ao PowerShell para coletar informações via WMI e comandos nativos do Windows.  
- O script trata erros de forma simples, retornando "Não encontrado" caso algo falhe.  
- As informações são formatadas de forma legível e separadas por categoria.

---

## 👤 Autor

Este projeto foi idealizado por Artur e desenvolvido em colaboração com ChatGPT (OpenAI), com base nas ideias e necessidades definidas por Artur.

---

## 📝 Licença

Este projeto é de uso livre para fins pessoais e educacionais.  
Caso deseje contribuir ou aprimorar, fique à vontade para fazer um fork ou abrir um pull request!
