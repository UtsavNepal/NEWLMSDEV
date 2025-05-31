pipeline {
    agent any
    stages {
        stage('Install Dependencies') {
            steps {
                bat 'npm install'
            }
        }
        stage('Run Tests') {
            steps {
                bat 'npm test'
            }
        }
        stage('Build') {
            steps {
                bat 'npm run build'
            }
        }
        stage('Deploy') {
            steps {
                // Example: Copy build files to a deployment directory
                bat 'xcopy /E /I /Y build\\* C:\\deploy\\LMS'
                // Or run your own deploy script, e.g.:
                // bat 'deploy.bat'
            }
        }
    }
}
