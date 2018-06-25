#!/usr/bin/env bash
cd $HOME/Downloads
wget https://chromedriver.storage.googleapis.com/2.37/chromedriver_linux64.zip
unzip chromedriver_mac_13.0.775.zip
mkdir -p $HOME/bin
mv chromedriver $HOME/bin
echo "export PATH=$PATH:$HOME/bin" >> $HOME/.bash_profile
pip install pandas
pip install splinter