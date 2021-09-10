from .managers import BroadlinkManager
from .controllers import BroadlinkAcController
from .controllers import BroadlinkTvController
from .controllers import BroadlinkDeviceController
from .controllers import BroadlinkRgbLampController

config = {
    'addr': { 'type': 'string', 'required': True }
}

device_controllers = [
    BroadlinkAcController,
    BroadlinkTvController,
    BroadlinkDeviceController,
    BroadlinkRgbLampController,
]


def on_load(**data):
    BroadlinkManager.init_client(**data)
