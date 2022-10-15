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
  - 
  - If device has `configure()` method, run [Configure.configure(..., 'started')]()
  
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

### Step 5: NetworkMap.start()

#### Path
> zigbee2mqtt\lib\extension\networkMap.ts

#### 5.1 Add event listener `eventBus.onMQTTMessage()`
- Event: `mqttMessage`
- Callback function: [NetworkMap.onMQTTMessage()]()
  
#### 5.2 Define supported format
  - `raw`: [NetworkMap.raw()]()
  - `graphviz`: [NetworkMap.graphviz()]()
  - `plantuml`: [NetworkMap.plantuml()]()

### Step 6: Groups.start()

#### Path
> zigbee2mqtt\lib\extension\groups.ts

#### 6.1 Add event listener `eventBus.onStateChange()`
- Event: `stateChange`
- Callback function: [Groups.onStateChange()]()

#### 6.2 Add event listener `eventBus.onMQTTMessage()`
- Event: `mqttMessage`
- Callback function: [Groups.onMQTTMessage()]()

#### 6.3 Run [Groups.syncGroupsWithSettings()]()

### Step 7: Bind.start()

#### 7.1 Add event listener `eventBus.onDeviceMessage()`
- Event: `deviceMessage`
- Callback function: [Bind.poll()]()

#### 7.2 Add event listener `eventBus.onMQTTMessage()`
- Event: `mqttMessage`
- Callback function: [Bind.onMQTTMessage()]()

#### 7.3 Add event listener `eventBus.onGroupMembersChanged()`
- Event: `groupMembersChanged`
- Callback function: [Bind.onGroupMembersChanged()]()

### Step 8: OnEvent.start()

#### Path
> zigbee2mqtt\lib\extension\onEvent.ts

#### Description
- This extension calls the zigbee-herdsman-converters onEvent.

#### 8.1 Call `onEvent` of each devices
- For each device in database:
  - If device has `onEvent()` method, run [OnEvent.callOnEvent(device, 'start', {})]()

#### 8.2 Add event listener `eventBus.onDeviceMessage()`
- Event: `deviceMessage`
- Callback function: [OnEvent.callOnEvent(..., "message", ...)]()

#### 8.3 Add event listener `eventBus.onDeviceJoined()`
- Event: `deviceJoined`
- Callback function: [OnEvent.callOnEvent(..., "deviceJoined", ...)]()

#### 8.4 Add event listener `eventBus.onDeviceInterview()`
- Event: `deviceInterview`
- Callback function: [OnEvent.callOnEvent(..., "deviceInterview", ...)]()

#### 8.5 Add event listener `eventBus.onDeviceAnnounce()`
- Event: `deviceAnnounce`
- Callback function: [OnEvent.callOnEvent(..., "deviceAnnounce", ...)]()

#### 8.6 Add event listener `eventBus.onDeviceNetworkAddressChanged()`
- Event: `deviceNetworkAddressChanged`
- Callback function: [OnEvent.callOnEvent(..., "deviceNetworkAddressChanged", ...)]()

#### 8.7 Add event listener `eventBus.onEntityOptionsChanged()`
- Event: `deviceOptionsChanged`
- Callback function: 
  - [OnEvent.callOnEvent(..., "deviceOptionsChanged", ...)]()
  - If `OnEvent.callOnEvent(..., "deviceOptionsChanged", ...)` runs successfully, eventBus emits event `devicesChanged` through `eventBus.emitDevicesChanged()`.

### Step 9: OTAUpdate.start()

#### Path
> zigbee2mqtt\lib\extension\otaUpdate.ts

#### 9.1 Add event listener `eventBus.onMQTTMessage()`
- Event: `mqttMessage`
- Callback function: [OTAUpdate.onMQTTMessage()]()

#### 9.2 Add event listener `eventBus.onDeviceMessage()`
- Event: `deviceMessage`
- Callback function: [OTAUpdate.onZigbeeEvent()]()

#### 9.3 Check if `Ikea` device using test URL

#### 9.4 Let zigbeeOTA module know if the override index file is provided

#### 9.5 In order to support local firmware files we need to let zigbeeOTA know where the data directory is

#### 9.6 In case Zigbee2MQTT is restared during an update, remove progress and remaining values from state.

### Step 10: ExternalExtension.start()

#### Path
> zigbee2mqtt\lib\extension\externalExtension.ts

#### 10.1 Add event listener `eventBus.onMQTTMessage()`
- Event: `mqttMessage`
- Callback function: [ExternalExtension.onMQTTMessage()]()

#### 10.2 Define requests
- `save`: [ExternalExtension.saveExtension()]()
- `remove`: [ExternalExtension.removeExtension()]()

