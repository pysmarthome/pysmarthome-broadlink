from pysmarthome import Model, MultiCommandDeviceController
from ..managers.manager import BroadlinkManager
from base64 import b64decode as decode


class BroadlinkDeviceController(MultiCommandDeviceController):
    model_class = Model.extends(MultiCommandDeviceController.model_class, name='BroadlinkDevicesModel')
    manager_class = BroadlinkManager


    def send_command(self, id):
        for cmd in self.model.commands:
            if (cmd.label == id) or (cmd.id == id):
                return self.dev.send_data(decode(cmd.data))
