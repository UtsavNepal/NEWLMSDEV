pipeline {
    agent any
    environment {
        EMAIL_CREDS = credentials('jenkins-email-credentials')
        DB_CREDS = credentials('jenkins-db-credentials')
    }
    stages {
        stage('Prepare Environment') {
            steps {
                writeFile file: 'LMS/.env', text: """
SECRET_KEY=django-insecure-#ipqde3_+@)1-r0kmbfb+b)n6r&n(9zpgnsv^7sit+40+q1(k1
DEBUG=True
ALLOWED_HOSTS=utsav.kutumbatech.com.np,110.34.2.30,localhost,127.0.0.1

EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=${env.EMAIL_CREDS_USR}
EMAIL_HOST_PASSWORD=${env.EMAIL_CREDS_PSW}
CORS_ALLOWED_ORIGINS=http://utsav.kutumbatech.com.np:5005,http://110.34.2.30:5005,http://localhost:5005

DB_NAME=lmss
DB_USER=${env.DB_CREDS_USR}
DB_PASSWORD=${env.DB_CREDS_PSW}
DB_HOST=localhost
DB_PORT=5432
"""
            }
        }
        stage('Build and Deploy with Docker Compose') {
            steps {
                dir('DevOps') {
                    bat 'docker-compose down -v'
                    bat 'docker-compose build --no-cache'
                    bat 'docker-compose up -d'
                }
            }
        }
    }
}
