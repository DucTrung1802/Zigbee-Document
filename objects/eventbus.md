# EventBus

## Path
> zigbee2mqtt\lib\eventBus.ts

## Description
- abcd

## Properties
- private callbacksByExtension: `{ [s: string]: { event: string, callback: (...args: unknown[]) => void }[] } = {}`
- private emitter = `new events.EventEmitter()`;

## Methods
- [constructor()]()
- [emitAdapterDisconnected()]()
- [onAdapterDisconnected()]()
- [emitPermitJoinChanged()]()
- [onPermitJoinChanged()]()
- [emitPublishAvailability()]()
- [onPublishAvailability()]()
- [emitEntityRenamed()]()
- [onEntityRenamed()]()
- [emitDeviceRemoved()]()
- [onDeviceRemoved()]()
- [emitLastSeenChanged()]()
- [onLastSeenChanged()]()
- [emitDeviceNetworkAddressChanged()]()
- [onDeviceNetworkAddressChanged()]()
- [emitDeviceAnnounce()]()
- [onDeviceAnnounce()]()
- [emitDeviceInterview()]()
- [onDeviceInterview()]()
- [emitDeviceJoined()]()
- [onDeviceJoined()]()
- [emitEntityOptionsChanged()]()
- [onEntityOptionsChanged()]()
- [emitDeviceLeave()]()
- [onDeviceLeave()]()
- [emitDeviceMessage()]()
- [onDeviceMessage()]()
- [emitMQTTMessage()]()
- [onMQTTMessage()]()
- [emitMQTTMessagePublished()]()
- [onMQTTMessagePublished()]()
- [emitPublishEntityState()]()
- [onPublishEntityState()]()
- [emitGroupMembersChanged()]()
- [onGroupMembersChanged()]()
- [emitDevicesChanged()]()
- [onDevicesChanged()]()
- [emitScenesChanged()]()
- [onScenesChanged()]()
- [emitReconfigure()]()
- [onReconfigure()]()
- [emitStateChange()]()
- [onStateChange()]()
- [on()]()
- [removeListeners()]()

## Methods in detail
---
## constructor()
- Input: `restartCallback: () => void, exitCallback: (code: number) => void`

- Output: `null`

### Flow

[Flow of constructor()](../sub_flow/4_declare_instance_controller_of_zigbee2mqtt.md)

---

## start()
- Input: `null`

- Output: `Promise<void>`

### Flow

[Flow of start()](../sub_flow/5_start_controller_of_zigbee2mqtt.md)

---

## enableDisableExtension()
- Input: `enable: boolean, name: string`

- Output: `Promise<void>`

### Flow

### Step 1: 
- If `enable` is set to `False`:
  - Run `callExtensions('stop', ...)` to stop desired extension.
  - Pop extension from working extensions list.

### Step 2:
- If `enable` is set to `True`:
  - Push extension into working extensions list.
  - Run `callExtensions('start', ...)` to start desired extension.

---

## addExtension()
- Input: `enable: boolean, name: string`

- Output: `Promise<void>`

### Flow

### Step 1:
- Push extension into working extensions list.

### Step 2:
- Run `callExtensions('start', ...)` to start desired extension.

---

## stop()
- Input: `null`

- Output: `Promise<void>`

### Flow

### Step 1:
- Run `callExtensions('stop', ...)` to stop desired extension.

### Step 2:
- Remove all listeners of `Controller`.

### Step 3:
- Stop State: [state.stop()]()

### Step 4:
- Disconnect MQTT: [mqtt.disconnect()]()

### Step 5:
- Stop Zigbee: [zigbee.stop()]()

---

## exit()
- Input: `code: number`

- Output: `Promise<void>`

### Flow

### Step 1:
- Finish logger: [logger.end()]()

### Step 2:
- Run exit callback function: `exitCallback`. See the following function.

Function [exit()]() in
> zigbee2mqtt\index.js

---

## onZigbeeAdapterDisconnected()
- Input: `null`

- Output: `Promise<void>`

### Flow
- Run [Controller.stop()](controller_zigbee2mqtt.md#stop)

---

## publishEntityState()
- Input: `entity: Group | Device, payload: KeyValue, stateChangeReason?: StateChangeReason`

- Output: `Promise<void>`

### Flow

[Flow of publishEntityState()](../sub_flow/5_9_send_all_cached_states.md)

---

## iteratePayloadAttributeOutput()
- Input: `topicRoot: string, payload: KeyValue, options: MQTTOptions`

- Output: `Promise<void>`

### Flow

### Step 1:
- Use regression to analysis sub payload.

### Step 2:
- Publish message: [mqtt.publish()]()

---

## callExtensions()
- Input: `method: 'start' | 'stop', extensions: Extension[]`

- Output: `Promise<void>`

### Flow
- Call method for extensions. Could be:
  - [Extension.start()]()
  - [Extension.stop()]()