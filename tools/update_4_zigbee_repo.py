import os
import sys

# Update 4 zigbee repositories
ZIGBEE_REPO = {
    "zigbee2mqtt": {
        "link": "https://github.com/Koenkk/zigbee2mqtt",
        "version": "1.28.3",
    },
    "zigbee2mqtt-frontend": {
        "link": "https://github.com/nurikk/zigbee2mqtt-frontend",
        "version": "1.28.4",
    },
    "zigbee-herdsman": {
        "link": "https://github.com/Koenkk/zigbee-herdsman",
        "version": "1.28.4",
    },
    "zigbee-herdsman-converters": {
        "link": "https://github.com/Koenkk/zigbee-herdsman-converters",
        "version": "1.28.4",
    },
}

# Parameters
old_general_version = "1.28.2"
new_general_version = "1.28.3"


def main():
    with open(
        os.path.join(
            sys.path[0], "update_script_to_{}.txt".format(new_general_version)
        ),
        "w",
    ) as f:
        for repo in ZIGBEE_REPO:
            f.write("# {}\n".format(repo))

            # Add new branch
            f.write("git checkout updated-{}\n".format(old_general_version))
            f.write("git branch updated-{}\n".format(new_general_version))
            f.write("git push origin -u updated-{}\n".format(new_general_version))
            f.write("git checkout updated-{}\n".format(new_general_version))

            f.write("\n\n\n\n")

        f.close()


main()
