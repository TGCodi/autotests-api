import socket



def server():
    # Создаём TCP-сокет
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Привязываем его к адресу и порту
    server_adress = ('localhost', 12345)
    server_socket.bind(server_adress)

    # Начинаем слушать входящие подключения 10
    server_socket.listen(10)
    print("Сервер запущен и ждёт подключения")

    # Список для хранения истории сообщений
    messages = []

    while True:
        # Принимаем соединение от клиента
        client_socket, client_address = server_socket.accept()
        print(f"пользователь с адресом: {client_address} подключился к серверу")

        # Получаем данные от клиента
        data = client_socket.recv(1024).decode()
        print(f"Пользователь с адресом: {client_address} отправил сообщение: {data}")

        # Отправляем ответ клиенту
        messages.append(data)
        client_socket.send('\n'.join(messages).encode())

        # Закрываем сединение с клиентом
        client_socket.close()

if __name__ == "__main__":
    server()