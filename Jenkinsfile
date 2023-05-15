pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                dir('Scores') {
                    sh 'docker-compose build'
                }
            }
        }

        stage('Run') {
            steps {
                dir('Scores') {
                    sh 'docker-compose up -d'
                }
            }
        }

        stage('Test') {
            steps {
                dir('Scores') {
             sh 'docker-compose exec flask_app python3 e2e.py'
                }
            }
        }

        stage('Finalize') {
            steps {
                dir('Scores') {
                    // use Jenkins credentials to login to Docker registry
                    withCredentials([usernamePassword(credentialsId: '003316d4-6108-4f65-88fb-d26b9922c254', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                        sh "docker login -u ${DOCKER_USERNAME} -p ${DOCKER_PASSWORD}"
                        sh 'docker-compose down'
                        sh 'docker-compose push'
                    }
                }
            }
        }
    }
}
