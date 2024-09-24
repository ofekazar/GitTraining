This repository is used as a training ground for new git and github users who where present in my short git presentation.
  
Get the slides presentation at: [Presentation](https://docs.google.com/presentation/d/1cxFqWHkBgOuAKvnfNQBkGSSe4aytUzByIeRcGPtsrpE/edit?usp=sharing)  
Get more hands on git training here: [Learn Git Branching](https://learngitbranching.js.org/)

# Installing Git
Go to the git download page and get the one for you operating system: https://git-scm.com/downloads  
Run the installer. These are the settings I use on my machine when installing on windows. You can use them unless you are familiar with the tool or your team require you to use different settings:
- Select Componenets: Default
- Choosing the default editor used by Git: I use Vim. If you are not familar I would recommend to use something you are familiar with.
- Adjusting the name of the initial branch in new repositories: Let Git decide ("master").
- Adjusting your PATH environment: Use Git and optional Unix tools from the Command Prompt. I highly recommend this option if you are familiar with linux terminal, it will add some of the most used commends to cmd.
- Choosing the SSH executable: Use bundled OpenSSH
- Choosing HTTPS transport backend: Use the OpenSSL library
- Configuring the line ending conversion: Checkout as-is, commit Unix-style line endings. This is the most team specific and environment specific setting in the options list. You can change this settings at a later stage.
- Configuring the terminal emulator to use with Git Bash: Use Windows' default console window
- Choose the default behavior of 'git pull': Fast-forward or merge. Another team specific option, easy to configure per project later. Use the default option when starting.
- Choose a credential helper: Git Credential Manager
- Configuring extra options: I check both. The first is for performance boost, the second is to support a feature that is normally not supported in windows so you can use repositories that are normally developed in a linux based system.
- Configuring experimental options: I keep it unchecked but if you know what it means, choose for your-self.


# Python Demo
You must have python and git installed to run this demo.  
The demo walks you through your first couple of commits with git.  
You will learn how to use the following commands:
- git init
- git add
- git commit
- git status
- git log

To run the demo, first go in the command line and cd in to this folder. Make sure both python, pip and git are installed and can run from your terminal. You can check by running the following commands:
~~~~
python --version
python -m pip --version
git --version
~~~~

Run the following to start the demo:
~~~~
python -m pip install rich
python demo.py
~~~~

# Short Pull Request Test
After finishing [Learn Git Branching](https://learngitbranching.js.org/), if you wish to try and merge a branch in to this repository you are more then welcomed.
- First clone this repository: [Cloning a repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)
- In the next steps replace your-name with your name
- Checkout in to a new branch with your name attached to it: git checkout -b feature/your-name
- Add a new file to the folder homework_folder in this repository root called your-name.txt
- Add the file to git: git add your-name.txt
- Push the changes to git: git push origin feature/your-name
- In the terminal you will see a link, go to it and create a pull request

Pull requests are a way to merge branches in to master where the repository manager has some control over which code is merged. You can read about it more here: [Github pull requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests)