pipeline {
    agent any
    environment {
        $DOCKER_IMAGE = "vk0809/flask-app:v1"
        IMAGE_TAG = ${BUILD_NUMBER}
    }
    stages {
        stage ("checkout") {
            steps {
                git branch: "master"
                URL: https://github.com/vk0809/Full-DevOps-End-to-End-Pipeline.git
            }
        }
        stage ("build image") {
            steps {
                sh '''
                docker build -t $DOCKER_IMAGE:IMAGE_TAG .
                docker tag $DOCKER_IMAGE:IMAGE_TAG $DOCKER_IMAGE:LATEST
                sh '''
            }
        }
        stage ("DOCKER PUSH & LOGIN") {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'vk0908',
                    usernameVariables: 'DOCKER_USER',
                    passwordVariables: 'DOCKER_PASS'
                )]) {
                    sh '''
                    echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin
                    docker push -u $DOCKER_IMAGE:IMAGE_TAG
                    docker push -u $DOCKER_IMAGE:LATEST
                }
            }
        }
    }
    post {
        success {
            echo "IMAGE PUSH SUCCESSFULLY TO DOCKER HUB"
        }
        failure {
            echo "Pipeline failed"
        }
    }
}
