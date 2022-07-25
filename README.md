# Tests of IBM Cloud context-based-restrictions security feature
This repository holds files for testing context-based restrictions in IBM Cloud.


The overall scenario is shown here. A Python script is deployed as job to IBM Cloud Code Engine. A jobrun, running the script, succeeds - all items in the bucket **cbrbucket** can be retrieved. With the deployed restrictions in place, running the same script from other environments fails with the access denied (see screenshots below).
![scenario overview](images/CBR_tests.png)


Access from Code Engine succeeds:
![access from Code Engine succeeds](images/CBR_CE_success.png)

Access from another compute environment fails. Access is denied:
![access from other environment is denied](images/CBR_denied.png)


### License
See the [LICENSE](LICENSE) file.