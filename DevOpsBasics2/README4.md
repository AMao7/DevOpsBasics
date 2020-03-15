# Downloading Chef
### Set environemnt variables CHEF_LICENSE = accept, set path to /c/ops/chefdk/bin

````
chef generate cookbook node_cookbook - to create new cookbook
cd node_cookbook
kitchen test
kitchen create
kitchen converge
kitchen setup
kitchen verify    
````
Testing:
````
chef exec rpsec spec
````
spc_helper.rb
````
at_exit {ChefSpec::Coverage.report!}
````
recipe cookbook
````
#
# Cookbook:: node_cookbook
# Recipe:: default
#
# Copyright:: 2020, The Authors, All Rights Reserved.

include_recipe 'apt'
include_recipe 'nodejs'

apt_update 'updated_sources' do
  action :update
end

package "nginx"
service "nginx" do
  action [:enable, :start]
end



include_recipe "apt"
include_recipe "nodejs"
nodejs_npm "pm2"



template '/etc/nginx/sites-available/proxy.conf' do
  source 'proxy.conf.erb'
  variables proxy_port: node['nginx']['proxy_port']
  notifies :restart, 'service[nginx]'
end


link '/etc/nginx/sites-enabled/proxy.conf' do
  to '/etc/nginx/sites-available/proxy.conf'
  notifies :restart, 'service[nginx]'
end

link '/etc/nginx/sites-enabled/default' do
  action :delete
  notifies :restart, 'service[nginx]'
end


````
default_spec.rb - unit test file
````
#
# Cookbook:: node_cookbook
# Spec:: default
#
# Copyright:: 2020, The Authors, All Rights Reserved.

require 'spec_helper'

describe 'node_cookbook::default' do
  context 'When all attributes are default, on Ubuntu 16.04' do
    # for a complete list of available platforms and versions see:
    # https://github.com/chefspec/fauxhai/blob/master/PLATFORMS.md
    platform 'ubuntu', '16.04'

    it 'converges successfully' do
      expect { chef_run }.to_not raise_error
    end

    it 'should install nginx' do
      expect(chef_run).to install_package "nginx"
    end

    it 'should install nodejs' do
      expect(chef_run).to install_package "nodejs"
    end

    it 'enable the nginx service' do
      expect(chef_run).to enable_service 'nginx'
    end

    it 'start the nginx service' do
      expect(chef_run).to start_service 'nginx'
    end
    it 'should install nodejs from a recipe' do
      expect(chef_run).to include_recipe("nodejs")
    end
    it 'should install pm2 via npm' do
      expect(chef_run).to install_nodejs_npm('pm2')
    end
    it 'should update source list' do
      expect(chef_run).to update_apt_update('updated_sources')
    end

    it 'should create a proxy.conf templates in /etc/nginx/sites-available' do
      expect(chef_run).to create_template "/etc/nginx/sites-available/proxy.conf"
      #.with_variables(proxy_port: 3000)
    end

    it 'should create a proxy.conf templates in /etc/nginx/sites-available' do
      expect(chef_run).to delete_link "/etc/nginx/sites-enabled/default"
    end

    it 'should create a proxy.conf templates in /etc/nginx/sites-available' do
      expect(chef_run).to create_link("/etc/nginx/sites-enabled/proxy.conf").with_link_type(:symbolic)
    end

  end

#.with(to:)
#  context 'When all attributes are default, on CentOS 7' do
    # for a complete list of available platforms and versions see:
    # https://github.com/chefspec/fauxhai/blob/master/PLATFORMS.md
#    platform 'centos', '7'

#    it 'converges successfully' do
#      expect { chef_run }.to_not raise_error
#    end
#end
end

````

integration test - inspec - requires server
````
describe port(80) do
  it { should be_listening }
end

describe service "nginx" do
  it { should be_running }
  it { should be_enabled }
end

describe http('http://localhost', enable_remote_worker: true) do
  its('status') { should cmp 502}
end

describe package('nodejs') do
  it { should be_installed }
  its('version') { should eq '8.11.2' }
end
````

### Why Chef?
- Extra and useful tools
- Speed
- Maintains state of system - only changes the things it needs to change
- Clean, reusable and easy to read


### Chef templayes and files
-  chef generate template proxy.conf
- chef generate attribute default


### Creating berks file
- push cookbooks to github (seperate for mongo and app-nodejs)
````
source 'http://supermarket.chef.io'

cookbook 'node_cookbook', git: 'git@github.com:AMao7/AppCookbook.git'
cookbook 'mongo_cookbook', git: 'git@github.com:AMao7/Mongo_Cookbook1.git'
berks vendor cookbooks
````