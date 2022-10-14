# Start all extensions 

## External flow: [Start Controller of zigbee2mqtt - Step 8](5_start_controller_of_zigbee2mqtt.md#step-8-start-all-extensions)

### Description
- This is the flow of `callExtensions("start", ...)` method of Controller of zigbee2mqtt.
  
#### Class [Extension]()

### Path
> zigbee2mqtt\lib\controller.ts

Start all extensions including:

### Step 1: [Bridge.start()](5_8_1_bridge.start().md)

#### Path
> zigbee2mqtt\lib\extension\bridge.ts

### Step 2: Publish.start()

#### Path
> zigbee2mqtt\lib\extension\publish.ts

- Add event listener `eventBus.onMQTTMessage()`
  - Event: `mqttMessage`
  - Callback function: [Publish.onMQTTMessage()]()

### Step 3: Receive.start()

#### Path
> zigbee2mqtt\lib\extension\receive.ts

- Add event listener `eventBus.onPublishEntityState()`
  - Event: `publishEntityState`
  - Callback function: [Receive.onPublishEntityState()]()
- Add event listener `eventBus.onDeviceMessage()`
  - Event: `onDeviceMessage`
  - Callback function: [Receive.onDeviceMessage()]()

### Step 4: Configure.start()

#### Path
> zigbee2mqtt\lib\extension\configure.ts

#### 4.1 Configure devices
- For each device in database:
  - Run [Configure.configure(..., 'started')]()
  
#### 4.2 Add event listener `eventBus.onDeviceJoined()`
- Event: `deviceJoined`
- Callback function: 
  - If `meta` field device has property `configured`, delete it.
  - Run [Configure.configure(..., 'zigbee_event')]()
  
#### 4.3 Add event listener `eventBus.onDeviceInterview()`
- Event: `deviceInterview`
- Callback function: [Configure.configure(..., 'zigbee_event')]()
  
#### 4.4 Add event listener `eventBus.onLastSeenChanged()`
- Event: `lastSeenChanged`
- Callback function: [Configure.configure(..., 'zigbee_event')]()

#### 4.5 Add event listener `eventBus.onMQTTMessage()`
- Event: `mqttMessage`
- Callback function: [Configure.onMQTTMessage()]()

#### 4.6 Add event listener `eventBus.onReconfigure()`
- Event: `reconfigure`
- Callback function: [Configure.onReconfigure()]()

### Step 5: NetworkMap

#### Path
> zigbee2mqtt\lib\extension\networkMap.ts

#### 5.1 Add event listener `eventBus.onMQTTMessage()`
- Event: `mqttMessage`
- Callback function: [NetworkMap.onMQTTMessage()]()
  
#### 5.2 Define supported format
  - `raw`: [NetworkMap.raw()]()
  - `graphviz`: [NetworkMap.graphviz()]()
  - `plantuml`: [NetworkMap.plantuml()]()

### Step 6: Groups

#### Path
> zigbee2mqtt\lib\extension\groups.ts

#### 6.1 Add event listener `eventBus.onStateChange()`
- Event: `stateChange`
- Callback function: [Groups.onStateChange()]()

#### 6.2 Add event listener `eventBus.onMQTTMessage()`
- Event: `mqttMessage`
- Callback function: [Groups.onMQTTMessage()]()

#### 6.3 Run [Groups.syncGroupsWithSettings()]()

### Step 7: Bind

### Step 8: OnEvent

### Step 9: OTAUpdate

### Step 10: ExternalExtension

### Step 11: Availability

### Step 12: Frontend

### Step 13: HomeAssistant




