pipeline {
  agent {
    docker {
      image 'python:3.8'
      args "-e HOME=${JENKINS_HOME}"
    }
  }
  stages {
    stage('Unit Tests') {
      steps {
        sh 'pip install -r requirements.txt --user'
        sh 'pytest'
      }
    }
    stage('Static Analysis') {
      steps {
        sh 'pylint src/cs334demo/*.py tests/*.py'
      }
    }
  }
}