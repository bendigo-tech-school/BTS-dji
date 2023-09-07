def start():
    """Checks network name, creates UDP socket and prints starting info to user"""
    import logging
    import sentry_sdk
    import sys
    import time
    import subprocess
    import socket
    import threading


    # Initialize Sentry (error catching)
    # Delete the following 4 lines to opt out
    # More: sentry.io

    # ------------------ #
    sentry_sdk.init(
        dsn="https://f2fcaa10be4f41958ab756183583ba81@o1400261.ingest.sentry.io/6728983",
        traces_sample_rate=1.0,
    )
    # ------------------ #
    global sock, response, tello_address, abort, sent, ip, status_port, video_port, mids
    # Set self variables
    logging = logging

    sock = None
    response = None
    tello_address = None
    abort = False
    response = None
    sent = None
    ip = None
    status_port = 8889
    video_port = 11111

    # Set variables for connection to drone
    host = ""
    port = 9000
    locaddr = (host, port)
    mids = "m1 m2 m3 m4 m5 m6 m7 m8"

    # Print starting info for the user
    print("--------------------------------------")
    print("_________  ____                  ____ ")
    print("    |      |      |      |      |    |")
    print("    |      |___   |      |      |    |")
    print("    |      |      |      |      |    |")
    print("    |      |____  |____  |____  |____|\r\n")
    print("             Drone Script             ")
    print("--------------------------------------")

    print(f"Current port for UDP connection: %s", str(port))

    print("          Checking network...         \r\n")
    time.sleep(0.5)

    # Check what network is connected
    if sys.platform == "win32":
        wifi = subprocess.check_output(
            ["/windows/system32/netsh", "WLAN", "show", "interfaces"])
        data = wifi.decode("utf-8")
        wifi_val = "Not connected"
        for line in data.split("\n"):
            if "SSID: " in line:
                _, val = line.split(": ")
                val = val.strip()
                wifi_val = val
        if "TELLO-" in data or "RMTT-" in data:
            print("Required network detected.")
        else:
            print("Network detected")
            print(
                "It seems like you have not joined the TELLO- or RMTT-network. Please make sure that you have joined the TELLO- or RMTT- Wi-Fi."
            )
    elif sys.platform == "darwin":
        process = subprocess.Popen(
            [
                "/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport",
                "-I",
            ],
            stdout=subprocess.PIPE,
        )
        out, _ = process.communicate()
        process.wait()
        wifi_val = "Not connected"
        for line in out.decode("utf-8").split("\n"):
            if "SSID: " in line:
                _, val = line.split(": ")
                val = val.strip()
                wifi_val = val
        if "TELLO-" not in wifi_val or "RMTT-" not in wifi_val:
            print("Network detected: %s", wifi_val)
            print(
                "It seems like you have joined a different network. Please make sure that you have joined the TELLO-XXXXX Wi-Fi."
            )
        else:
            print("Required network detected: %s", wifi_val)
    else:
        print("Could not determine network.")
        print(
            "Make sure that you are connected to the TELLO-XXXXX or RMTT-XXXXX WiFi networks."
        )

    # Print info to the user
    print("         Making UDP socket...         \r\n")
    time.sleep(1)

    # Create UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    tello_address = ("192.168.10.1", 8889)
    sock.bind(locaddr)
    print("Socket created.")
    print("Socket bound to: %s", str(locaddr))

    recvThread = threading.Thread(target=receive)
    recvThread.start()
    print("Receive thread started.")
    run("command", "Enabling SDK mode\r\n")
    print("--------------------------------------\r\n")


# Function to receive commands from the drone
def receive(self):
    """Receives UDP messages from the drone"""
    while True:
        try:
            response, ip = sock.recvfrom(256)
        except Exception:
            break


def run(command: str, message: str = "No tips available for this command "):
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


def _set_abort(self):
    global abort
    """Sets the abort variable to True"""
    abort = True




# SDK 2.0 Commands
def init():
    """Sends command to initialize SDK mode"""
    print("Sending command: init()")
    return run("command", "Enabling SDK mode\r\n")


def takeoff():
    """Sends command to take off"""
    print("Sending command: takeoff()")
    return run("takeoff", "Taking off, keep clear of drone!\r\n")


def land():
    """Sends command to land"""
    print("Sending command: land()")
    return run("land", "Landing, keep space clear!\r\n")






# End command
def end():
    global sock
    """Closes the socket"""
    print("end(): Closing socket")
    sock.close()
    print("end(): Socket closed")
    return "ok"


start()