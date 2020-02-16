pipeline {
  agent { docker { image 'python:3.8' } }
  stages {
    stage('Unit Tests') {
      steps {
        withEnv(["HOME=${env.WORKSPACE}"]) {
          sh 'pip install -r requirements.txt --user'
          sh 'pip install -e .'
        }
      }
    }
    stage('Static Analysis') {
      steps {
        withEnv(["HOME=${env.WORKSPACE}"]) {
          sh 'pylint src/cs334demo/*.py tests/*.py'
        }
      }
    }
  }
}