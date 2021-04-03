"""
Module: 'machine' on esp32 1.14.0
"""
# MCU: (sysname='esp32', nodename='esp32', release='1.14.0', version='v1.14 on 2021-02-02', machine='ESP32 module with ESP32')
# Stubber: 1.3.2


class ADC:
    """The ADC class provides an interface to analog-to-digital convertors, and represents a single endpoint that can sample a continuous voltage and convert it to a discretised value.
    """
    ATTN_0DB = 0
    ATTN_11DB = 3
    ATTN_2_5DB = 1
    ATTN_6DB = 2
    WIDTH_10BIT = 1
    WIDTH_11BIT = 2
    WIDTH_12BIT = 3
    WIDTH_9BIT = 0

    def __init__(self, id) -> None:
        """Access the ADC associated with a source identified by id. This id may be an integer (usually specifying a channel number), a Pin object, or other value supported by the underlying machine.

        Args:
            id (Int | Pin)
        """

    def atten(self, attenuation):
        """This method allows for the setting of the amount of attenuation on the input of the ADC. This allows for a wider possible input voltage range, at the cost of accuracy (the same number of bits now represents a wider range). 
        """

    def width(self, width):
        """This method allows for the setting of the number of bits to be utilised and returned during ADC reads.
        """

    def read_u16():
        """Take an analog reading and return an integer in the range 0-65535. The return value represents the raw reading taken by the ADC, scaled such that the minimum value is 0 and the maximum value is 65535.
        """

    def read() -> float:
        """Read value using the newly configured attenuation and width.
        """
        pass


class DAC:
    ''
    def write():
        pass


DEEPSLEEP = 4
DEEPSLEEP_RESET = 4
EXT0_WAKE = 2
EXT1_WAKE = 3
HARD_RESET = 2


class I2C:
    ''
    def init():
        pass

    def readfrom():
        pass

    def readfrom_into():
        pass

    def readfrom_mem():
        pass

    def readfrom_mem_into():
        pass

    def readinto():
        pass

    def scan():
        pass

    def start():
        pass

    def stop():
        pass

    def write():
        pass

    def writeto():
        pass

    def writeto_mem():
        pass

    def writevto():
        pass


PIN_WAKE = 2


class PWM:
    """PWM can be enabled on all output-enabled pins. The base frequency can range from 1Hz to 40MHz but there is a tradeoff; as the base frequency increases the duty resolution decreases. See LED Control for more details. Currently the duty cycle has to be in the range of 0-1023.
    """

    def __init__(self, id, freq=None, duty=512) -> None:
        pass

    def deinit():
        """This will turn off PWM on the pin
        """

    def duty(duty: int = None) -> int:
        """Set the duty cycle (0-1023)
        """

    def freq(freq: int = None) -> int:
        """Set the frequency
        """

    def init():
        pass


PWRON_RESET = 1


