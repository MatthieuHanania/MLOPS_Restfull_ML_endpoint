pipeline{
  agent any
  stages{
    
    //stage to see if everything works correctly
    stage("Hello word"){
      steps{
        echo 'hello word'
      }    
    }
    
    
    stage("Docker Image"){
      steps{
        echo 'building docker image'
        bat 'docker build -t RESTAPImage .'
        echo 'running the image'
        bat 'docker run -p 5000:5000 -d RESTAPImage'
      }
    }

  }
}

