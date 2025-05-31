pipeline {
    agent any
    stages {
        stage('Build and Deploy with Docker Compose') {
            steps {
                dir('DevOps') {
                    bat 'docker-compose down -v'
                    bat 'docker-compose build'
                    bat 'docker-compose up -d'
                }
            }
        }
    }
}
