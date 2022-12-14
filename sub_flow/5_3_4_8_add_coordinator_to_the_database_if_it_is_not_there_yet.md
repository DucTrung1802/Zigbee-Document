# Add coordinator to the database if it is not there yet 

## External flow: [Start Controller of zigbee-herdsman - Step 8](5_3_4_start_controller_of_zigbee-herdsman.md#step-8-add-coordinator-to-the-database-if-it-is-not-there-yet)

### Description
- This is the `getCoordinator()` method of ZStackAdapter of zigbee-herdsman.
- It is a job (`<FUNCTION>`) added in `queue.execute()`.

#### Syntax: `queue.execute<T>(async <FUNCTION>)`

#### Class [ZStackAdapter](...)

### Path
> zigbee-herdsman\src\adapter\z-stack\adapter\zStackAdapter.ts

## Job (`<FUNCTION>`)

### Flow

<img src="../images/5_3_4_8_add_coordinator_to_the_database_if_it_is_not_there_yet.png" width="550"/>

### Step 1: checkInterpanLock()
- If `interpanLock` value is `True`, an Error will be thrown: `Cannot execute command, in Inter-PAN mode`
- [Inter-PAN mode](https://www.google.com.vn/)

### Step 2: [znp.waitFor(...Type.AREQ, Subsystem.ZDO, 'activeEpRsp', ...)](5_3_4_8_2_znp.waitfor(...type.areq%2C_subsystem.zdo%2C_'activeeprsp'%2C_...).md)

### Step 3: [znp.request(Subsystem.ZDO, 'activeEpReq', ...)](5_3_4_8_3_znp.request(subsystem.zdo%2C_'activeepreq'%2C_...).md)

### Step 4: activeEpRsp.start().promise
- Get ID of the `activeEpRsp` waiter
- Set timeout for the `activeEpRsp` waiter: [timeouts.default](znp) = 10 seconds 
- Start timer

Class [Waitress]()
Method [waitFor]()

### Step 5: [znp.request(Subsystem.UTIL, 'getDeviceInfo', ...)](5_3_4_8_5_znp.request(Subsystem.UTIL%2C%20'getDeviceInfo'%2C%20...).md)

### Step 6: For each active endpoint of Coordinator

#### 6.1 [znp.waitFor(...Type.AREQ, Subsystem.ZDO, 'simpleDescRsp', ...)](5_3_4_8_6_1_znp.waitfor(...type.areq%2C_subsystem.zdo%2C_'simpledescrsp'%2C_...).md)

#### 6.2 [znp.request(Subsystem.ZDO, 'simpleDescReq', ...)](5_3_4_8_6_2_znp.request(subsystem.zdo,_'simpledescreq',_...).md)

#### 6.3 simpleDescRsp.start().promise
- Get ID of the `simpleDescRsp` waiter
- Set timeout for the `simpleDescRsp` waiter: [timeouts.default](znp) = 10 seconds 
- Start timer

Class [Waitress]()
Method [waitFor]()

#### 6.4 Push endpoint information of Coordinator
- ID: 1
  - deviceID: 5
  - profileID: 260
  - inputClusters: [ ]
  - outputCluster: [ ]

- ID: 2
  - deviceID: 5
  - profileID: 257
  - inputClusters: [ ]
  - outputCluster: [ ]

- ID: 3
  - deviceID: 5
  - profileID: 260
  - inputClusters: [ ]
  - outputCluster: [ ]

- ID: 4
  - deviceID: 5
  - profileID: 263
  - inputClusters: [ ]
  - outputCluster: [ ]

- ID: 5
  - deviceID: 5
  - profileID: 264
  - inputClusters: [ ]
  - outputCluster: [ ]

- ID: 6
  - deviceID: 5
  - profileID: 265
  - inputClusters: [ ]
  - outputCluster: [ ]

- ID: 8
  - deviceID: 5
  - profileID: 260
  - inputClusters: [ ]
  - outputCluster: [ ]

- ID: 10
  - deviceID: 5
  - profileID: 260
  - inputClusters: [ ]
  - outputCluster: [ ]

- ID: 11
  - deviceID: 1024
  - profileID: 260
  - inputClusters: [ 1281, 10 ]
  - outputCluster: [ 1280, 1282 ]

- ID: 12
  - deviceID: 5
  - profileID: 49246
  - inputClusters: [ ]
  - outputCluster: [ ]

- ID: 13
  - deviceID: 5
  - profileID: 260
  - inputClusters: [ 25 ]
  - outputCluster: [ ]

- ID: 47
  - deviceID: 5
  - profileID: 260
  - inputClusters: [ ]
  - outputCluster: [ ]

- ID: 110
  - deviceID: 5
  - profileID: 260
  - inputClusters: [ ]
  - outputCluster: [ ]

- ID: 242
  - deviceID: 5
  - profileID: 41440
  - inputClusters: [ ]
  - outputCluster: [ ]

### If there is `No coordinator in database`:
- Run [Device.create("Coordinator",...)]()

### Method [queue.execute()](...)

## External flow: [Start Controller of zigbee-herdsman - Step 8](5_3_4_start_controller_of_zigbee-herdsman.md#step-8-add-coordinator-to-the-database-if-it-is-not-there-yet)
