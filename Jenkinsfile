pipeline {
  agent any
  
   stages {
       stage("Creating users and groups") {
           steps {
               sh """
                    python userdel.py
               """
           }//stages 
       }//steps
       stage("Adding users to groups") {
           steps{
               sh """
                  python groups.py 
               """
           }//stage
       }//steps
   }//pipeline
}
     post{
           always{
               sh """
                  python test.py
               """
           }//post
     }//always
