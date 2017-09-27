pipeline {
    agent any;

    stages {
        stage('deploy') {
            steps {
                sh "ansible-playbook -i inventario hello-openshift/tasks/main.yml"
            }
        }
	stage("final"){
		sh "echo terminando job"
	}
    }
}