#### 10.3 Load `user-defined` extensions

Method [ExternalExtension.loadUserDefinedExtensions()]()

#### 10.4 Publish `user-defined` extensions

Method [ExternalExtension.publishExtensions()]()

### Step 11: Availability.start()

#### Path
> zigbee2mqtt\lib\extension\availability.ts

#### 11.1 Add event listener `eventBus.onEntityRenamed()`
- Event: `deviceRenamed`
- Callback function: 
  - If availability is enabled for entity:
    - ``mqtt.publish(`${data.from}/availability`, ...)``
    - Run [Availability.publishAvailability()]()

#### 11.2 Add event listener `eventBus.onDeviceRemoved()`
- Event: `deviceRemoved`
- Callback function: Clear timeout of device - [clearTimeout(this.timers[data.ieeeAddr])]()

#### 11.3 Add event listener `eventBus.onDeviceLeave()`
- Event: `deviceLeave`
- Callback function: Clear timeout of device - [clearTimeout(this.timers[data.ieeeAddr])]()

#### 11.4 Add event listener `eventBus.onDeviceAnnounce()`
- Event: `deviceLeave`
- Callback function: Retrieve state of device - [Availability.retrieveState(data.device)]()

#### 11.5 Add event listener `eventBus.onLastSeenChanged()`
- Event: `lastSeenChanged`
- Callback function: Retrieve state of device - [Availability.onLastSeenChanged]()

#### 11.6 Add event listener `eventBus.onPublishAvailability()`
- Event: `publishAvailability`
- Callback function: Publish availability for all entities - [Availability.publishAvailabilityForAllEntities]()

#### 11.7 Add event listener `eventBus.onGroupMembersChanged()`
- Event: `publishAvailability`
- Callback function: Publish availability for all entities - [Availability.publishAvailability(data.group, ...)]()

#### 11.8 Publish availability for all entities 
- [Availability.publishAvailabilityForAllEntities]()

### Step 12: Frontend.start()

#### Path
> zigbee2mqtt\lib\extension\frontend.ts

#### 12.1 Create http server 
- Run [http.createServer()]()

#### 12.2 Add event listener `server.on()`
- Event: `upgrade`
- Callback function: [Frontend.onUpgrade]()

#### 12.3 Initialize `fileServer`
- Assign `fileServer = ` [gzipStatic(...)]()

#### 12.4 Initialize `WebSocket`

Class [WebSocket]() 

#### 12.5 Add event listener `wss.on()`
- Event: `connection`
- Callback function: [Frontend.onWebSocketConnection()]()

#### 12.6 Start a server listening for connections

### Step 13: HomeAssistant.start()

#### Path
> zigbee2mqtt\lib\extension\homeassistant.ts

#### Step 13.1 Get zigbee2mqtt version
- Current version: `16.17.0`

#### Step 13.2 Add event listener `eventBus.onDeviceRemoved()`
- Event: `deviceRemoved`
- Callback function: [HomeAssistant.onDeviceRemoved()]()

#### Step 13.3 Add event listener `eventBus.onMQTTMessage()`
- Event: `mqttMessage`
- Callback function: [HomeAssistant.onMQTTMessage()]()

#### Step 13.4 Add event listener `eventBus.onEntityRenamed()`
- Event: `deviceRenamed`
- Callback function: [HomeAssistant.onEntityRenamed()]()

#### Step 13.5 Add event listener `eventBus.onPublishEntityState()`
- Event: `publishEntityState`
- Callback function: [HomeAssistant.onPublishEntityState()]()

#### Step 13.6 Add event listener `eventBus.onGroupMembersChanged()`
- Event: `groupMembersChanged`
- Callback function: [HomeAssistant.onGroupMembersChanged()]()

#### Step 13.7 Add event listener `eventBus.onDeviceAnnounce()`
- Event: `deviceAnnounce`
- Callback function: [HomeAssistant.onZigbeeEvent()]()

#### Step 13.8 Add event listener `eventBus.onDeviceJoined()`
- Event: `deviceJoined`
- Callback function: [HomeAssistant.onZigbeeEvent()]()

#### Step 13.9 Add event listener `eventBus.onDeviceInterview()`
- Event: `deviceInterview`
- Callback function: [HomeAssistant.onZigbeeEvent()]()

#### Step 13.10 Add event listener `eventBus.abcd()`
- Event: `abcd`
- Callback function: [HomeAssistant.abcd()]()

#### Step 13.11 Add event listener `eventBus.abcd()`
- Event: `abcd`
- Callback function: [HomeAssistant.abcd()]()

#### Step 13.12 Add event listener `eventBus.abcd()`
- Event: `abcd`
- Callback function: [HomeAssistant.abcd()]()
