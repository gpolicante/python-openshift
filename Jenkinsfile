pipeline {
    agent any;

    stages {
        stage('deploy') {
            steps {
                sh "ansible-playbook -i inventario hello-openshift/tasks/main.yml"
            }
        }
    }
}