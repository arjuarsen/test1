pipeline {
    agent { docker { image 'python:3.5.1' } }
    stages {
        stage('check version') {
            steps {
                sh 'python --version'
            }
        }
    }
}
