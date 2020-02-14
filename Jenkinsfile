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
                    image 'qnib/pytest'
                }
            }
            steps {
		sh 'pip3 install tox'
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
