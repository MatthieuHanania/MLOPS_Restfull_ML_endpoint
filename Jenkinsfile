pipeline{
  agent any
  stages{
    
    //stage to see if everything works correctly
    stage("Hello word"){
      steps{
        echo 'hello word'
      }    
    }
    
    //Do the unittest
    stage("Testing"){
      steps{
        echo 'testing'
        bat' python -m test_main'
      }
    }
    
    //stage to build and run the docker image
    stage("Docker Image"){
      steps{
        echo 'building docker image'
        bat 'docker build -t restapimage .'
        echo 'running the image'
        bat 'docker run -p 5000:5000 -d restapimage'
      }
    }

  }
}


