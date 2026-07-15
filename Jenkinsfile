pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Install & Test') {
            steps {
                sh 'pip install -r requirements.txt'
                sh 'pytest --junitxml=report.xml'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t inventory-service:latest .'
            }
        }
    }
    post {
        always {
            junit 'report.xml'
        }
    }
}