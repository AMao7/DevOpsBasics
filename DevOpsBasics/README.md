    ## Introduction to DevOps

    ### What is DevOps?

    - Set of practises in software development from operation to production (higher quality and shorter time)
    - Collaboration of Dev and Ops
    - CI, CD and CD
    - Automation through monitoring and testing
    - Cross-functional teams (culture)
    - Shorter lifecycle and higher quality for development
    - Turning challenges into benefits

    ### Four pillars of DevOps
    - Ease of use
    - Flexibility
    - Robustness
    - Costs


    ### DevOps value (CAMS)
    - Collaboration
    - Measurement
    - Automation
    - Culture

    ### DevOps Principles
    - Customer-centric action
    - End to end responsibility
    - CI, CD and CD
    - Automate everything
    - Work as one team
    - Monitor and test everything

    ### Stages in DevOps Lifecycle
    - Continuous Development
    - Continuous Testing
    - Continuous Intergration (tests of merged branches)
    - Continuous Deployment
    - Continuous Monitoring

    ### DevOps tool
    - Code = Git, GitHub, GitLab, Pycharm
    - Build = Maven, Gradle , Apache
    - Test = JUnit and SE
    - Release = Jenkins and Bamboo
    - Deploy = Puppet, CHEF, ANSIBLE and SALTSTACK
    - Operate
    - Monitor = Nagios, Splunk and Sensu

    ### DevOps Implementation
    - Cloud platform = AWS, GCP and Azure
    - Infrastucture Architecture = Virtualization and Containerization (Docker)
    - DevOps Implementation = IaC, IaaS, Iaap (service) and Iaap (product)
    - Difference between virtual environments (takes resources even if it isnt using it)
    vs containers (no allocation of resources needed, just takes what it needs)

    ### Development Environment
    - Standardised
    - One for one application
    - Close to production environment
    - Robust, fast and easy to rebuild
    - Portable, decoupled from hardware or platform (VM and Container)

    ### Building a development environment
    - Technologies (Vagrant and VM)
    - Architecture (Windows, Vagrant, VM and Dev Environments)
      - Dev Environment such as Nginx, Node.js, MongoDB and Ruby
   
### Making new environment
1. Vagrant init (ubuntu/bionic64) - to initalise vagrantfile for ubuntu box
2. Vagrant up - makes the virtual machine 
3. Vagrant ssh - to make key (sync folder to the root vagrant folder)
        4. sudo apt-get update - to update software inventory
        5. sudo apt-get upgrade -y - says yes automatically to upgrades
        6. sudo apt-get install nginx -y - to install open source webserver
        7. sudo systemctl start nginx - to start nginx on new system
8. ps aux | grep nginx 
9. wget 127.0.0.1:80 - connects to web (port number 80)
 - ifconfig  = finds out about the settings of the vm
 
#### Example of vagrant file
````
Vagrant.configure("2") do |config|

  config.vm.box = "ubuntu/bionic64"
  config.vm.network "private_network", ip: "192.168.10.100"
  config.hostsupdater.aliases = ["development.local"]
  config.vm.provider "virtualbox" do |v|
     v.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
     v.customize ["modifyvm", :id, "--natdnsproxy1", "on"]
  end
end
````

### Other commands
- cat /etc/hosts - to find whats in the host pc
- vagrant reload - to reload the vm without destroying it
- .. are parent files, . is the file you are in
- file (example.txt) - tells you info about the file
- cp (filename.txt)(filename.jpg) - copy file to make a different file type
- touch/mkdir .hidden_file/directory - to create a hidden file (ls-a or ll can view it)
- man (commandname) - to find manual for that command (RTFM)
- tar --create --verbose --file archive.tar . - creates a archive file
- ls e* = to display every file that start with a 'e'
- ls example[1-3].txt - finds example 1-3.txt file
- head -2 (file).txt - shows top 2 text lines
- tail -2 (file).txt - shows bottom 2 text lines
- sort (file).txt - sorts file by alphabetical order
- nl (file).txt - enumerate file text
- wc (file).txt - words count (word break, n. of lines and character count)
- cut, tac, sed, uniqueinq
- STDINN (0) , STDOUT (1), STDERR (2) 
- top - shows you current processes 
- top & - adds soemthing to the t   op
- kill -9 (process) - to kill the process
- 
- ps (process) aux (all users) | grep (group by) (what you wanna group)
- ls > dir_list.txt - creates dir_list.txt which contains all the files on the directory 
(overwrites if one exists already)
- ls >> dir_list.txt - appends all files again
- ls missing_dir 2> error_log.txt - saves error message to error_log.txt file
- - ````
    ls example* missing_directory > ls_log.txt 2>&1
    cat ls_log.txt
    ````
    - takes error and standard output to ls_log.txt

- Bash directory permissions
    - chmode 777 to give every user full access 
    - r (4) = read, w (2) = write and x (1) = execute
    - first 3 are owner, second 3 are group and last 3 are others
```
-rwxrwxrwx 1 vagrant vagrant  1154 Jan 19 20:05  example.txt*
-rwxrwxrwx 1 vagrant vagrant     0 Jan 19 20:05  example1.txt*
-rwxrwxrwx 1 vagrant vagrant     0 Jan 19 20:05  example2.txt*
-rwxrwxrwx 1 vagrant vagrant     0 Jan 19 20:05  example3.txt*
drwxrwxrwx 1 vagrant vagrant     0 Feb 18 14:07 'my photos'/
-rwxrwxrwx 1 vagrant vagrant 27297 Jan 19 20:05  puppy.jpg*
-rwxrwxrwx 1 vagrant vagrant 27297 Feb 18 14:01  puppy.txt*
-rwxrwxrwx 1 vagrant vagrant   117 Jan 19 20:05  words.txt*
````
 

