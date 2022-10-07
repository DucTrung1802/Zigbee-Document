# Controller (zigbee2mqtt)

## Description

## Path
> zigbee2mqtt\lib\controller.ts

## Properties
- private eventBus: EventBus
- private zigbee: Zigbee;
- private state: State;
- private mqtt: MQTT;
- private restartCallback: () => void;
- private exitCallback: (code: number) => void;
- private extensions: Extension[];
- private extensionArgs: ExtensionArgs;


## Methods

---

### constructor()
- Input: `restartCallback: () => void, exitCallback: (code: number) => void`

- Output: `null`

### Flow

![abcd]()

#### Step 1: 




---

### start()
```async start(): Promise<void>```

### enableDisableExtension()
```@bind async enableDisableExtension(enable: boolean, name: string): Promise<void>```

### addExtension()
```@bind async addExtension(extension: Extension): Promise<void>```

### stop()
```async stop(): Promise<void>```

### exit()
```async exit(code: number): Promise<void>```

### onZigbeeAdapterDisconnected()
```@bind async onZigbeeAdapterDisconnected(): Promise<void>```

### publishEntityState()
```@bind async publishEntityState(entity: Group | Device, payload: KeyValue, stateChangeReason?: StateChangeReason): Promise<void>```

### iteratePayloadAttributeOutput()
```async iteratePayloadAttributeOutput(topicRoot: string, payload: KeyValue, options: MQTTOptions): Promise<void>```

### sample()
```abc```





#### sample()
```abc```




