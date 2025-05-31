pipeline {
    agent any
    stages {
        stage('Prepare Environment') {
            steps {
                writeFile file: 'LMS/.env', text: '''
SECRET_KEY=django-insecure-#ipqde3_+@)1-r0kmbfb+b)n6r&n(9zpgnsv^7sit+40+q1(k1
DEBUG=True
ALLOWED_HOSTS=utsav.kutumbatech.com.np,110.34.2.30,localhost,127.0.0.1


EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=aayushbajracharya90@gmail.com
EMAIL_HOST_PASSWORD=fxac asfd yqht wfmf
CORS_ALLOWED_ORIGINS=http://utsav.kutumbatech.com.np:5005,http://110.34.2.30:5005,localhost:5005,http://localhost:5005


DB_NAME=lmss
DB_USER=postgres
DB_PASSWORD=abc123
DB_HOST=localhost
DB_PORT=5432
'''
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
