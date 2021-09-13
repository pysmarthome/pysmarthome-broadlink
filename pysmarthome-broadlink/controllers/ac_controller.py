from .broadlink_controller import BroadlinkDeviceController
from pysmarthome import Model, AcsModel, AcController, MultiCommandDevicesModel


class BroadlinkAcController(AcController, BroadlinkDeviceController):
    model_class = Model.extends(MultiCommandDevicesModel, AcsModel, name='BroadlinkAcsModel')


    def on(self):
        self.send_command('on')
        return True


    def off(self):
        self.send_command('off')
        return True


    def set_temp_by(self, n):
        self.set_int_state_attr_by('temp', n)


    def set_temp_to(self, target):
        self.set_int_state_attr_to('temp', target)
