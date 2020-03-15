### Connecting to aws

### make isntance
### save private key to directory
### scp -i /c/private-keys/Abdimalik-mao-eng53-ire.pem provision.db.sh ubuntu@34.244.250.46:/home/ubuntu/provision.db.sh (Transfer db files to aws isntance)
### ssh -i (location of private key) -r (recursive) app/ ubuntu@ip-address /home/ubuntu/app
### chmod provision files to allow execution through chmod 700 -R
### cd app
### npm install
### npm start
### npm run test
### pm2 start app.js - check if app is working
#### curl localhost:3000 - see html data for front page



### Create VM Jenkins Master + Ansible controller
### Jenkins Slave
### Connect VM1 and VM2 , so that ansible master can provision slave
### provision vm2 as node.js



### NAT Gateway is a device that allows requests to come out of a private network and responses to ocme back. But it doesnt allow incoming requests

Request/Outbound
Private ip - Router - Defauly Gateway - Internet Gateway - DNS Server - Public IP
Respond/Inbound
Public IP - NAT Gateway + NAT Table/Router - Private IP
AWS VPC
### Create VPC
### Create internet gateway - Attach VPC - Create Subnet (for public/private IP) CLASS C SUBNET [10.1.1.0/24] [10.1.2.0/24] - Has its own network ACL
### create new route table to connect private and public ip
### edit route table association to public ip
### within your private and public subnet you can create EC2 instance(nginx)
### (stateless)N-ACL For VPC and subnet,(stateful) Security Group for EC2 instances

### To connect Public vpc to Private to vpc you have to allow 4 fences (PubSG,PubN-ACL,Priv-ACL,PrivSG) - Both ways
### Remebers state of object = stateful (requires only inbound-NACL-VPC,SUBNET), Dont remember state = stateless (requires only inbound and outbound, SG, EC2)

### CIDR Block = choose nodes that you want ipv4
### NAT Gateway = allows instances in private subnet to connect to internet
### NACL = Firewall provided by aws for VPC and subnets
### Route table = set of rules called routes which determines where network traffic from your subnet or gateway
### subnet = range of ip addresses in your VPC

### A VPC with a size /16 IPv4 CIDR block (example: 10.0.0.0/16). This provides 65,536 private IPv4 addresses.

A public subnet with a size /24 IPv4 CIDR block (example: 10.0.0.0/24). This provides 256 private IPv4 addresses. A public subnet is a subnet that's associated with a route table that has a route to an Internet gateway.

A private subnet with a size /24 IPv4 CIDR block (example: 10.0.1.0/24). This provides 256 private IPv4 addresses.

### if ip is inside subnet it shouts it, if not it routes it

### Bastion host
 - Fortified host standing guard as the first line of defence to protect server from any intruders
 - Allows you to access linux instances without exposing environment to internet
 - slows down attackers and protects against port scanning, can also see logs and prevent rogue SSH access
 - Nginx and SSH
 - stand in public subnet, built with strong security protection, can be accessed via ssh from internet and can have SSH access to private instance

 ansible-playbook --vault-password-file aws_password aws_provision.yml