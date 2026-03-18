import asyncio
import random

async def cancel_order(order_id: str):
    if random.random() < 0.20:
        return {"status": "error", "message": f"Failed to cancel order {order_id}"}
    
    await asyncio.sleep(0.5) 
    return {"status": "success", "message": f"Order {order_id} cancelled successfully"}

async def send_email(email: str, message: str):
    await asyncio.sleep(1)
    return {"status": "success", "message": f"Email sent to {email}"}
