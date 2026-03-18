from tools import cancel_order, send_email

async def execute_plan(plan):
    results = []
    
    for task in plan:
        tool_name = task.get("tool")
        args = task.get("arguments", {})
        
        print(f"Executing: {tool_name} with args {args}")

        if tool_name == "cancel_order":
            result = await cancel_order(args.get("order_id"))
            results.append(result)
            
            # Guardrail: If cancellation fails, stop the workflow
            if result["status"] == "error":
                results.append({"status": "skipped", "message": "Email not sent because order cancellation failed."})
                break 
                
        elif tool_name == "send_email":
            result = await send_email(args.get("email"), args.get("message"))
            results.append(result)

    return results