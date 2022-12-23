# netcheck service 
it checks raspberry pi is connected to internet or not 


## steps : 
```
sudo cp netcheck.service /etc/systemd/system/
sudo systemctl start netcheck
sudo systemctl enable netcheck
```

## check status of the service
```
sudo systemctl status netcheck
```
