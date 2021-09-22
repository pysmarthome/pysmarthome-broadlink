from .broadlink_controller import BroadlinkDeviceController
from pysmarthome import Model, TvsModel, TvController, MultiCommandDevicesModel


class BroadlinkTvController(TvController, BroadlinkDeviceController):
    model_class = Model.extends(MultiCommandDevicesModel, TvsModel, name='BroadlinkTvsModel')


    def on(self):
        self.send_command('on')
        return True


    def off(self):
        self.send_command('off')
        return True


    def mute(self):
        self.send_command('mute')
        self.set_state(mute=not self.model.state.mute)


    def set_vol_by(self, n):
        self.set_int_state_attr_by('volume', n)


    def set_vol_to(self, target):
        self.set_int_state_attr_to('volume', target)
