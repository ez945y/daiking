from fastapi import FastAPI, WebSocket

app = FastAPI()

@app.websocket("/wwss")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
