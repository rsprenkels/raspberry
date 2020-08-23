# run from user homedir (usually user is pi)

# add hostame IP to /etc/hosts

# copy ssh keys
ssh-copy-id pi@pi3w

# also put key_ron and key_ron.pub as id_rsa and id_rsa.pub into .ssh

# on target machine, homedir
sudo apt-get -y install git

mkdir git; cd git
git clone git@github.com:rsprenkels/raspberry.git

# get prerequiste for using venv
sudo apt-get install python3-venv

# create a venv and activate it
python3 -m venv leds
source leds/bin/activate
sudo -H pip install --upgrade --ignore-installed pip setuptools

# the lib and other stuff for led matrix
sudo apt-get install python-dev python-pip
pip install max7219
