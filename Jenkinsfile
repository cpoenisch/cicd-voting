pipeline {
  options {
    buildDiscarder(logRotator(numToKeepStr: '10'))
    ansiColor('xterm')
    timestamps()
    timeout(time: 10, unit: 'MINUTES')
  }
  agent {
    dockerfile { filename 'Dockerfile' }
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
          pip install pylint unittest-xml-reporting
          """
        }
      }
    }
    stage('Linting') {
      steps {
        script {
          sh """
          pylint --rcfile=pylint.cfg --exit-zero app pages voting > pylint.log
          """
        }
        recordIssues(tools: [pyLint(pattern: 'pylint.log')])
      }
    }
    stage('Unit Testing') {
      steps {
        script {
          sh """
          python ./manage.py test
          """
        }
        junit 'test-reports/unittest.xml'
      }
    }
  }
}
