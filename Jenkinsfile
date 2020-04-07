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
       stage("Adding users to groups")i {
           steps{
               sh """
                  python groups.py 
               """
           }
       }
       stages{
           stage ("Deleting users")
               steps {
                   sh """
                       userdel -r Jasur
                       userdel -r Javlon
                       userdel -r Aziz
                   """
               }
       }
  
  }
}