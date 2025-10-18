from __future__ import annotations
from uuid import UUID, uuid4
from datetime import datetime
from pydantic import BaseModel, Field, conint


class CartItem(BaseModel):
    """
    Represents a user's shopping cart item before checkout.
    Each user can have multiple cart items (one per product).
    """
    id: UUID = Field(default_factory=uuid4, description="Cart item ID.")
    user_id: UUID = Field(..., description="User who owns this cart.")
    product_id: UUID = Field(..., description="Product added to cart.")
    quantity: conint(gt=0) = Field(..., description="Quantity of the product.")
    added_at: datetime = Field(default_factory=datetime.utcnow, description="Timestamp when added to cart.")

    model_config = {
        "json_schema_extra": {
            "example": {
                "id": "c1111111-1111-4111-8111-111111111111",
                "user_id": "u1111111-1111-4111-8111-111111111111",
                "product_id": "p2222222-2222-4222-8222-222222222222",
                "quantity": 2,
                "added_at": "2025-01-15T10:20:30Z"
            }
        }
    }
