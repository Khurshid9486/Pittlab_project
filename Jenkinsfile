pipeline {
  agent {
       label 'generic'
  } //agent
   stages {
       stage("Creating users and groups") {
           steps {
               sh """
                    python test.py
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
