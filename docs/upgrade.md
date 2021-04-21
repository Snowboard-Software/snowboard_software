Upgrade Snowboard
===========

💡 Before you upgrade, we recommend you to back up your virtual machine that runs Snowboard.

##### 1. Navigate into the directory that contains the `docker-compose.yml`
```bash
cd snowboard
```

##### 2. Pull the new version of Snowboard
```bash
docker-compose pull
```
##### 3. Renew the running version. 
```bash
docker-compose up -d
```
This command automatically restarts the updated services.