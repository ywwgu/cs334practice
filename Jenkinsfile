pipeline {
  agent {
    docker {
      image 'python:3.8'
      args '-u root:root'
    }
  }
  stages {
    stage('Unit Tests') {
      steps {
        sh 'pip install -r requirements.txt --user'
        sh 'pip install -e .'
      }
    }
    stage('Static Analysis') {
      steps {
        sh 'pylint src/cs334demo/*.py tests/*.py'
      }
    }
  }
}