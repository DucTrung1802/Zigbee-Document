# Zigbee Document

### Legend
<img src="images/legend.png" width="550"/>

## Initialization

### Path
> zigbee2mqtt\index.js

### Flow
<img src="images/README.png" width="550"/>

### Step 1: await checkDist()
- Build zigbee2mqtt if it has not been built yet.
- Build zigbee2mqtt if it has changes.

### Step 2: Check if the Node.js version satisfies the Zigbee2MQTT requirements
- Zigbee2MQTT requires node version ^14 | ^16 | ^18 | ^19.

### Step 3: Validate settings in file `zigbee2mqtt\dist\util\settings.js`

### Step 4: [Declare instance Controller of zigbee2mqtt](sub_flow/4_declare_instance_controller_of_zigbee2mqtt.md)

### Step 5: [Start Controller of zigbee2mqtt](sub_flow/5_start_controller_of_zigbee2mqtt.md)

## Event loop