class Pin:
    """Access the pin peripheral (GPIO pin) associated with the given id. If additional arguments are given in the constructor then they are used to initialise the pin. Any settings that are not specified will remain in their previous state.
    """
    IN = 1
    IRQ_FALLING = 2
    IRQ_RISING = 1
    OPEN_DRAIN = 7
    OUT = 3
    PULL_DOWN = 1
    PULL_HOLD = 4
    PULL_UP = 2
    WAKE_HIGH = 5
    WAKE_LOW = 4

    def __init__(self, id: int, mode=- 1, pull=- 1, *, value=None, drive=None, alt=None) -> None:
        """Access the pin peripheral (GPIO pin) associated with the given id. If additional arguments are given in the constructor then they are used to initialise the pin. Any settings that are not specified will remain in their previous state.

        Args:
            id : is mandatory and can be an arbitrary object. Among possible value types are: int (an internal Pin identifier), str (a Pin name), and tuple (pair of [port, pin]).
            value : is valid only for Pin.OUT and Pin.OPEN_DRAIN modes and specifies initial output pin value if given, otherwise the state of the pin peripheral remains unchanged
            drive : specifies the output power of the pin
            alt : specifies an alternate function for the pin and the values it can take are port dependent.
            mode (optional): specifies the pin mode. Defaults to -1.
            pull (optional): specifies if the pin has a (weak) pull resistor attached. Defaults to -1.
        """

    def init(self, mode=- 1, pull=- 1, *, value, drive, alt):
        """Re-initialise the pin using the given parameters. Only those arguments that are specified will be set. The rest of the pin peripheral state will remain unchanged. See the constructor documentation for details of the arguments.
        """

    def irq(self, handler=None, trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING, *, priority=1, wake=None, hard=False):
        """Configure an interrupt handler to be called when the trigger source of the pin is active. If the pin mode is Pin.IN then the trigger source is the external value on the pin. If the pin mode is Pin.OUT then the trigger source is the output buffer of the pin. Otherwise, if the pin mode is Pin.OPEN_DRAIN then the trigger source is the output buffer for state ‘0’ and the external pin value for state ‘1’.

        Args:
            handler (optional): is an optional function to be called when the interrupt triggers. The handler must take exactly one argument which is the Pin instance.. Defaults to None.
            trigger (optional): configures the event which can generate an interrupt. Defaults to Pin.IRQ_FALLING|Pin.IRQ_RISING.
            priority (int, optional): sets the priority level of the interrupt. The values it can take are port-specific, but higher values always represent higher priorities.. Defaults to 1.
            wake (optional): selects the power mode in which this interrupt can wake up the system. Defaults to None.
            hard (bool, optional): if true a hardware interrupt is used. This reduces the delay between the pin change and the handler being called. Hard interrupt handlers may not allocate memory. Defaults to False.
        """

    def off():
        """Set pin to “0” output level.
        """

    def on():
        """Set pin to “1” output level.
        """

    def value(self, x):
        """This method allows to set and get the value of the pin, depending on whether the argument x is supplied or not.

            If the argument is omitted then this method gets the digital logic level of the pin, returning 0 or 1 corresponding to low and high voltage signals respectively. The behaviour of this method depends on the mode of the pin:

            Pin.IN - The method returns the actual input value currently present on the pin.

            Pin.OUT - The behaviour and return value of the method is undefined.

            Pin.OPEN_DRAIN - If the pin is in state ‘0’ then the behaviour and return value of the method is undefined. Otherwise, if the pin is in state ‘1’, the method returns the actual input value currently present on the pin.
        """


class RTC:
    ''
    def datetime():
        pass

    def init():
        pass

    def memory():
        pass


class SDCard:
    ''
    def deinit():
        pass

    def info():
        pass

    def ioctl():
        pass

    def readblocks():
        pass

    def writeblocks():
        pass


SLEEP = 2
SOFT_RESET = 5


class SPI:
    ''
    LSB = 1
    MSB = 0

    def deinit():
        pass

    def init():
        pass

    def read():
        pass

    def readinto():
        pass

    def write():
        pass

    def write_readinto():
        pass


class Signal:
    ''
    def off():
        pass

    def on():
        pass

    def value():
        pass


class SoftI2C:
    ''
    def init():
        pass

    def readfrom():
        pass

    def readfrom_into():
        pass

    def readfrom_mem():
        pass

    def readfrom_mem_into():
        pass

    def readinto():
        pass

    def scan():
        pass

    def start():
        pass

    def stop():
        pass

    def write():
        pass

    def writeto():
        pass

    def writeto_mem():
        pass

    def writevto():
        pass


class SoftSPI:
    ''
    LSB = 1
    MSB = 0

    def deinit():
        pass

    def init():
        pass

    def read():
        pass

    def readinto():
        pass

    def write():
        pass

    def write_readinto():
        pass


TIMER_WAKE = 4
TOUCHPAD_WAKE = 5


class Timer:
    ''
    ONE_SHOT = 0
    PERIODIC = 1

    def deinit():
        pass

    def init():
        pass

    def value():
        pass


class TouchPad:
    ''
    def config():
        pass

    def read():
        pass


class UART:
    ''
    INV_CTS = 1048576
    INV_RTS = 8388608
    INV_RX = 524288
    INV_TX = 4194304

    def any():
        pass

    def deinit():
        pass

    def init():
        pass

    def read():
        pass

    def readinto():
        pass

    def readline():
        pass

    def sendbreak():
        pass

    def write():
        pass


