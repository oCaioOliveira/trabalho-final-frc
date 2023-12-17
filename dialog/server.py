import asyncio
import websockets

salas = {}


async def server(websocket, path):
    sala = path.strip("/")

    if sala not in salas:
        salas[sala] = set()

    salas[sala].add(websocket)

    try:
        async for message in websocket:
            for client in salas[sala]:
                if client != websocket:
                    await client.send(message)
    finally:
        salas[sala].remove(websocket)


start_server = websockets.serve(server, "ip-desejado", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
