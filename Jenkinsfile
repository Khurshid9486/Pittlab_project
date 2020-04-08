pipeline {
    agent any
    stages {
        stage("Creating users and groups") {
            steps {
                sh """
                    python test.py
                """
            }
        }
        stage("Adding users to groups") {
            steps{
                sh """
                    python groups.py
                """
            }
        }
            stage ("Deleting users") {
                steps {
                    sh """
                    groupdel -f Aziz
                    groupdel -f Javlon
                    groupdel -f Jasur
                    userdel -rf Javlon
                    userdel -rf Jasur
                    userdel -rf Aziz 
                    """
                }
            }
    }
}