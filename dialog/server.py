import asyncio
import websockets
import json

salas = {}
clients_video = {}


async def server_texto(websocket, path):
    sala = path.strip("/") or "default"
    if sala not in salas:
        salas[sala] = {"texto": set(), "video": set()}
    salas[sala]["texto"].add(websocket)

    try:
        async for message in websocket:
            for client in salas[sala]["texto"]:
                if client != websocket:
                    await client.send(message)
    finally:
        salas[sala]["texto"].remove(websocket)
        if not salas[sala]["texto"] and not salas[sala]["video"]:
            del salas[sala]


async def listar_salas_disponiveis(websocket, path):
    salas_disponiveis = list(salas.keys())
    await websocket.send(json.dumps(salas_disponiveis))


async def server_video(websocket, path):
    sala = path.strip("/") or "default"
    if sala not in salas:
        salas[sala] = {"texto": set(), "video": set()}
    salas[sala]["video"].add(websocket)

    try:
        async for message in websocket:
            for client in salas[sala]["video"]:
                if client != websocket:
                    await client.send(message)
    finally:
        salas[sala]["video"].remove(websocket)
        if not salas[sala]["texto"] and not salas[sala]["video"]:
            del salas[sala]


start_server = websockets.serve(server_texto, "localhost", 8765)
start_listar_salas = websockets.serve(listar_salas_disponiveis, "localhost", 8766)
start_server_video = websockets.serve(server_video, "localhost", 8767)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_until_complete(start_listar_salas)
asyncio.get_event_loop().run_until_complete(start_server_video)
asyncio.get_event_loop().run_forever()
