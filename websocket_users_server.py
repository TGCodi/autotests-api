import asyncio

import websockets
from websockets import ServerConnection

async def echo(websoket: ServerConnection):
    async for message in websoket:
        print(f"Получено сообщение: {message}")

        for i in range(1, 6):
            response = f"{i} Сообщение пользователя: {message}"
            await websoket.send(response)

async def main():
    server = await websockets.serve(echo, "localhost", 8765)
    print("WebSocket сервер запущен на ws://localhost:8765")
    await server.wait_closed()

asyncio.run(main())
