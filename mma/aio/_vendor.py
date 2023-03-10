# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.9.4, generator: @autorest/python@6.4.3)
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from abc import ABC
from typing import TYPE_CHECKING

from ._configuration import MMAV3StatsConfiguration

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core import AsyncPipelineClient

    from .._serialization import Deserializer, Serializer


class MMAV3StatsMixinABC(ABC):
    """DO NOT use this class. It is for internal typing use only."""

    _client: "AsyncPipelineClient"
    _config: MMAV3StatsConfiguration
    _serialize: "Serializer"
    _deserialize: "Deserializer"
