"""
Module: 'network' on esp32 1.14.0
"""
# MCU: (sysname='esp32', nodename='esp32', release='1.14.0', version='v1.14 on 2021-02-02', machine='ESP32 module with ESP32')
# Stubber: 1.3.2


import string


AP_IF = 1
AUTH_MAX = 6
AUTH_OPEN = 0
AUTH_WEP = 1
AUTH_WPA2_ENTERPRISE = 5
AUTH_WPA2_PSK = 3
AUTH_WPA_PSK = 2
AUTH_WPA_WPA2_PSK = 4
ETH_CLOCK_GPIO0_IN = 0
ETH_CLOCK_GPIO16_OUT = 2
ETH_CLOCK_GPIO17_OUT = 3


def LAN():
    pass


MODE_11B = 1
MODE_11G = 2
MODE_11N = 4
PHY_IP101 = 2
PHY_LAN8720 = 0
PHY_TLK110 = 1


def PPP():
    pass


STAT_ASSOC_FAIL = 203
STAT_BEACON_TIMEOUT = 200
STAT_CONNECTING = 1001
STAT_GOT_IP = 1010
STAT_HANDSHAKE_TIMEOUT = 204
STAT_IDLE = 1000
STAT_NO_AP_FOUND = 201
STAT_WRONG_PASSWORD = 202
STA_IF = 0


class WLAN:
    def __init__(self, interface_id) -> None:
        """Create a WLAN network interface object. Supported interfaces are network.STA_IF (station aka client, connects to upstream WiFi access points) and network.AP_IF (access point, allows other WiFi clients to connect). Availability of the methods below depends on interface type. For example, only STA interface may WLAN.connect() to an access point.
        """

    def active(self, is_active: bool = None):
        """Activate (“up”) or deactivate (“down”) network interface, if boolean argument is passed. Otherwise, query current state if no argument is provided. Most other methods require active interface.
        """

    def connect(self, ssid=None, password=None, *, bssid=None):
        """Connect to the specified wireless network, using the specified password. If bssid is given then the connection will be restricted to the access-point with that MAC address (the ssid must also be specified in this case).
        """

    def disconnect(self):
        """Disconnect from the currently connected wireless network.
        """

    def scan(self) -> list[tuple[bytes, bytes, int, int, int, int]]:
        """Scan for the available wireless networks.
        """

    def status(self, param=None):
        """Return the current status of the wireless connection.
        """

    def isconnected(self) -> bool:
        """In case of STA mode, returns True if connected to a WiFi access point and has a valid IP address. In AP mode returns True when a station is connected. Returns False otherwise.
        """

    def ifconfig():
        """In case of STA mode, returns True if connected to a WiFi access point and has a valid IP address. In AP mode returns True when a station is connected. Returns False otherwise.
        """

    def config():
        """Get or set general network interface parameters. These methods allow to work with additional parameters beyond standard IP configuration (as dealt with by WLAN.ifconfig()). These include network-specific and hardware-specific parameters. For setting parameters, keyword argument syntax should be used, multiple parameters can be set at once. For querying, parameters name should be quoted as a string, and only one parameter can be queries at time:
        """


def phy_mode(mode=None):
    """Get or set the PHY mode.

        If the mode parameter is provided, sets the mode to its value. If the function is called without parameters, returns the current mode.
    """
