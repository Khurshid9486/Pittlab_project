pipeline {
  agent any
  
   stages {
       stage("makins sure that users are deleted first") {
           steps {
               sh """
                    python userdel.py
               """
           }//stages 
       }//steps
       stage("creating those users") {
           steps{
               sh """
                  python test.py
               """
           }//stage
       }//steps
   }//pipeline
}
      stage("adding those users to the group") {
           steps{
               sh """
                  python test.py
               """
           }//stage
       }//steps
     post{
           always{
               sh """
                  python userdel.py
               """
           }//post
     }//always
