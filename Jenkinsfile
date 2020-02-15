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
                    image 'csmoco1742/python_tox:1.0'
                }
            }
            steps {
                sh 'tox'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
