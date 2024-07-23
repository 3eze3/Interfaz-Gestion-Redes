#!/usr/bin/python3

from contextlib import nullcontext
import re
import subprocess
import socket
import ipaddress
import threading
import sys


def obtner_ip(dominio):
    try:
        ip = socket.gethostbyname(dominio)
        return ip
    except socket.gaierror:
        return None


def ping(ip):

    if ip is None or ip is nullcontext:
        sys.exit(1)

    try:
        subprocess.check_output(['ping', '-c', '1', str(ip)],
                                stderr=subprocess.STDOUT, timeout=1)
        return True
    except subprocess.CalledProcessError:
        return False
    except subprocess.TimeoutExpired:
        return False


def check_ip(ip):
    if ping(ip):
        print(f"[*] Host {ip} - Active")
    else:
        pass


def check_devices(network):
    """ Escanea una subred para ver qué dispositivos están activos. """
    if network is None or network is nullcontext:
        sys.exit(1)
    ip_base = str(ipaddress.IPv4Network(network, strict=False).network_address)
    ip_base_parts = ip_base.split('.')
    base_prefix = '.'.join(ip_base_parts[:3])

    threads = []

    for octet in range(1, 255):
        ip = f"{base_prefix}.{octet}"
        thread = threading.Thread(target=check_ip, args=(ip,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print(f"\n[*] Escaneo de la {network} finalizado con exito! \n")
    sys.exit(0)


def is_ipv4(ip):

    ptt_ip = re.compile(r'^(\d{1,3}\.){3}\d{1,3}$')

    if ptt_ip.match(ip):
        return True
    return False


def sn_ping(addr):
    print("\n[*] Escanea un rango de direcciones IP "
          "en una subred para ver si están activas.\n")
    print("\n[*] Escanea puertos específicos en cada IP "
          "para ver si están abiertos.\n")
    if not is_ipv4(addr):
        addr = obtner_ip(addr)
        check_ip(addr)
        sys.exit(0)
    else:
        check_devices(str(addr))
