from typing import Literal
from pydantic import BaseModel, ValidationError

# Testing data
mock_orders = [
    {"order_id": 101, "price": "29.99", "item_name": "Logitech Mouse", "status": "PENDING"},
    {"order_id": 102, "price": 1099.00, "item_name": "4K Monitor", "status": "INVALID_STATUS"},
    {"order_id": "one-hundred-three", "price": 5.50, "item_name": "HDMI Cable", "status": "SHIPPED"}
]

# 1. Define the Firewall Schema, THIS IS THE CORE CONFIG
class OrderModel(BaseModel):
    order_id: int
    price: float
    item_name: str
    status: Literal["PENDING", "SHIPPED", "DELIVERED"]


# 2. Pass data through the firewall
for o in mock_orders:
    print(o)
    try:
        order = OrderModel(**o)    
        print(f"Order {order.order_id} is clean.")
    except ValidationError as e:
        # Loop through the structured errors Pydantic provides
        for error in e.errors():
            field = " -> ".join(str(loc) for loc in error["loc"])
            error_msg = error["msg"]
            print(f"Field [{field}]: {error_msg}")
