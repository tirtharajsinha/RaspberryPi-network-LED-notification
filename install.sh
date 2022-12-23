#! /bin/sh.
sudo cp netcheck.service /etc/systemd/system/
sudo systemctl start netcheck
sudo systemctl enable netcheck
