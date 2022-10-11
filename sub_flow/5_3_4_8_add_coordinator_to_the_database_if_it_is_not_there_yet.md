# Add coordinator to the database if it is not there yet 

## External flow: [Start Controller of zigbee-herdsman - Step 8](5_3_4_start_controller_of_zigbee-herdsman.md#step-8-add-coordinator-to-the-database-if-it-is-not-there-yet)

### Description
- This is the `execute<T>()` method of Queue of zigbee-herdsman with a function (job) as argument.
- Syntax: `znp.request(Subsystem.SYS, 'ping', ...)`
- Request:
  - Type: `SYS`
  - Command: `ping`
  
#### Class [Znp](...)

### Path
> zigbee-herdsman\src\adapter\z-stack\znp\znp.ts

### Reference
- **Name**: `SYS_PING` 
- **Type**: `SREQ`
- **Description**: This command issues PING requests to verify if a device is active and check the capability of the device.
- **Document**: [Z-Stack Monitor and Test API_2020](https://drive.google.com/file/d/1y9t4c9erLgI0HNlFCsCABP23IFJd_A_n/view?usp=sharing)
- **Page**: 80/223

### Method
[request()]() of Znp