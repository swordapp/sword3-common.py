from __future__ import annotations

from http import HTTPStatus
from typing import Dict, Tuple, Type

from .lib.seamless import SeamlessException


class SwordExceptionMeta(type):
    def __new__(mcs, name, bases, attrs):
        cls = super().__new__(mcs, name, bases, attrs)
        if hasattr(cls, "status_code") and hasattr(cls, "name"):
            cls._registry[(cls.status_code, cls.name)] = cls
        return cls


class SwordException(Exception, metaclass=SwordExceptionMeta):
    _registry: Dict[Tuple[int, str], Type[SwordException]] = {}

    status_code: int
    name: str
    reason: str

    @classmethod
    def for_status_code_and_name(cls, status_code: int, name: str):
        return cls._registry[(status_code, name)]
