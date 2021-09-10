from pysmarthome import MultiCommandRgbLampController
from .broadlink_controller import BroadlinkDeviceController


class BroadlinkRgbLampController(BroadlinkDeviceController, MultiCommandRgbLampController):
    model_class = MultiCommandRgbLampController.model_class
