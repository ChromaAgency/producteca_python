from pydantic import BaseModel, Field
from typing import Optional
import requests
from producteca.abstract.abstract_dataclass import BaseService


class PaymentCard(BaseModel):
    paymentNetwork: Optional[str] = None
    firstSixDigits: Optional[int] = None
    lastFourDigits: Optional[int] = None
    cardholderIdentificationNumber: Optional[str] = None
    cardholderIdentificationType: Optional[str] = None
    cardholderName: Optional[str] = None


class PaymentIntegration(BaseModel):
    integrationId: str
    app: int


class Payment(BaseModel):
    date: str
    amount: float
    couponAmount: Optional[float] = None
    status: str
    method: str
    integration: Optional[PaymentIntegration] = None
    transactionFee: Optional[float] = None
    installments: Optional[int] = None
    card: Optional[PaymentCard] = None
    notes: Optional[str] = None
    hasCancelableStatus: bool
    id: Optional[int] = None


class PaymentService(BaseService):
    endpoint: str = Field(default='salesorders', exclude=True)

    def create(self, sale_order_id: int, payload: "Payment") -> "Payment":
        url = self.config.get_endpoint(f"{self.endpoint}/{sale_order_id}/payments")
        res = requests.post(url, data=payload.model_dump_json(exclude_none=True), headers=self.config.headers)
        return Payment(**res.json())

    def update(self, sale_order_id: int, payment_id: int, payload: "Payment") -> "Payment":
        url = self.config.get_endpoint(f"{self.endpoint}/{sale_order_id}/payments/{payment_id}")
        res = requests.put(url, data=payload.model_dump_json(exclude_none=True), headers=self.config.headers)
        return Payment(**res.json())
