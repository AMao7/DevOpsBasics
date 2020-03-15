### Terraform

````
mkdir terraform
touch main.tf variables.tf
````

inside main.tf
````
provider "aws" {
  region = "eu-west-1"
}
````

````
terraform init
````