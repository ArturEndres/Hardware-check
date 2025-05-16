import os
import platform
import socket
import uuid
import psutil
import subprocess
from datetime import datetime

def executar_powershell(comando):
    try:
        resultado = subprocess.run(["powershell", "-Command", comando], capture_output=True, text=True, encoding='utf-8')
        return resultado.stdout.strip()
    except Exception:
        return ""

def limpar_linhas_saida(saida):
    return [linha.strip() for linha in saida.splitlines() if linha.strip()]

# HARDWARE
def get_gpu():
    return executar_powershell("(Get-CimInstance Win32_VideoController).Name") or "Não encontrado"

def get_cpu():
    return executar_powershell("(Get-CimInstance Win32_Processor).Name") or "Não encontrado"

def get_mobo():
    return executar_powershell("(Get-CimInstance Win32_BaseBoard).Product") or "Não encontrado"

def get_ram_info():
    try:
        ram = psutil.virtual_memory()
        return f"{round(ram.total / (1024 ** 3), 2)} GB"
    except:
        return "Não encontrado"

def get_ram_slots():
    saida = executar_powershell("(Get-CimInstance Win32_PhysicalMemory | Select-Object -ExpandProperty BankLabel)")
    linhas = limpar_linhas_saida(saida)
    return len(linhas) if linhas else "Não encontrado"

def get_serial():
    return executar_powershell("(Get-CimInstance Win32_BIOS).SerialNumber") or "Não encontrado"

def get_disk_info():
    try:
        modelos = limpar_linhas_saida(executar_powershell("(Get-CimInstance Win32_DiskDrive).Model"))
        infos = []
        for i, part in enumerate(psutil.disk_partitions()):
            if 'cdrom' in part.opts or not os.path.exists(part.mountpoint):
                continue
            uso = psutil.disk_usage(part.mountpoint)
            total = round(uso.total / (1024 ** 3), 2)
            livre = round(uso.free / (1024 ** 3), 2)
            modelo = modelos[i] if i < len(modelos) else "Desconhecido"
            infos.append(f"{modelo} - Total: {total} GB / Livre: {livre} GB")
        return '\n'.join(infos) if infos else "Não encontrado"
    except:
        return "Não encontrado"

def get_pc_manufacturer():
    fabricante = executar_powershell("(Get-CimInstance Win32_ComputerSystem).Manufacturer")
    if any(x in fabricante for x in ["OEM", "To Be Filled", ""]) or fabricante == "":
        fabricante = executar_powershell("(Get-CimInstance Win32_BaseBoard).Manufacturer")
    return fabricante or "Desconhecido"

# REDE
def get_mac_ip():
    try:
        mac = ':'.join(f'{(uuid.getnode() >> i) & 0xff:02x}' for i in range(40, -1, -8)).upper()
        ip = socket.gethostbyname(socket.gethostname())
        return mac, ip
    except:
        return "Não encontrado", "Não encontrado"

def get_dns():
    saida = executar_powershell("Get-DnsClientServerAddress | Select-Object -ExpandProperty ServerAddresses")
    linhas = limpar_linhas_saida(saida)
    return ', '.join(linhas) if linhas else "Não encontrado"

def get_dhcp_status():
    saida = executar_powershell("(Get-NetIPInterface | Where-Object {$_.AddressFamily -eq 'IPv4'}).Dhcp")
    if "Enabled" in saida:
        return "DINÂMICO"
    elif "Disabled" in saida:
        return "FIXO"
    return "Não encontrado"

def get_network_adapter():
    return executar_powershell("(Get-NetAdapter | Where-Object { $_.Status -eq 'Up' }).Name") or "Não encontrado"

# SISTEMA
def get_hostname():
    return socket.gethostname()

def get_os_info():
    nome = executar_powershell("(Get-CimInstance Win32_OperatingSystem).Caption").strip()
    versao = executar_powershell("(Get-CimInstance Win32_OperatingSystem).Version").strip()
    build = executar_powershell("(Get-ItemProperty -Path 'HKLM:\\Software\\Microsoft\\Windows NT\\CurrentVersion').CurrentBuild").strip()
    release = executar_powershell("(Get-ItemProperty -Path 'HKLM:\\Software\\Microsoft\\Windows NT\\CurrentVersion').DisplayVersion").strip()
    return f"{nome} (Build {build}, Release {release})", versao

# MAIN
def main():
    nome = input("Digite o seu nome: ").strip()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    mac, ip = get_mac_ip()
    os_nome, os_versao = get_os_info()

    dados = {
        "Data e Hora": timestamp,
        "Fabricante do PC": get_pc_manufacturer(),
        "MOBO": get_mobo(),
        "CPU": get_cpu(),
        "GPU": get_gpu(),
        "RAM": get_ram_info(),
        "Qtd. Pentes de RAM": get_ram_slots(),
        "Disco(s)": get_disk_info(),
        "Número Serial": get_serial(),

        "MAC Address": mac,
        "IP Address": ip,
        "DNS": get_dns(),
        "DHCP Status": get_dhcp_status(),
        "Adaptador de Rede": get_network_adapter(),
        "Hostname": get_hostname(),

        "Sistema Operacional": os_nome,
        "Versão do SO": os_versao
    }

    caminho_arquivo = os.path.join(os.getcwd(), f"{nome}.txt")
    with open(caminho_arquivo, "w", encoding="utf-8") as f:
        f.write(f"Data e Hora da coleta: {dados['Data e Hora']}\n\n")

        f.write("=== HARDWARE ===\n")
        for chave in ["Fabricante do PC", "MOBO", "CPU", "GPU", "RAM", "Qtd. Pentes de RAM", "Disco(s)", "Número Serial"]:
            f.write(f"{chave}: {dados[chave]}\n")

        f.write("\n=== REDE ===\n")
        for chave in ["MAC Address", "IP Address", "DNS", "DHCP Status", "Adaptador de Rede", "Hostname"]:
            f.write(f"{chave}: {dados[chave]}\n")

        f.write("\n=== SISTEMA ===\n")
        f.write(f"Sistema Operacional: {dados['Sistema Operacional']}\n")
        f.write(f"Versão do SO: {dados['Versão do SO']}\n")

    print(f"\nArquivo salvo em: {caminho_arquivo}")

if __name__ == "__main__":
    main()
