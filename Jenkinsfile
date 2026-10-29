pipeline {
    agent any

    stages {
        stage('Check Environment') {
            steps {
                bat 'python --version'
                bat 'git --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Run Automated Tests') {
            steps {
                bat 'python -m pytest -v'
            }
        }

        stage('Run Application') {
            steps {
                bat 'python hello.py'
            }
        }
    }

    post {
        success {
            echo 'SUCCESS: MLOps pipeline completed!'
        }
        failure {
            echo 'FAILED: Check the Console Output for errors.'
        }
    }
}
