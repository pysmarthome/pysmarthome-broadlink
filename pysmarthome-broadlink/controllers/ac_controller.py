from .broadlink_controller import BroadlinkDeviceController
from pysmarthome import AcsModel, AcController, clone


class BroadlinkAcController(AcController, BroadlinkDeviceController):
    model_class = AcsModel.clone()
    model_class.children_model_classes = clone(BroadlinkDeviceController.model_class.children_model_classes)
    model_class.children_model_classes |= clone(AcsModel.children_model_classes)


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
