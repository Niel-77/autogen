from __future__ import annotations

from typing import Optional, runtime_checkable

from typing_extensions import Any, AsyncGenerator, Dict, List, Protocol, Required, TypedDict, Union

from ..cache import AbstractCache
from .types import ChatMessage, CreateResponse, RequestUsage


class ModelCapabilities(TypedDict, total=False):
    vision: Required[bool]
    function_calling: Required[bool]


@runtime_checkable
class ModelClient(Protocol):
    # Caching has to be handled internally as they can depend on the create args that were stored in the constructor
    async def create(
        self, messages: List[ChatMessage], cache: Optional[AbstractCache] = None, extra_create_args: Dict[str, Any] = {}
    ) -> CreateResponse: ...

    def create_stream(
        self, messages: List[ChatMessage], cache: Optional[AbstractCache] = None, extra_create_args: Dict[str, Any] = {}
    ) -> AsyncGenerator[Union[str, CreateResponse], None]: ...

    def actual_usage(self) -> RequestUsage: ...

    def total_usage(self) -> RequestUsage: ...

    @property
    def capabilities(self) -> ModelCapabilities: ...