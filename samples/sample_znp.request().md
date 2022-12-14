# znp.request(Subsystem.SYS, 'version', ...)

## External flow: [Start Adapter (ZStackAdapter) - Step 3](5_3_4_3_start_adapter_(zstackadapter).md)

### Description
- This is the `request()` method of Znp in zigbee-herdsman with a specific command as argument.

#### Syntax: `znp.request(Subsystem.<TYPE_OF_SUBSYSTEM>, '<COMMAND>', <PAYLOAD>, ...)`

#### Specific syntax: `znp.request(Subsystem.SYS, 'ping', {capabilities: 1})`

#### Class [Znp](...)

### Path
> zigbee-herdsman\src\adapter\z-stack\znp\znp.ts

### Reference
- **Name**: `SYS_VERSION` 
- **Type**: `SREQ`
- **Description**: This command is used to request for the device’s version string.
- **Document**: [Z-Stack Monitor and Test API_2020](https://drive.google.com/file/d/1y9t4c9erLgI0HNlFCsCABP23IFJd_A_n/view?usp=sharing)
- **Page**: 81/223

### Method
[request()]() of Znp