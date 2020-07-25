# run from user homedir (usually user is pi)

# add hostame IP to /etc/hosts

# copy ssh keys
ssh-copy-id pi@pi3w

# also put key_ron and key_ron.pub as id_rsa and id_rsa.pub into .ssh

# on target machine, homedir
sudo apt-get -y install git

mkdir git; cd git
git clone git@github.com:rsprenkels/raspberry.git

mkdir ent
