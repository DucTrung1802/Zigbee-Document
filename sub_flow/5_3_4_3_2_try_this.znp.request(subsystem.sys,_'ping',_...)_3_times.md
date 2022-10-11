# Try this.znp.request(Subsystem.SYS, 'ping', ...) 3 times 

## External flow: [Start Adapter (ZStackAdapter) - Step 2](5_3_4_3_start_adapter_(zstackadapter).md)

### Description
- This is the `request()` method of Znp of zigbee-herdsman with a specific request as argument.
- - Syntax: `znp.request(Subsystem.SYS, 'ping', ...)`
- Request:
  - Type: `SYS`
  - Command: `ping`
  
#### Class [Znp](...)

### Path
> zigbee-herdsman\src\adapter\z-stack\znp\znp.ts

### Reference
- **Name**: `SYS_PING` 
- **Type**: `SREQ`
- **Description**: This command issues PING requests to verify if a device is active and check the capability of the device
- **Document**: [Z-Stack Monitor and Test API_2020](https://drive.google.com/file/d/1y9t4c9erLgI0HNlFCsCABP23IFJd_A_n/view?usp=sharing)
- **Page**: 80/223

### Method
[request()]() of Znp