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
<br>
- [emitAdapterDisconnected()]()
- [onAdapterDisconnected()]()
<br>
- [emitPermitJoinChanged()]()
- [onPermitJoinChanged()]()
<br>
- [emitPublishAvailability()]()
- [onPublishAvailability()]()
<br>
- [emitEntityRenamed()]()
- [onEntityRenamed()]()
<br>
- [emitDeviceRemoved()]()
- [onDeviceRemoved()]()
<br>
- [emitLastSeenChanged()]()
- [onLastSeenChanged()]()
<br>
- [emitDeviceNetworkAddressChanged()]()
- [onDeviceNetworkAddressChanged()]()
<br>
- [emitDeviceAnnounce()]()
- [onDeviceAnnounce()]()
<br>
- [emitDeviceInterview()]()
- [onDeviceInterview()]()
<br>
- [emitDeviceJoined()]()
- [onDeviceJoined()]()
<br>
- [emitEntityOptionsChanged()]()
- [onEntityOptionsChanged()]()
<br>
- [emitDeviceLeave()]()
- [onDeviceLeave()]()
<br>
- [emitDeviceMessage()]()
- [onDeviceMessage()]()
<br>
- [emitMQTTMessage()]()
- [onMQTTMessage()]()
<br>
- [emitMQTTMessagePublished()]()
- [onMQTTMessagePublished()]()
<br>
- [emitPublishEntityState()]()
- [onPublishEntityState()]()
<br>
- [emitGroupMembersChanged()]()
- [onGroupMembersChanged()]()
<br>
- [emitDevicesChanged()]()
- [onDevicesChanged()]()
<br>
- [emitScenesChanged()]()
- [onScenesChanged()]()
<br>
- [emitReconfigure()]()
- [onReconfigure()]()
<br>
- [emitStateChange()]()
- [onStateChange()]()
<br>
- [on()]()
- [removeListeners()]()

## Methods in detail
---
## constructor()
- Input: `onError: (error: Error) => void`

- Output: `null`

### Flow

### Step 1:
- Set max listeners for emitter: `100`

### Step 2:
- Add event listener `emitter.on()`
  - Event: `error`
  - Callback function: [onError]()

```  
logger.error(...);
logger.debug(...);
```

---

## emitAdapterDisconnected()
- Input: `null`

- Output: `null`

### Flow
- Emit event: `adapterDisconnected`

## onAdapterDisconnected()
- Input: `key: ListenerKey, callback: () => void`

- Output: `null`

### Flow
- Add event listener for event: `adapterDisconnected`

---

## emitPermitJoinChanged()
- Input: `data: eventdata.PermitJoinChanged`

- Output: `null`

### Flow
- Emit event: `permitJoinChanged`

## onPermitJoinChanged()
- Input: `key: ListenerKey, callback: (data: eventdata.PermitJoinChanged) => void`

- Output: `null`

### Flow
- Add event listener for event: `permitJoinChanged`

---

## emitPublishAvailability()
- Input: `null`

- Output: `null`

### Flow
- Emit event: `publishAvailability`

## onPublishAvailability()
- Input: `key: ListenerKey, callback: () => void`

- Output: `null`

### Flow
- Add event listener for event: `publishAvailability`

---

## emitEntityRenamed()
- Input: `data: eventdata.EntityRenamed`

- Output: `null`

### Flow
- Emit event: `deviceRenamed`

## onEntityRenamed()
- Input: `key: ListenerKey, callback: (data: eventdata.EntityRenamed) => void`

- Output: `null`

### Flow
- Add event listener for event: `deviceRenamed`

---

## emitDeviceRemoved()
- Input: `data: eventdata.DeviceRemoved`

- Output: `null`

### Flow
- Emit event: `deviceRemoved`

## onDeviceRemoved()
- Input: `key: ListenerKey, callback: (data: eventdata.DeviceRemoved) => void`

- Output: `null`

### Flow
- Add event listener for event: `deviceRemoved`

---

## emitLastSeenChanged()
- Input: `data: eventdata.LastSeenChanged`

- Output: `null`

### Flow
- Emit event: `lastSeenChanged`

## onLastSeenChanged()
- Input: `key: ListenerKey, callback: (data: eventdata.LastSeenChanged) => `

- Output: `null`

### Flow
- Add event listener for event: `lastSeenChanged`

---

## emitDeviceNetworkAddressChanged()
- Input: `data: eventdata.DeviceNetworkAddressChanged`

- Output: `null`

### Flow
- Emit event: `deviceNetworkAddressChanged`

## onDeviceNetworkAddressChanged()
- Input: `key: ListenerKey, callback: (data: eventdata.DeviceNetworkAddressChanged) => void`

- Output: `null`

### Flow
- Add event listener for event: `deviceNetworkAddressChanged`

---

## emitDeviceAnnounce()
- Input: `data: eventdata.DeviceAnnounce`

- Output: `null`

### Flow
- Emit event: `deviceAnnounce`

