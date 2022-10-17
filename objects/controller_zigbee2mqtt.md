# Controller (zigbee2mqtt)

## Path
> zigbee2mqtt\lib\controller.ts

## Description
- abcd

## Properties
- private eventBus: [EventBus]()
- private zigbee: [Zigbee]();
- private state: [State]();
- private mqtt: [MQTT]();
- private restartCallback: () => void;
- private exitCallback: (code: number) => void;
- private extensions: [Extension]()[ ];
- private extensionArgs: ExtensionArgs;


## Methods
- [constructor()]()
- [start()]()
- [enableDisableExtension()]()
- [addExtension()]()
- [stop()]()
- [exit()]()
- [onZigbeeAdapterDisconnected()]()
- [publishEntityState()]()
- [iteratePayloadAttributeOutput()]()
- [callExtensions()]()

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

---

## enableDisableExtension()
- Input: `enable: boolean, name: string`

- Output: `Promise<void>`

---

## addExtension()
- Input: `enable: boolean, name: string`

- Output: `Promise<void>`

---

## stop()
- Input: `null`

- Output: `Promise<void>`

---

## exit()
- Input: `code: number`

- Output: `Promise<void>`

---

## onZigbeeAdapterDisconnected()
- Input: `null`

- Output: `Promise<void>`

---

## publishEntityState()
- Input: `entity: Group | Device, payload: KeyValue, stateChangeReason?: StateChangeReason`

- Output: `Promise<void>`

---

## iteratePayloadAttributeOutput()
- Input: `topicRoot: string, payload: KeyValue, options: MQTTOptions`

- Output: `Promise<void>`

---

## callExtensions()
- Input: `method: 'start' | 'stop', extensions: Extension[]`

- Output: `Promise<void>`




