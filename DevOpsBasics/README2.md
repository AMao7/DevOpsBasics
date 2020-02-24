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


