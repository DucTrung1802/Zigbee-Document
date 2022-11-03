new_supported_devices_string = """
SP2610ZB Sinopé Zigbee smart outlet
SR-ZG9001K2-DIM Sunricher Zigbee wall remote control for single color, 1 zone
TS0601_co2_sensor TuYa NDIR co2 sensor
TS0601_smart_human_presense_sensor TuYa Smart Human presence sensor
WNRR15/WNRR20 Legrand Outlet with power consumption monitoring
"""

new_supported_devices_string = new_supported_devices_string[1:]

for line in new_supported_devices_string.splitlines():
    first_word = line.split()[0]
    line = line.replace(first_word, "`{}`".format(first_word))
    line = "- " + line
    print(line)