ULP_WAKE = 6


class WDT:
    ''
    def feed():
        pass


WDT_RESET = 3


def deepsleep():
    """Stops execution in an attempt to enter a low power state.

        If time_ms is specified then this will be the maximum time in milliseconds that the sleep will last for. Otherwise the sleep can last indefinitely.

        With or without a timeout, execution may resume at any time if there are events that require processing. Such events, or wake sources, should be configured before sleeping, like Pin change or RTC timeout.

        The precise behaviour and power-saving capabilities of lightsleep and deepsleep is highly dependent on the underlying hardware, but the general properties are:

        A lightsleep has full RAM and state retention. Upon wake execution is resumed from the point where the sleep was requested, with all subsystems operational.

        A deepsleep may not retain RAM or any other state of the system (for example peripherals or network interfaces). Upon wake execution is resumed from the main script, similar to a hard or power-on reset. The reset_cause() function will return machine.DEEPSLEEP and this can be used to distinguish a deepsleep wake from other resets.
    """


def disable_irq():
    """Disable interrupt requests. Returns the previous IRQ state which should be considered an opaque value. This return value should be passed to the enable_irq() function to restore interrupts to their original state, before disable_irq() was called.
    """


def enable_irq():
    """Re-enable interrupt requests. The state parameter should be the value that was returned from the most recent call to the disable_irq() function.
    """


def freq():
    """Returns CPU frequency in hertz.
    """


def idle():
    """Gates the clock to the CPU, useful to reduce power consumption at any time during short or long periods. Peripherals continue working and execution resumes as soon as any interrupt is triggered (on many ports this includes system timer interrupt occurring at regular intervals on the order of millisecond).
    """


def lightsleep():
    """Stops execution in an attempt to enter a low power state.

        If time_ms is specified then this will be the maximum time in milliseconds that the sleep will last for. Otherwise the sleep can last indefinitely.

        With or without a timeout, execution may resume at any time if there are events that require processing. Such events, or wake sources, should be configured before sleeping, like Pin change or RTC timeout.

        The precise behaviour and power-saving capabilities of lightsleep and deepsleep is highly dependent on the underlying hardware, but the general properties are:

        A lightsleep has full RAM and state retention. Upon wake execution is resumed from the point where the sleep was requested, with all subsystems operational.

        A deepsleep may not retain RAM or any other state of the system (for example peripherals or network interfaces). Upon wake execution is resumed from the main script, similar to a hard or power-on reset. The reset_cause() function will return machine.DEEPSLEEP and this can be used to distinguish a deepsleep wake from other resets.
    """


mem16 = None
mem32 = None
mem8 = None


def reset():
    """Resets the device in a manner similar to pushing the external RESET button.
    """


def reset_cause():
    """Get the reset cause.
    """


def sleep():
    """This function is deprecated, use lightsleep() instead with no arguments.
    """


def soft_reset():
    """Performs a soft reset of the interpreter, deleting all Python objects and resetting the Python heap.It tries to retain the method by which the user is connected to the MicroPython REPL (eg serial, USB, Wifi).
    """


def time_pulse_us():
    """Time a pulse on the given pin, and return the duration of the pulse in microseconds. The pulse_level argument should be 0 to time a low pulse or 1 to time a high pulse.

        If the current input value of the pin is different to pulse_level, the function first (*) waits until the pin input becomes equal to pulse_level, then (**) times the duration that the pin is equal to pulse_level. If the pin is already equal to pulse_level then timing starts straight away.

        The function will return -2 if there was timeout waiting for condition marked (*) above, and -1 if there was timeout during the main measurement, marked (**) above. The timeout is the same for both cases and given by timeout_us (which is in microseconds).
    """


def unique_id() -> bytes:
    """Returns a byte string with a unique identifier of a board/SoC. It will vary from a board/SoC instance to another, if underlying hardware allows. Length varies by hardware (so use substring of a full value if you expect a short ID). In some MicroPython ports, ID corresponds to the network MAC address.
    """


def wake_reason():
    """Get the wake reason.
    """
