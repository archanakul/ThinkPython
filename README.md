# ThinkPython
All the Exercise Solution for Think Python - Version 1.1.20

# Basics of Command Line Interface(CLI) - Terminal:
#### A) ROOT Directory: Directory at the top of the directory tree & is represented by "/".
   
#### B) HOME Directory: Directory with a name usually used to login to the machine & is represented by. 
   
#### C) WORKING Directory: Directory that you are currently working in from CLI.

#### D) Syntax for CLI commands:
            <command flags arguments>
        where:
        command: That does some specific task
        flags: Options provided to common to trigger certain behavior, prefixed 
               with "-" 
        arguments: What the command is going to modify or other option for the 
                   command      

####E) Most widely used CLI commands:
    
    1. $ pwd: 
            Print the current working directory
    2. $ clear: 
            Clear the terminal screen
            
    3. ls:
             List working directory contents(UNHIDDEN files & directories)
    4. ls -a:
             List both HIDDEN (names begin with a dot (.))& UNHIDDEN working 
             directory contents
    5. ls -l: 
            List working directory contents in long format i.e with details
            
    6. cd dirPath : 
            Change working directory to given dirPath
    7. cd ..: 
            Changes working directory to a folder one level up the tree
            
    8. mkdir dirName: 
            Creats a directory with dirName under working directory  
    9. touch fileName: 
            Creats a new file with fileName under working directory
            
    10. cp fileName dirPath: 
            Copies the the fileName under working directory to a given dirPath
    11. cp -r dirName newPath: 
            Copies the directory & the entire subtree connected RECURSSIVELY in 
            working directory to newPath
    12. cp -r dirName/ newPath: 
            Copies contents of the directory rather than the directory itself to 
            newPath
            
    13. mv fileName dirPath : 
            Moves the fileName from working directory to given dirPath
    14. mv fileName newName: 
            Renames the fileName in working directory to newName
            
    15. rm fileName :
            Removes/delets the fileName from working directory  
    16. echo arguments:
            write arguments to the standard output(Screen)
    17. date:
            Display or set date & time
            
    18. source fileName:
           Takes the contents of fileName or resource & passes it to the 
           Tcl(Tool Command Line) interpreter as a text script  
    19. pbcopy
            Provide copying & pasting to pasteboard/Clipboard from command line     
            
# Setup git:
### A) Once installed successfully, check for version of git installation
                $git --version 
      should report back version number marked on the .DMG file of installer
### B) If not same then 
   1. We need to make sure the Terminal goes through the correct order 
       of folders to discover your newer version of Git.
            
            $ echo "export PATH=/usr/local/git/bin:/usr/local/bin:/usr/local/sbin:$PATH" >> ~/.bash_profile
        
   2. Tell the Terminal to look at your bash_profile to get the updated order of 
      folders (your "$PATH").
            
            $ source ~/.bash_profile -> hidden file under home directory

### C) Configuring Git identification
  1. Set your username
            
            $ git config --global user.name "Your Name Here"
  2. Set your email address
            
            $ git config --global user.email "your_name@domain.com"

# Setup Github:   
### A) Once you have created an account in Github:
    Install a utility that allows your system to authenticate with Github    
    automatically without entring username/password on each session      

### B) Check if the utility is already installed:
        $ git credential-osxkeychain
    returns below message if already installed
        Usage: git credential-osxkeychain <get|store|erase>
    returns below message if not already installed
        git: 'credential-osxkeychain' is not a git command. See 'git --help' 
    
### C) SSH(Secure Shell) key basically lets your computer uniquely identify itself when it connects to servers. 
    If Github is aware of the key your computer is using, you won’t have to 
    enter your Github username/password every time you connect.   

