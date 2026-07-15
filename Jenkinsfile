pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Install & Test') {
            agent {
                docker {
                    image 'python:3.11-slim'
                    args '-u root'
                }
            }
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
            junit allowEmptyResults: true, testResults: 'report.xml'
        }
    }
}