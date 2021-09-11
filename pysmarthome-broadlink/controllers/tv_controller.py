from .broadlink_controller import BroadlinkDeviceController
from pysmarthome import TvsModel, TvController, clone


class BroadlinkTvController(TvController, BroadlinkDeviceController):
    model_class = TvsModel.clone()
    model_class.children_model_classes = clone(BroadlinkDeviceController.model_class.children_model_classes)
    model_class.children_model_classes |= clone(TvsModel.children_model_classes)


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
        self.set_int_state_attr_to('volume', n)


    def set_vol_to(self, target):
        self.set_int_state_attr_to('volume', target)
