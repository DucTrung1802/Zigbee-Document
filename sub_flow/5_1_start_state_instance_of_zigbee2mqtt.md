# Start State instance of zigbee2mqtt 

## External flow: [Start Controller of zigbee2mqtt - Step 1](5_start_controller_of_zigbee2mqtt.md)

### Description
- This is the flow of `start()` method of Controller of zigbee2mqtt.  
#### Class [State](...)

### Path
> zigbee2mqtt\lib\state.ts
> 
### Flow

<img src="../images/5_1_start_state_instance_of_zigbee2mqtt.js.png" width="550"/>

### Step 1: Load state
- Try to load state from file (default path: `zigbee2mqtt\data\state.json`, decoder: `utf8`)
- Error occurs when file is corrupted or file does not exist.

### Step 2: [Set interval for saving data]
- Save interval: 300s

- Data has the form as following
```
{
    "ieeeAddress": {
        "attribute_1": value_1
        "attribute_2": value_2
        "attribute_3": value_3
        ...
    }

}
```

Example:

```
{
    "0x804b50fffe584534": {
        "battery": 89,
        "voltage": 2900,
        "last_action": "switch_1_single"
    }
}
```

### Step 3: Set event listener for eventBus, listen to event "deviceLeave"
- Event: `deviceLeave`
- Callback function: Delete the state of the leaving device from database in file `zigbee2mqtt\lib\state.ts`
