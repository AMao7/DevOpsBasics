# Infrastructure as Code

### Types of IT infrastructure
- On premises + immutability
    - Hardware waste + High labour cost
- On premises + Mutability - A lot of company running this way
    - Inefficient + High running cost + security concerns
- Cloud + Mutability
    - Inefficient + not using cloud's advantage
- Cloud + Immutability - Becoming popular
    - Efficient + cost reduction + flexibility
    
### IaC 
- Provision and manage IT infrastructure through source code (info of all your environment- has provision)
    - Benefits = Costs saving, speed, simplicity, minimisation of risk and config consistency
    - Best practices = Codify, Maintain version control, CT, CI, CD, modular and immutability
  
### 2 parts of IaC
 - Configuarion Management = Provisioning
    - Ansible, Puppet and Chef
    
 - Orchestration = tools and scripts that talk to cloud and pull then together into the architecture
    - CloudFormation, Ansible and Terraform
    
    Chef/ansible takes instance and provisions it
    packer then makes image from the instance
    Terraform takes image or set of image to make environment
  