### D) Check for pre-existing SSH keys on your computer if not present then generate a new SSH key
   1. Point the terminal to the directory that would contain SSH keysfor your 
       user account:
       
                $ cd ~/.ssh  
   2. If you get the response “No such file or directory" then you need to 
       generate SSH key else u already have one for your machine.
   3. Create a new SSH key to use with Github if not already present using the 
       email you entered while creating Github account 
         
                $ ssh-keygen -t rsa -C "your_email@domain.com"                                             
   4. When it asks you to enter a file name in which to save the key, just 
       press return/enter  -> SSH key goes into ~/.ssh folder
   5. You will then be asked to enter a passphrase & confirm it. Enter a secure 
       passphrase

### E) Add SSH key to Github:
   1. Copy the SSH key for the computer on to clipboard
   
            $ pbcopy < ~/.ssh/id_rsa.pub
   2. login to Github account
   3. Click Add SSH key
   4. Enter a descriptive title for the computer you’re currently on
   5. Paste your SSH key on clipboard into the Key field
   6. Click Add Key
   7. Enter your Github password

### F) Test the Connectivity:
   1. Try to connect to Github using your SSH key from Terminal
   
            $ ssh -T git@github.com    
   2. We may see the following warning:
   
            "The authenticity of host 'github.com (207.97.227.239)'
             cant be established. RSA key fingerprint is             
             16:27:ac:a5:76:28:2d:36:63:1b:56:4d:eb:df:a6:48. Are you sure 
             you want to continue connecting (yes/no)? "         
   3. Type yes & press return
   4. We will have to enter our recently selected passphrase 
   5. You should then see:
   
            "Hi username! You've successfully authenticated, but GitHub does 
             not provide shell access. "   

# How to move a bunch of files in a folder into Github repository(on Linux) :
### A) Create a new repository (Name=ThinPython) on github.
### B) Open the terminal & make the new directory
        $ mkdir /usr/../ThinkPython
### C) Copy your ProjectFolder to this ThinkPython
        $ cp -r /usr/../Chapter1-Welcome  /usr/../ThinkPython
### D) Change the present work directory to ThinkPython.
        $ cd /usr/../ThinkPython
### E) Run these commands
   1. Run initialization command tocreate a git repository from working directory:
   
            $git init            
   2. Add the modified program/folder to the GIT INDEX, which is a staging area for objects prepared to be commited.
That means that the git now knows about the change, but the change hasn’t been permanently recorded in the repository yet
           
            $git add Chapter1-Welcome            
   3. Include the staged changes i.e Commit the files in the GIT INDEX to the LOCAL REPOSITORY & creates a new revision with a log
           
            $git commit -m "first commit"
            -m flag: Allows us to enter the Commit message in the same line. 
                     Commit messages are normally in present tense.                   
   4. See which remote servers you have configured, run below
            
            $ git remote
    Lists the shortnames of each remote handle you’ve specified. 
    If you’ve cloned your repository, you should at least see ORIGIN – 
    that is the default name Git gives to the server you cloned from  
   5. Display URLs that Git has stored for the shortnames to be used when reading &  writing to remote:
           
            $ git remote -v
        origin	https://github.com/Username/ThinkPython.git (fetch)
        origin	https://github.com/Username/ThinkPython.git (push) 
   6. Add a new remote Git repository as a shortname you can reference
   
            $git remote add origin https://github.com/Username/ThinkPython.git 
   7. To push your MASTER branch to your ORIGIN server
            
            $git push -u origin master
      If you & someone else clone at the same time & they push upstream & 
      then you push upstream, your push will rightly be rejected. 
            
            ! [rejected]        master -> master (non-fast-forward)
      You can fix this by fetching & merging the changes made on the remote 
      branch with the changes that you have made locally
   8. Fetches updates made to an online repository
           
            $ git fetch origin 
   9. Merges updates made online with your local work
           
            $ git merge origin YOUR_BRANCH_NAME(master) 
   10. Grabs online updates & merges them with your local work can be done by just pull rather than fetch & merge:
            
            $ git pull origin YOUR_BRANCH_NAME
                       
                                  
            
          
            
