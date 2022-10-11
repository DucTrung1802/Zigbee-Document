# Start Adapter (ZStackAdapter) 

## External flow: [Start Controller of zigbee-herdsman - Step 3](5_3_4_start_controller_of_zigbee-herdsman.md#step-3-start-adapter-zstackadapter)

### Description
- This is the flow of `start()` method of ZStackAdapter of zigbee-herdsman.
  
#### Class [ZStackAdapter](...)

### Path
> zigbee-herdsman\src\adapter\z-stack\adapter\zStackAdapter.ts

### Flow

<img src="../images/5_3_4_3_start_adapter_(zstackadapter).png" width="550"/>

### Step 1: [Open Znp](5_3_4_3_1_open_znp.md)

### Step 2: [Try this.znp.request(Subsystem.SYS, 'ping', ...) 3 times](5_3_4_3_2_try_this.znp.request(subsystem.sys%2C_'ping'%2C_...)_3_times.md)

### Step 3: this.znp.request(Subsystem.SYS, 'version', ...)

### Step 4: Detect concurrent of adapter

### Step 5: Declare an instance of Queue with (concurrent = 16)

### Step 6: Declare an instance of ZnpAdapterManager

### Step 7: ZnpAdapterManager.start()

### Step 8: Wait a bit for adapter to startup, otherwise led doesn't disable



