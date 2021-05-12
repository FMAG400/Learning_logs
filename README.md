# Learning_logs
An easy study note - from the Python Crash Course

1.Background

    To get started with the Django framework, write a Web application called "learning_log."

2.Install

    (1) Build virtual environment. 
        Create a directory named 'learning_log' and enter the following instructions in this directory:
          $ python3 -m venv ll_env
        If venv is not available, then:
          $ pip3 install --user virtualenv
          $ virtualenv ll_env
        
    (2) Activate virtual environment.
          $ source ll_env/bin/activate
        or shut down by:
          $ deactivate
    
    (3) Install 'Django' in this activate virtual environment.
          $ pip3 install Django==3.2.2
    
3.Usage
    
    Following the instructions in step 2, activate the virtual environment in the learning_log directory and enter the following instructions to run the project:
      $ python3 manage.py runserver
    Type http://127.0.0.1:8000/ in your browser's search bar.



