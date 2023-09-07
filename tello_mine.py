import socket
import time

UDP_IP = "192.168.10.1"
UDP_PORT = 8889
MESSAGE = "command"

# print("UDP target IP:", UDP_IP)
# print("UDP target port:", UDP_PORT)
# print("message:", MESSAGE)
#
# sock = socket.socket(socket.AF_INET, # Internet
#              socket.SOCK_DGRAM) # UDP
# sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
#
# MESSAGE = "takeoff"
# sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
#
# MESSAGE = "land"
# sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))

#
# print("UDP target IP:", UDP_IP)
# print("UDP target port:", UDP_PORT)
# print("message:", MESSAGE)
#
#
# sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
# sock.sendto(bytes(MESSAGE, "utf-8"), (UDP_IP, UDP_PORT))
# time.sleep(10)
# MESSAGE = "takeoff"
# sock.sendto(bytes(MESSAGE, "utf-8"), (UDP_IP, UDP_PORT))
# time.sleep(10)
# MESSAGE = "land"
# sock.sendto(bytes(MESSAGE, "utf-8"), (UDP_IP, UDP_PORT))
#
def _set_abort(self):
    global abort
    """Sets the abort variable to True"""
    abort = True

def run(command):
    """Sends command to the drone and prints message to the user"""
    import threading
    abort = False
    timer = threading.Timer(10, _set_abort)
    # Encode the message in the utf-8 encoding
    command = command.encode(encoding="utf-8")
    # Send the encoded message to the Tello
    sent = sock.sendto(command, tello_address)

    response = None
    timer.start()
    while response is None:
        if abort is True:
            break
    timer.cancel()
    if response is None:
        print("Command timed out.")
        return "error"
    if abort is False:
        response = response.decode(encoding="utf-8")
        response = None
        print("Response to previous command: %s", response)
        return response
    return "error"




host = ""
port = 9000
locaddr = (host, port)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(locaddr)

tello_address = ("192.168.10.1", 8889)
run("Command")
run("takeoff")