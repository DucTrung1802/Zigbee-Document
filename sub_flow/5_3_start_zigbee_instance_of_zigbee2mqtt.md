# Start Zigbee instance of zigbee2mqtt 

## External flow: [Start Controller of zigbee2mqtt - Step 3](5_start_controller_of_zigbee2mqtt.md#step-3-start-zigbee-instance-of-zigbee2mqtt)

### Description
- This is the flow of `start()` method of Zigbee of `zigbee2mqtt`.
  
#### Class [Zigbee](...)

### Path
> zigbee2mqtt\lib\zigbee.ts

### Flow

<img src="../images/5_3_start_zigbee_instance_of_zigbee2mqtt.png" width="550"/>

### Step 1: Get depencency version of zigbee-herdsman
- Current version: `0.14.27`

### Step 2: Load and apply configuration
All the following data are get from file `zigbee2mqtt\lib\util\settings.ts`
- network
  - panID
  - extendedPanID
  - channelList
  - networkKey
- databasePath
- databaseBackupPath
- backupPath
- serialPort
  - baudRate
  - rtscts
  - path
  - adapter
- adapter
  - concurrent
  - delay
  - disableLED

### Step 3: Declare instance Controller of zigbee-herdsman
- Valid channel (11 - 26)
- Valid network key (array, 16 digits long)
- Valid extended PAN ID (array, 8 digits long)
- Valid PAN ID (0x0001 - 0xFFFE)

Class [Controller (zigbee-herdsman)]()

### Step 4: [Start Controller of zigbee-herdsman](5_3_4_start_controller_of_zigbee-herdsman.md)

Class [Controller (zigbee-herdsman)]()

### Step 5: Add event listener for this.herdsman

### Step 6: Handle passlist and blocklist

### Step 7: Check if we have to set a transmit power



