# netcheck service 
it checks raspberry pi is connected to internet or not 


# install
```
sudo apt install python3-pip
pip install RPi.GPIO
pip install requests
bash install.sh
```

## manual install : 
```
sudo cp netcheck.service /etc/systemd/system/
sudo systemctl start netcheck
sudo systemctl enable netcheck
```

## check status of the service
```
sudo systemctl status netcheck
```

## default pin numbers
(+) pin : GPIO 21/pin 40
GND pin : GPIO GND/pin 39

## check pinout
```
pinout
```
## check pinstate
```
raspi-gpio get
```


## Alter GPIO pin state
### power up
```
raspi-gpio set <PIN_number> op pn dh
```
### power down
```
raspi-gpio set <PIN_NUMBER> op pn dl
```




