from xmlrpc.client import boolean


class BLE:
    def __init__(self) -> None:
        pass

    def active(self, active=True) -> bool:
        """Optionally changes the active state of the BLE radio, and returns the current state.

        The radio must be made active before using any other methods on this class.
        """

    def config(self):
        pass

    def irq(self, handler) -> None:
        pass

    def gap_advertise(self, interval_us, adv_data=None, *, resp_data=None, connectable=True):
        pass

    def gap_scan(self, duration_ms, interval_us=1280000, window_us=11250, active=False, /):
        pass

    def gap_connect(self, addr_type, addr, scan_duration_ms=2000, /):
        pass

    def gap_disconnect(self, conn_handle, /):
        pass

    def gatts_register_services(self, services_definition, /):
        pass

    def gatts_read(self, value_handle, /):
        pass

    def gatts_write(self, value_handle, data, /):
        pass

    def gatts_notify(self, conn_handle, value_handle, data=None, /):
        pass

    def gatts_indicate(self, conn_handle, value_handle, /):
        pass

    def gatts_set_buffer(self, value_handle, len, append=False, /):
        pass