## onDeviceAnnounce()
- Input: `key: ListenerKey, callback: (data: eventdata.DeviceAnnounce) => void`

- Output: `null`

### Flow
- Add event listener for event: `deviceAnnounce`

---

## emitDeviceInterview()
- Input: `data: eventdata.DeviceInterview`

- Output: `null`

### Flow
- Emit event: `deviceInterview`

## onDeviceInterview()
- Input: `key: ListenerKey, callback: (data: eventdata.DeviceInterview) => void`

- Output: `null`

### Flow
- Add event listener for event: `deviceInterview`

---

## emitDeviceJoined()
- Input: `data: eventdata.DeviceJoined`

- Output: `null`

### Flow
- Emit event: `deviceJoined`

## onAbcd()
- Input: `key: ListenerKey, callback: (data: eventdata.DeviceJoined) => void`

- Output: `null`

### Flow
- Add event listener for event: `deviceJoined`

---

## emitEntityOptionsChanged()
- Input: `data: eventdata.EntityOptionsChanged`

- Output: `null`

### Flow
- Emit event: `entityOptionsChanged`

## onEntityOptionsChanged()
- Input: `key: ListenerKey, callback: (data: eventdata.EntityOptionsChanged) => void`

- Output: `null`

### Flow
- Add event listener for event: `entityOptionsChanged`

---

## emitDeviceLeave()
- Input: `data: eventdata.DeviceLeave`

- Output: `null`

### Flow
- Emit event: `deviceLeave`

## onDeviceLeave()
- Input: `key: ListenerKey, callback: (data: eventdata.DeviceLeave) => void`

- Output: `null`

### Flow
- Add event listener for event: `deviceLeave`

---

## emitDeviceMessage()
- Input: `data: eventdata.DeviceMessage`

- Output: `null`

### Flow
- Emit event: `deviceMessage`

## onDeviceMessage()
- Input: `key: ListenerKey, callback: (data: eventdata.DeviceMessage) => void`

- Output: `null`

### Flow
- Add event listener for event: `deviceMessage`

---

## emitMQTTMessage()
- Input: `data: eventdata.MQTTMessage`

- Output: `null`

### Flow
- Emit event: `mqttMessage`

## onMQTTMessage()
- Input: `key: ListenerKey, callback: (data: eventdata.MQTTMessage) => void`

- Output: `null`

### Flow
- Add event listener for event: `mqttMessage`

---

## emitMQTTMessagePublished()
- Input: `data: eventdata.MQTTMessagePublished`

- Output: `null`

### Flow
- Emit event: `mqttMessagePublished`

## onMQTTMessagePublished()
- Input: `key: ListenerKey, callback: (data: eventdata.MQTTMessagePublished) => void`

- Output: `null`

### Flow
- Add event listener for event: `mqttMessagePublished`

---

## emitPublishEntityState()
- Input: `ndata: eventdata.PublishEntityStateull`

- Output: `null`

### Flow
- Emit event: `publishEntityState`

## onPublishEntityState()
- Input: `key: ListenerKey, callback: (data: eventdata.PublishEntityState) => void`

- Output: `null`

### Flow
- Add event listener for event: `publishEntityState`

---

## emitGroupMembersChanged()
- Input: `ndata: eventdata.GroupMembersChangedull`

- Output: `null`

### Flow
- Emit event: `publishEntityState`

## onGroupMembersChanged()
- Input: `key: ListenerKey, callback: (data: eventdata.GroupMembersChanged) => void`

- Output: `null`

### Flow
- Add event listener for event: `publishEntityState`

---

## emitDevicesChanged()
- Input: `null`

- Output: `null`

### Flow
- Emit event: `devicesChanged`

## onDevicesChanged()
- Input: `key: ListenerKey, callback: () => void`

- Output: `null`

### Flow
- Add event listener for event: `devicesChanged`

---

## emitScenesChanged()
- Input: `null`

- Output: `null`

### Flow
- Emit event: `scenesChanged`

## onScenesChanged()
- Input: `key: ListenerKey, callback: () => void`

- Output: `null`

### Flow
- Add event listener for event: `scenesChanged`

---

## emitReconfigure()
- Input: `data: eventdata.Reconfigure`

- Output: `null`

### Flow
- Emit event: `reconfigure`

## onReconfigure()
- Input: `key: ListenerKey, callback: (data: eventdata.Reconfigure) => void`

- Output: `null`

### Flow
- Add event listener for event: `reconfigure`

---

## emitStateChange()
- Input: `data: eventdata.StateChange`

- Output: `null`

### Flow
- Emit event: `stateChange`

## onStateChange()
- Input: `key: ListenerKey, callback: (data: eventdata.StateChange) => void`

- Output: `null`

### Flow
- Add event listener for event: `stateChange`

---

## on()
- Input: `event: string, callback: (...args: unknown[]) => void, key: ListenerKey`

- Output: `null`

### Flow


---

## removeListeners()
- Input: `key: ListenerKey`

- Output: `null`

### Flow


---
