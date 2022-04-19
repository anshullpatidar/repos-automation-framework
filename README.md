Github repository link:
https://github.com/anshullpatidar/repos-automation-framework

Local machine setup:

1) Install following software on local:
      1) python
      2) pytest
      3) pipenv


2) Git clone master branch from Git repository:
    git clone https://github.com/anshullpatidar/repos-automation-framework.git


3) Create branch from master branch on your local machine:
    git branch -b <branch_name>


4) Install requirements by using following command:
   pip install -r requirements.txt


5) Now start working in your branch. Once done commit your changes in you branch and then raise a merge request against master branch.


Run Testcase locally::
   We can run test using following configuration :

    Run/Debug configiration
        1. script path : path of the test suite (ex. /Users/<user_name>/PycharmProjects/automation-framework/)
        2. keywords : test case name (ex. test_repos)
        
     additional environment can be --html=report.html (To genrate html report)
    
    Run from terminal, run below commands for execution
       1. pipenv install --dev
       2. pipenv run python -m  pytest --html=report.html

WIP - Run Pipeline in Gitlab:

   TODO: Need to update in gilab-ci.yml
   We can run automation pipeline by passing following parameters :

    Target Branch : master
        1. TEST_ENV : (can be Dev/QA/Stage)
        2. PROJECT_NAME : <project_name>
        3. TEST_DIR : repos-automation-framework

     Execution environment can be Dev, QA, Stage.

