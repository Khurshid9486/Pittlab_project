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
           stage ("Deleting users")
               steps {
                   sh """
                     python userdel.py
                   """
               }
       }
  
  }
