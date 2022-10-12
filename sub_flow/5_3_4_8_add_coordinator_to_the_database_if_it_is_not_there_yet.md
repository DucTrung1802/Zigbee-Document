# Add coordinator to the database if it is not there yet 

## External flow: [Start Controller of zigbee-herdsman - Step 8](5_3_4_start_controller_of_zigbee-herdsman.md#step-8-add-coordinator-to-the-database-if-it-is-not-there-yet)

### Description
- This is the `getCoordinator()` method of ZStackAdapter of zigbee-herdsman.
- It is a job (`<FUNCTION>`) added in `queue.execute()`.

#### Syntax: `queue.execute<T>(async <FUNCTION>)`

#### Class [ZStackAdapter](...)

#### Method [queue.execute()](...)

### Path
> zigbee-herdsman\src\adapter\z-stack\adapter\zStackAdapter.ts

### Job (`<FUNCTION>`)

#### Flow

<img src="..." width="550"/>

#### Steps