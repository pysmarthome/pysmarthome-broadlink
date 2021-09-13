from pysmarthome import Model, MultiCommandRgbLampController
from .broadlink_controller import BroadlinkDeviceController


class BroadlinkRgbLampController(BroadlinkDeviceController, MultiCommandRgbLampController):
    model_class = Model.extends(
        MultiCommandRgbLampController.model_class,
        name='BroadlinkMultiCommandRgbLampsModel'
    )
