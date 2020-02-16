node
{
    stage('Fetch')
    {
        checkout scm
    }
    stage('Unit Testing')
    {
        sh 'pip3 install -r requirements.txt'
        sh `pytest`
    }
    stage('Static Analysis')
    {
        sh 'pylint src/abv/*.py tests/*.py'
    }
}