from netmiko.cisco_base_connection import CiscoSSHConnection


class MoxaEDSBase(CiscoSSHConnection):
    """ Support Moxa EDS/IKS device series"""
    def sessionn_preparation(self):
        """Prepare the session after the connection has been established"""
        self._test_channel_read(pattern=r"#")
        self.set_base_prompt()
        time.sleep(0.3 * self.global_delay_factor)
        self.clear_buffer()


class MoxaSSH(MoxaEDSBase):
    pass
