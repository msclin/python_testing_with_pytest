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
                source venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }
        stage('test') {
            steps {
                sh '''
                bash
                source venv/bin/activate
                pytest --html=reports/report.html -vv
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
                        reportName: 'Tasks Test Results',
                        reportTitles: 'Tasks Test Results'
                    ])
                }
            }
        }
    }
}