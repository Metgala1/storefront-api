from fastapi import APIRouter, WebSocket, WebSocketDisconnect

router = APIRouter(tags=["websocket"])

@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    
    try:
        
        while True:
            maessage = await websocket.receive_text()
            
            await websocket.send_text(
                f"Server received: {maessage}"
            )
    except WebSocketDisconnect:
        print("Client disconnected")
        
