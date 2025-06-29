from abc import ABC
from ..config.config import ConfigProducteca


class BaseService(ABC):
    endpoint: str
    config: ConfigProducteca
