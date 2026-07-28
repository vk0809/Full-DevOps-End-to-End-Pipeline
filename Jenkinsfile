pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "vk0908/flask-app"
        IMAGE_TAG = "${BUILD_NUMBER}"
    }

    stages {

        stage("Checkout") {
            steps {
                git branch: "master",
                    url: "https://github.com/vk0809/Full-DevOps-End-to-End-Pipeline.git"
            }
        }

        stage("Build Image") {
            steps {
                sh '''
                    docker build -t $DOCKER_IMAGE:$IMAGE_TAG .
                    docker tag $DOCKER_IMAGE:$IMAGE_TAG $DOCKER_IMAGE:latest
                '''
            }
        }

        stage("Docker Login & Push") {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'vk0908',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh '''
                        echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin

                        docker push $DOCKER_IMAGE:$IMAGE_TAG
                        docker push $DOCKER_IMAGE:latest
                    '''
                }
            }
        }
        stage("kubernet deploy") {
            steps {
                sh '''
                    kubectl set image deployment/flask-app flask-app=$IMAGE -n devops
                    kubectl rollout status deployment/flask-app -n devops
                '''
            }
        }
    }

    post {
        success {
            echo "IMAGE PUSHED SUCCESSFULLY TO DOCKER HUB"
        }

        failure {
            echo "Pipeline failed"
        }
    }
}
