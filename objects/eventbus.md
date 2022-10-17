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

## abcd()
- Input: `null`

- Output: `null`

### Flow

### Step 1:

### Step 2:

### Step 3:

### Step 4:

---