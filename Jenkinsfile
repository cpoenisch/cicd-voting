pipeline {
  options {
    buildDiscarder(logRotator(numToKeepStr: '10'))
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
    stage('Prepare') {
      steps {
        script {
          sh """
          python --version
          pip install pylint unittest-xml-reporting
          """
        }
      }
    }
    stage('Lint') {
      steps {
        script {
          sh """
          pylint --rcfile=pylint.cfg --exit-zero app pages voting > pylint.log
          """
        }
        recordIssues(tools: [pyLint(pattern: 'pylint.log')])
      }
    }
    stage('Unit Test') {
      steps {
        script {
          sh """
          python ./manage.py test
          """
        }
        junit 'test-reports/unittest.xml'
      }
    }
    stage('Deploy') {
      steps {
        withCredentials([usernamePassword(credentialsId: 'heroku-git', passwordVariable: 'GIT_PASS', usernameVariable: 'GIT_USER')]) {
          sh """
          echo 'machine git.heroku.com \
login ${GIT_USER} \
password ${GIT_PASS}' > ~/.netrc
          git remote add heroku https://git.heroku.com/cicd-voting.git
          git remote -v
          git checkout ${GIT_BRANCH}
          git push heroku ${GIT_BRANCH}:master
          """
        }
      }
    }
  }
}
