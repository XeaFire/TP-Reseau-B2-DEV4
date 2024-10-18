#!/bin/bash
sudo mkdir -p /var/log/bs_server
sudo touch /var/log/bs_server/bs_server.log
sudo chown $(whoami):$(whoami) /var/log/bs_server/bs_server.log

sudo mkdir -p /var/log/bs_server
sudo touch /var/log/bs_client/bs_client.log
sudo chown $(whoami):$(whoami) /var/log/bs_client/bs_client.log