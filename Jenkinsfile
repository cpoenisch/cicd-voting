pipeline {
  options {
    buildDiscarder(logRotator(numToKeepStr: '10'))
    ansiColor('xterm')
    timestamps()
    timeout(time: 10, unit: 'MINUTES')
  }
  agent {
    docker { image 'python:3.8.5-alpine' }
    //dockerfile { filename 'Dockerfile' }
  }
  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }
    stage('Setup') {
      steps {
        script {
          sh """
          python --version
          pip install -r requirements.txt
          """
        }
      }
    }
    stage('Linting') {
      steps {
        script {
          sh """
          pylint --rcfile=pylint.cfg app pages voting --msg-template="{path}:{line}: [{msg_id}({symbol}), {obj}] {msg}"
          recordIssues tool: pyLint(pattern: 'pylint.log')
          """
        }
      }
    }
    stage('Unit Testing') {
      steps {
        script {
          sh """
          python ./manage.py test
          """
        }
      }
    }
  }
}
