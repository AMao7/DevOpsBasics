# Getting Set up with VM (ruby)

### installing ruby test script
1. install ruby from rubyinstaller
2. on git bash run gem install bundler
3. run bundle intall
4. run rake spec

### Provisioning
1. touch provision.sh
2. ```#!/bin/bash
    sudo apt-get update -y
    sudo apt-get upgrade -y 
    sudo apt-get install nginx -y 
    curl -sL https://deb.nodesource.com/setup_13.x | sudo -E bash -
    sudo apt-get install -y nodejs
    sudo npm i -g pm2
   ````
3. privileged: false to use as root (true means as root)
   
 

### Vagrantfile content
````
required_plugins = ["vagrant-hostsupdater"]
required_plugins.each do |plugin|
    exec "vagrant plugin install #{plugin}" unless Vagrant.has_plugin? plugin
end

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/bionic64"
  config.vm.network "private_network", ip: "192.168.10.100"
  config.hostsupdater.aliases = ["development.local"]
  config.vm.synced_folder "app", "/app"
  config.vm.provision "shell", path: "environment/provision.sh", privileged: false
  config.vm.provider "virtualbox" do |v|

      v.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
      v.customize ["modifyvm", :id, "--natdnsproxy1", "on"]
  end
end
````


### Actual testing
1. cd /app
2. npm install
3. npm start &
4. wget 127.0.0.1:3000
5. npm test


### Environment Variable
````
MY_VAR =hello
echo $MY_VAR
DIR=$(pwd)
echo $DIR
LIST=$(ll)
echo $LIST
mkdir test
cd test
touch my_script.sh
vi my_scipt.sh
MY_VAR=hello
./myscript.sh
Export MY_VAR
````

### more bash commands
- cat.bash_history - shows history of previous commands
- history | grep kill - find out who typed previous command kill
- printenv - finds out everyhting 
- $ shows path but : means append

 for log in:

````
./.bash_profile
./.bash_login
./.bashrc 
````

### Two virtual machines connected
Vagrant file content:
````
# Install required plugins
required_plugins = ["vagrant-hostsupdater"]
required_plugins.each do |plugin|
    exec "vagrant plugin install #{plugin}" unless Vagrant.has_plugin? plugin
end

Vagrant.configure("2") do |config|
  config.vm.define "app" do |app|
    app.vm.box = "ubuntu/bionic64"
    app.vm.network "private_network", ip: "192.168.10.100"
    app.hostsupdater.aliases = ["development.local"]
    app.vm.synced_folder "app", "/home/ubuntu/app"
    app.vm.provision "shell", path: "environment/app/provision.sh", privileged: false
    config.vm.provider "virtualbox" do |v|
      v.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
      v.customize ["modifyvm", :id, "--natdnsproxy1", "on"]
    end
  end

  config.vm.define "db" do |db|
    db.vm.box = "ubuntu/bionic64"
    db.vm.network "private_network", ip: "192.168.10.150"
    db.hostsupdater.aliases = ["database.local"]
    db.vm.synced_folder "environment/db", "/home/ubuntu/environment"
    db.vm.provision "shell", path: "environment/db/provision.sh", privileged: false
     # network
  config.vm.provider "virtualbox" do |v|
    v.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
    v.customize ["modifyvm", :id, "--natdnsproxy1", "on"]
  end
  end
end
````

### Reverse Proxy Nginix
- Removing port from website to make it more user friendly
- Remove port 3000 from www.development.local:3000/posts

### Making Slave Node:
1. Vagrant file:
````
config.vm.define "jenkinsslave" do |jenkinsslave|
    jenkinsslave.vm.box = "ubuntu/bionic64"
      jenkinsslave.vm.network "private_network", ip: "192.168.10.200"
    jenkinsslave.hostsupdater.aliases = ["localhost:8080 "]
    jenkinsslave.vm.synced_folder "environment/jenkinsslave", "/home/ubuntu/jenkins"
    jenkinsslave.vm.provision "shell", path: "environment/jenkinsslave/provision.sh", privileged: false
    jenkinsslave.vm.provider "virtualbox" do |v|
      v.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
      v.customize ["modifyvm", :id, "--natdnsproxy1", "on"]
    end
  end
````
- Provision file:
````
#!/bin/bash

# Update the sources list
sudo apt-get update -y

# upgrade any packages available
sudo apt-get upgrade -y

# install git
sudo apt-get install git -y

# install nodejs
sudo apt-get install python-software-properties -y
curl -sL https://deb.nodesource.com/setup_12.x | sudo -E bash -
sudo apt-get install nodejs 

# install pm2
sudo npm install pm2 -g
sudo apt-get install openjdk-8-jre-headless -y

sudo apt-get install nginx -y

# finally, restart the nginx service so the new config takes hold
sudo service nginx restart

sudo cat /vagrant/environment/jenkinsslave/jenkin_key.pub >> /home/vagrant/.ssh/authorized_keys
````
- Make sure to have public key at location
- Private key is given to jenkins
- ssh -i cat /vagrants/environment/jenkinsslave/jenkin_key vagrant@192.168.10.200 to connect the key





