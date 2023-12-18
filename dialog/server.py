import asyncio
import websockets
import json

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


async def listar_salas_disponiveis(websocket, path):
    salas_disponiveis = list(salas.keys())
    await websocket.send(json.dumps(salas_disponiveis))


start_server = websockets.serve(server, "192.168.0.112", 8765)
start_listar_salas = websockets.serve(listar_salas_disponiveis, "192.168.0.112", 8766)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_until_complete(start_listar_salas)
asyncio.get_event_loop().run_forever()
