import serial
import platform
import glob

def list_serial_ports():
    system_name = platform.system()
    if system_name == "Windows":
        # Scan for available ports.
        available = []
        for i in range(256):
            try:
                s = serial.Serial(i)
                available.append(i)
                s.close()
            except serial.SerialException:
                pass
        return available
    elif system_name == "Darwin":
        # Mac
        #return glob.glob('/dev/tty*') + glob.glob('/dev/cu*')
        return glob.glob('/dev/cu*')
    else:
        # Assume Linux or something else
        return glob.glob('/dev/ttyS*') + glob.glob('/dev/ttyUSB*')
        #return glob.glob('/dev/ttyUSB*')

print len(list_serial_ports())
print list_serial_ports()[1]