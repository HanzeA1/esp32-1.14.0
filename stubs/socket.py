"""
Module: 'socket' on esp32 1.14.0
"""
# MCU: (sysname='esp32', nodename='esp32', release='1.14.0', version='v1.14 on 2021-02-02', machine='ESP32 module with ESP32')
# Stubber: 1.3.2
AF_INET = 2
AF_INET6 = 10
IPPROTO_IP = 0
IPPROTO_TCP = 6
IPPROTO_UDP = 17
IP_ADD_MEMBERSHIP = 3
SOCK_DGRAM = 2
SOCK_RAW = 3
SOCK_STREAM = 1
SOL_SOCKET = 4095
SO_REUSEADDR = 4


def getaddrinfo(host, port, family=0, type=0, proto=0, flags=0):
    """Resolve host and port into list of address info entries.
    Translate the host/port argument into a sequence of 5-tuples that contain
    all the necessary arguments for creating a socket connected to that service.
    host is a domain name, a string representation of an IPv4/v6 address or
    None. port is a string service name such as 'http', a numeric port number or
    None. By passing None as the value of host and port, you can pass NULL to
    the underlying C API.
    The family, type and proto arguments can be optionally specified in order to
    narrow the list of addresses returned. Passing zero as a value for each of
    these arguments selects the full range of results.
    """


class socket:
    """A subclass of _socket.socket adding the makefile() method."""

    def __init__(self, family=AF_INET, type=SOCK_STREAM, proto=0, fileno=None):
        # For user code address family and type values are IntEnum members, but
        # for the underlying _socket.socket they're just integers. The
        # constructor of _socket.socket converts the given argument to an
        # integer automatically.
        pass

    def accept(self):
        """accept() -> (socket object, address info)
        Wait for an incoming connection.  Return a new socket
        representing the connection, and the address of the client.
        For IP sockets, the address info is a pair (hostaddr, port).
        """

    def bind(self, address):
        """Bind the socket to address. The socket must not already be bound.
        """

    def close(self):
        """Close the SocketIO object.  This doesn't close the underlying
        socket, except if all references to it have disappeared.
        """

    def connect(self, address):
        """Connect to a remote socket at address.
        """

    def fileno(self):
        """Return the file descriptor of the underlying socket.
        """

    def listen(self, backlog=0):
        """Enable a server to accept connections. If backlog is specified, it must be at least 0 (if it’s lower, it will be set to 0); and specifies the number of unaccepted connections that the system will allow before refusing new connections. If not specified, a default reasonable value is chosen.
        """

    def makefile(self, mode="r", buffering=None, *,
                 encoding=None, errors=None, newline=None):
        """makefile(...) -> an I/O stream connected to the socket
        The arguments are as for io.open() after the filename, except the only
        supported mode values are 'r' (default), 'w' and 'b'.
        """

    def read(self, size=None):
        """Read up to size bytes from the socket. Return a bytes object. If size is not given, it reads all data available from the socket until EOF; as such the method will not return until the socket is closed. This function tries to read as much data as requested (no “short reads”). This may be not possible with non-blocking socket though, and then less data will be returned.
        """

    def readinto(self, b):
        """Read up to len(b) bytes into the writable buffer *b* and return
        the number of bytes read.  If the socket is non-blocking and no bytes
        are available, None is returned.
        If *b* is non-empty, a 0 return value indicates that the connection
        was shutdown at the other end.
        """

    def readline(self):
        """Read a line, ending in a newline character
        """

    def recv(self, bufsize):
        """Receive data from the socket. The return value is a bytes object representing the data received. The maximum amount of data to be received at once is specified by bufsize.
        """

    def recvfrom(self, bufsize):
        """Receive data from the socket. The return value is a pair (bytes, address) where bytes is a bytes object representing the data received and address is the address of the socket sending the data.
        """

    def send(self, bytes: bytes):
        """Send data to the socket. The socket must be connected to a remote socket. Returns number of bytes sent, which may be smaller than the length of data (“short write”).
        """

    def sendall(self, bytes: bytes):
        """Send all data to the socket. The socket must be connected to a remote socket. Unlike send(), this method will try to send all of data, by sending data chunk by chunk consecutively.

        The behavior of this method on non-blocking sockets is undefined. Due to this, on MicroPython, it’s recommended to use write() method instead, which has the same “no short writes” policy for blocking sockets, and will return number of bytes sent on non-blocking sockets.
        """

    def sendto(self, bytes: bytes, address):
        """Send data to the socket. The socket should not be connected to a remote socket, since the destination socket is specified by address.
        """

    def setblocking(self, flag):
        """Set blocking or non-blocking mode of the socket: if flag is false, the socket is set to non-blocking, else to blocking mode.
        """

    def setsockopt(self, level, optname, value):
        """Set the value of the given socket option. The needed symbolic constants are defined in the socket module (SO_* etc.). The value can be an integer or a bytes-like object representing a buffer.
        """

    def settimeout(self, value):
        """Note: Not every port supports this method, see below.

        Set a timeout on blocking socket operations. The value argument can be a nonnegative floating point number expressing seconds, or None. If a non-zero value is given, subsequent socket operations will raise an OSError exception if the timeout period value has elapsed before the operation has completed. If zero is given, the socket is put in non-blocking mode. If None is given, the socket is put in blocking mode.

        Not every MicroPython port supports this method. A more portable and generic solution is to use uselect.poll object. This allows to wait on multiple objects at the same time (and not just on sockets, but on generic stream objects which support polling). Example:
        """

    def write(self, b):
        """Write the given bytes or bytearray object *b* to the socket
        and return the number of bytes written.  This can be less than
        len(b) if not all data could be written.  If the socket is
        non-blocking and no bytes could be written None is returned.
        """
