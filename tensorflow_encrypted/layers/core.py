from typing import Optional
from abc import ABC, abstractmethod
from ..protocol.protocol import get_protocol, Protocol

from ..protocol.pond import PondPrivateTensor

# TODO
# split backward function in compute_gradient and compute_backpropagated_error?


class Layer(ABC):
    @abstractmethod
    def initialize(self, *args, **kwargs) -> None:
        pass

    @abstractmethod
    def forward(self, x: PondPrivateTensor) -> PondPrivateTensor:
        pass

    @abstractmethod
    def backward(self, *args, **kwargs):
        pass

    @property
    def prot(self) -> Optional[Protocol]:
        return get_protocol()
