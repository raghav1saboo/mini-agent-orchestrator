import re
import asyncio

async def create_plan(user_request: str):
    """
    Mocks an LLM by parsing a natural language request into a sequence of tasks
    using regex instead of an external API call.
    """
    await asyncio.sleep(0.5)
    
    tasks = []
    
    order_match = re.search(r'#?(\d+)', user_request)
    email_match = re.search(r'[\w\.-]+@[\w\.-]+\.\w+', user_request)

    if order_match:
        order_id = order_match.group(1)
        tasks.append({
            "tool": "cancel_order", 
            "arguments": {"order_id": order_id}
        })

    if email_match:
        email_addr = email_match.group(0)
        tasks.append({
            "tool": "send_email", 
            "arguments": {
                "email": email_addr, 
                "message": f"Confirmation: Order {order_id if order_match else 'unknown'} has been processed."
            }
        })

    if not tasks:
        return {"error": "Could not identify any tasks in your request."}

    return tasks