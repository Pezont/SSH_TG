import socket
import subprocess


def start_listener():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 22))
    server_socket.listen(5)

    print("Скрипт слежения за портом 22 запущен.")

    while True:
        client_socket, addr = server_socket.accept()
        message = f"Обнаружено подключение к порту 22 с адреса {addr[0]}:{addr[1]}"
        subprocess.run(["python3", "tg_bot.py", message])
        client_socket.close()


if __name__ == "__main__":
    start_listener()
