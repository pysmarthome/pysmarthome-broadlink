from .managers import BroadlinkManager
from .controllers import BroadlinkTvController
from .controllers import BroadlinkRgbLampController

config = {
    'addr': { 'type': 'string', 'required': True }
}

device_controllers = [
    BroadlinkTvController,
    BroadlinkDeviceController,
    BroadlinkRgbLampController,
]


def on_load(**data):
    BroadlinkManager.init_client(**data)
