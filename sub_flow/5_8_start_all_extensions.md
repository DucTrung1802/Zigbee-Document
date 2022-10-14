# Start all extensions 

## External flow: [Start Controller of zigbee2mqtt - Step 8](5_start_controller_of_zigbee2mqtt.md#step-8-start-all-extensions)

### Description
- This is the flow of `callExtensions("start", ...)` method of Controller of zigbee2mqtt.
  
#### Class [Extension]()

### Path
> zigbee2mqtt\lib\controller.ts

Start all extensions including:

### Step 1: [Bridge.start()](5_8_1_bridge.start().md)

### Step 2: Publish.start()
- Add event listener [eventBus.onMQTTMessage()]()
  - Event: `mqttMessage`
  - Callback function: [Publish.onMQTTMessage()]()

### Step 3: Receive.start()
- Add event listener `eventBus.onPublishEntityState`
  - Event: `publishEntityState`
  - Callback function: [Receive.onPublishEntityState()]()
- Add event listener `eventBus.onDeviceMessage`
  - Event: `onDeviceMessage`
  - Callback function: [Receive.onDeviceMessage()]()

### Step 4: Configure
#### 4.1 Configure devices
- For each device in database:
  - Run [configure(..., 'started')]()
#### 4.2 Add event listener for eventBus
- Event: `deviceJoined`
- Callback function: 
  - If `meta` field device has property `configured`, delete it.
  - Run [configure(..., 'zigbee_event')]()
#### 4.3 Add event 

### Step 5: NetworkMap

### Step 6: Groups

### Step 7: Bind

### Step 8: OnEvent

### Step 9: OTAUpdate

### Step 10: ExternalExtension

### Step 11: Availability

### Step 12: Frontend

### Step 13: HomeAssistant




