sudo service web_server stop
cd ~/web_server/
git pull
sudo systemctl daemon-reload
sudo service web_server start
sudo service web_server status
