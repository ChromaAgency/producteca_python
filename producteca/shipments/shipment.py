from typing import List, Optional
from pydantic import BaseModel
import requests
from producteca.abstract.abstract_dataclass import BaseService
from dataclasses import dataclass


class ShipmentProduct(BaseModel):
    product: int
    variation: Optional[int] = None
    quantity: int


class ShipmentMethod(BaseModel):
    trackingNumber: Optional[str] = None
    trackingUrl: Optional[str] = None
    courier: Optional[str] = None
    mode: Optional[str] = None
    cost: Optional[float] = None
    type: Optional[str] = None
    eta: Optional[int] = None
    status: Optional[str] = None


class ShipmentIntegration(BaseModel):
    id: Optional[int] = None
    integrationId: Optional[str] = None
    app: Optional[int] = None
    status: str


class Shipment(BaseModel):
    date: Optional[str] = None
    products: Optional[List[ShipmentProduct]] = None
    method: Optional[ShipmentMethod] = None
    integration: Optional[ShipmentIntegration] = None


@dataclass
class ShipmentService(BaseService):

    def create(self, sale_order_id: int, payload: "Shipment") -> "Shipment":
        url = self.config.get_endpoint(f"salesorders/{sale_order_id}/shipments")
        res = requests.post(url, data=payload.model_dump_json(exclude_none=True), headers=self.config.headers)
        return Shipment(**res.json())

    def update(self, sale_order_id: int, shipment_id: str, payload: "Shipment") -> "Shipment":
        url = self.config.get_endpoint(f"salesorders/{sale_order_id}/shipments/{shipment_id}")
        res = requests.put(url, data=payload.model_dump_json(exclude_none=True), headers=self.config.headers)
        return Shipment(**res.json())
