from abc import ABC
from ..config.config import ConfigProducteca
from dataclasses import dataclass


@dataclass
class BaseService(ABC):
    config: ConfigProducteca
    endpoint: str
