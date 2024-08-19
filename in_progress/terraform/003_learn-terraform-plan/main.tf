terraform {
  required_version = "~> 1.6"
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
    random = {
      source  = "hashicorp/random"
      version = "3.5.1"
    }
  }
}

provider "docker" {}

provider "random" {}

resource "random_pet" "instance" {
  length = 2
}

resource "docker_image" "nginx" {
  name         = "nginx"
  keep_locally = false
}

resource "docker_container" "nginx" {
  image = docker_image.nginx.image_id
  name  = random_pet.instance.id

  ports {
    internal = 80
    external = 8080
  }
}

module "hello" {
  source  = "joatmon08/hello/random"
  version = "6.0.0"

  hellos = {
    hello        = random_pet.instance.id
    second_hello = "World"
  }

  some_key = "secret"
}