### Packer

- Install packer and add to environment variable
- Create folder in Hashicorp - Packer - Bin - Packer.exe
- Creates a template instance to make image


- Create Berksfile
````
source 'http://supermarket.chef.io'

cookbook 'node_cookbook', git: 'git@github.com:AMao7/AppCookbook.git'
cookbook 'mongo_cookbook', git: 'git@github.com:AMao7/Mongo_Cookbook1.git'
````

then pass berks code
````
berks vendor cookbooks'
````

````
touch packer.json
````

- Inside packer.json insert:
````
{
{
  "variables": {
    "aws_access_key": "{{env `AWS_ACCESS_KEY_ID`}}",
    "aws_secret_key": "{{env `AWS_SECRET_ACCESS_KEY`}}",
    "version" : "{(env `GIT_TAG_NAME`)}"
  },
  "builders": [{
    "type": "amazon-ebs",

    "subnet_id": "subnet-0e9b6138ff1ce18f2",
    "ssh_keypair_name": "Abdimalik-mao-eng53-ire",
    "ssh_private_key_file": "C:/private-keys/Abdimalik-mao-eng53-ire.pem",
    "associate_public_ip_address": "true",



    "access_key": "{{user `aws_access_key`}}",
    "secret_key": "{{user `aws_secret_key`}}",
    "region": "eu-west-1",
    "source_ami_filter": {
      "filters": {
      "virtualization-type": "hvm",
      "name": "ubuntu/images/*ubuntu-xenial-16.04-amd64-server-*",
      "root-device-type": "ebs"
      },
      "owners": ["099720109477"],
      "most_recent": true
    },
    "instance_type": "t2.micro",
    "ssh_username": "ubuntu",
    "ami_name": "abdimalik-mao-eng53-nodejs-{{timestamp}}"

  }],
  "provisioners": [
    {
      "type": "chef-solo",
      "cookbook_paths": ["./cookbooks"],
      "run_list":["node_cookbook::default"]
    },
    {
      "type": "shell",
      "inline": ["mkdir /home/ubuntu/app"]
    },
    {
      "type": "file",
      "source": "app/",
      "destination": "/home/ubuntu/app"
    },
    {
      "type": "shell",
      "inline": ["cd /home/ubuntu/app","npm install"]
    }
  ]
}



````

test to see if the syntax is correct
````
packer validate packer.json
````