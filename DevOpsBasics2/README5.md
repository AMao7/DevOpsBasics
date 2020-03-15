### Chef - Jenkins - AWS

````
touch. kitchen.cloud.yml
KITCHEN_YAML=kitchen.cloud.yml kitchen test
````
````
driver:
  name: ec2
  region: eu-west-1
  require_chef_omnibus: true
  instance_type: t2.micro
  associate_public_ip: true
#  aws_ssh_key_id: Abdimalik-mao-eng53-ire.pem

  transport:

   ssh_key: /c/private-keys/Abdimalik-mao-eng53-ire.pem
````
### create environment variables for aws keys

AWS_ACCESS_KEY_ID
AWS_ACCESS_SECRET_KEY_ID
- On windows
- Build environment on jenkins
    - Use secret texts (AWS)
- Inject environment variables
KITCHEN_YAML=kitchen.cloud.yml
CHEF_LICENSE=accept

### Chef Vagrant file
````
required_plugins = %w( vagrant-hostsupdater vagrant-berkshelf )
required_plugins.each do |plugin|
    exec "vagrant plugin install #{plugin} #{ARGV.join(" ")}" unless Vagrant.has_plugin? plugin || ARGV[0] == 'plugin'
end

 

Vagrant.configure("2") do |config|

 

  config.vm.define "app" do |app|
    app.vm.box = "ubuntu/xenial64"
    app.vm.network "private_network", ip: "192.168.10.100"
    app.hostsupdater.aliases = ["development.local"]

 

    # Synced app folder
    app.vm.synced_folder "app", "/app"
    app.vm.provider "virtualbox" do |v|
     v.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
     v.customize ["modifyvm", :id, "--natdnsproxy1", "on"]
    end

 

    # provision with chef
    app.vm.provision "chef_solo" do |chef|
        chef.add_recipe "node_cookbook::default"
        chef.arguments = "--chef-license accept"
    end
  end

 

  config.vm.define "db" do |db|
    db.vm.box = "ubuntu/xenial64"
    db.vm.network "private_network", ip: "192.168.10.150"
    db.hostsupdater.aliases = ["database.local"]
    db.vm.provider "virtualbox" do |v|
     v.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
     v.customize ["modifyvm", :id, "--natdnsproxy1", "on"]
    end

 

    # provision with chef
    db.vm.provision "chef_solo" do |chef|
        chef.add_recipe "mongo_cookbook::default"
        chef.arguments = "--chef-license accept"
    end
  end
end
```
