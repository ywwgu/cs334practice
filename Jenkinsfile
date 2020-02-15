pipeline {
    agent any

    stages {
        stage('Fetch') {
            steps {
                checkout scm
            }
        }
        stage('Test') {
            agent {
                docker {
                    image 'python:3.8'
                }
            }
            steps {
                sh 'pip3 install -r requirements.txt --user'
                sh 'pytest'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
