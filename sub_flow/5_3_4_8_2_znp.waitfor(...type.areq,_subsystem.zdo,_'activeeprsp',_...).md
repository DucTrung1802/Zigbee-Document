# znp.waitFor(...Type.AREQ, Subsystem.ZDO, 'activeEpRsp', ...)

## External flow: [Add coordinator to the database if it is not there yet - Step 2](5_3_4_8_add_coordinator_to_the_database_if_it_is_not_there_yet.md#step-2-znpwaitfortypeareq-subsystemzdo-activeeprsp)

### Description
- This is the `waitFor()` method of Znp in zigbee-herdsman with a specific command as argument.

#### Syntax: `znp.waitFor(<COMMAND_TYPE>, Subsystem.<TYPE_OF_SUBSYSTEM>, '<COMMAND>', ...)`

#### Specific syntax: `znp.waitFor(...Type.AREQ, Subsystem.ZDO, 'activeEpRsp', ...)`

#### Class [Znp](...)

### Path
> zigbee-herdsman\src\adapter\z-stack\znp\znp.ts

### Reference
- **Name**: `ZDO_ACTIVE_EP_RSP` 
- **Type**: `AREQ`
- **Description**: This callback message is in response to the ZDO Active Endpoint Request.
- **Document**: [Z-Stack Monitor and Test API_2020](https://drive.google.com/file/d/1y9t4c9erLgI0HNlFCsCABP23IFJd_A_n/view?usp=sharing)
- **Page**: 185/223

### Method
[waitFor()]() of Znp