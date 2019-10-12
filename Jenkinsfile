pipeline {
    agent {
        docker {
            image 'python:3.7.2'
        }
    }
    stages {
        stage('build') {
            steps {
                sh '''
                python -m venv venv
                . venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }
        stage('test') {
            steps {
                sh '''
                bash
                . venv/bin/activate
                pytest
                '''
            }
            post {
                always {
                    publishHTML([
                        allowMissing: false,
                        alwaysLinkToLastBuild: false,
                        keepAll: false,
                        reportDir: 'reports',
                        reportFiles: 'report.html',
                        reportName: 'HTML Report',
                        reportTitles: 'Login Test Results'
                    ])
                }
            }
        }
    }
}