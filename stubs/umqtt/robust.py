"""
Module: 'umqtt.robust' on esp32 1.14.0
"""
# MCU: (sysname='esp32', nodename='esp32', release='1.14.0', version='v1.14 on 2021-02-02', machine='ESP32 module with ESP32')
# Stubber: 1.3.2

class MQTTClient:
    """The MQTTClient class provides a robust MQTT client based on the simple version.
    It features the same functions as the simple version, with a few additions
    It is designed to be memory efficient and robust, and can be used for subscriptions and publications.
    https://github.com/micropython/micropython-lib/tree/master/umqtt.robust"""

    def __init__(self, client_id, server, port=0, user=None, password=None, keepalive=0, ssl=False, ssl_params={}):
        """Initialize an instance of MQTTClient

        Args:
            client_id: identifier for MQTTClient
            server: broker to connect to
            port: port to use for connection, defaults to 0
            user: username to use for connnection, defaults to empty
            password: password to use for connection, defaults to empty
            keepalive: time between keepalive messages, disable using 0, defaults to 0
            ssl: whether to connect using SSL or not, defaults to False
            ssl_params: SSL parameters to use with ussl, for more information look at https://docs.micropython.org/en/latest/library/ussl.html
        """
    DEBUG = None
    DELAY = 2
    def _recv_len(self):
        """Returns received length"""
        pass

    def _send_str(self, s: str):
        """Send string to server
        
        Args:
            s: string to send
        """
        pass

    def check_msg(self):
        """Check whether there is a pending message from the sever.
        If true will work like wait_msg(), else will return immediately"""
        pass

    def connect(self, clean_session=True):
        """Connect to a server
        Returns True if this connection uses persisten session stored on a server (this will be always False if clean_session=True argument is used (default))."""
        pass

    def delay(self, i):
        """Delays program
        
        Args:
            i: amount of seconds to delay for
        """
        pass

    def disconnect(self):
        """Disconnect from server"""
        pass

    def log(self, in_reconnect, e):
        """Logs messages, if DEBUG is set to True (defaults to False)"""
        pass

    def ping(self):
        """Pings server
        Message is processed by wait_msg()"""
        pass

    publish = None
    reconnect = None
    def set_callback(self, f: function):
        """Set callback function to process messages

        Args:
            f: function to pass messages to, function is given parameters topic and message
        """
        pass

    def set_last_will(self, topic, msg, retain=False, qos=0):
        """Sets last will message
        
        Args:
            topic: topic to publish in
            msg: message to publish
            retain: whether the broker has to retain the message, defaults to False
            qos: defines quality of service, defaults to 0"""
        pass

    def subscribe(self, topic: str, qos=0):
        """Subscribe to a topic

        Args:
            topic: topic to subscribe to
            qos: defines quality of service, defaults to 0
        """
        pass

    wait_msg = None
simple = None
utime = None
