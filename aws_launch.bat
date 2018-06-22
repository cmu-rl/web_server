#!/bin/bash
add-apt-repository ppa:deadsnakes/ppa -y
apt-get update
apt-get install python3.6 -y
echo 'alias python=python3.6' >> /home/ubuntu/.bashrc 
source /home/ubuntu/.bashrc

apt-get install python3-pip -y
python3.6 -m pip install --upgrade pip
REM install django here
apt install virtualenv
python3.6 -m pip install django
ssh-keyscan github.com >> /home/ubuntu/.ssh/known_hosts

cd /home/ubuntu
git clone https://github.com/cmu-rl/web_server.git
virtualenv -p /usr/bin/python3.6
chown -R ubuntu:ubuntu ./web_server/

/usr/bin/python3.6 /home/ubuntu/web_server/src/hb/web/manage.py migrate
cd /home/ubuntu/web_server/


echo "[Unit]" >> ./tmp
echo "Description=My Script Service" >> ./tmp
echo "After=multi-user.target" >> ./tmp
echo "" >> ./tmp
echo "[Service]" >> ./tmp
echo "Type=simple" >> ./tmp
echo "StandardOutput=journal" >> ./tmp
echo "StandardError=journal" >> ./tmp
REM echo "ExecStart=source /home/ubuntu/web_server/activate.sh" >> ./tmpls 
echo "ExecStart=/usr/bin/python3.6 /home/ubuntu/web_server/src/hb/web/manage.py runserver  0.0.0.0:80" >> ./tmp    


echo "" >> ./tmp
echo "[Install]" >> ./tmp
echo "WantedBy=multi-user.target" >> ./tmp

chmod 644 ./tmp
mv ./tmp /lib/systemd/system/web_server.service

systemctl daemon-reload
service web_server start
service web_server status
systemctl enable web_server.service

reboot now