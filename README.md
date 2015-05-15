# ThinkPython
All the Exercise Solution for Think Python - Version 1.1.20

# Basics of Command Line Interface(CLI) - Terminal:
## ROOT Directory: Directory at the top of the directory tree & is represented by "/"
## HOME Directory: Directory with a name usually used to login to the machine & is represented by 
## WORKING Directory: Directory that you are currently working in from CLI
## Syntax for CLI commands:
<command flags arguments>
where:
command: That does some specific task
flags: options provided to common to trigger certain behavior, prefixed with "-" 
arguments:  what the command is going to modify or other option for the command      
## Most widely used CLI commands:
        * $ pwd: 
            Print the current working directory
        * $ clear: 
            Clear the terminal screen
            
        * ls:
             List working directory contents(UNHIDDEN files & directories)
        * ls -a:
             List both HIDDEN (names begin with a dot (.))& UNHIDDEN working 
             directory contents
        * ls -l: 
            List working directory contents in long format i.e with details
            
        * cd dirPath : 
            Change working directory to given dirPath
        * cd ..: 
            Changes working directory to a folder one level up the tree
            
        * mkdir dirName: 
            Creats a directory with dirName under working directory  
        * touch fileName: 
            Creats a new file with fileName under working directory
            
        * cp fileName dirPath: 
            Copies the the fileName under working directory to a given dirPath
        * cp -r dirName newPath: 
            Copies the directory & the entire subtree connected RECURSSIVELY in 
            working directory to newPath
        * cp -r dirName/ newPath: 
            Copies contents of the directory rather than the directory itself to 
            newPath
            
        * mv fileName dirPath : 
            Moves the fileName from working directory to given dirPath
        * mv fileName newName: 
            Renames the fileName in working directory to newName
            
        * rm fileName :
            Removes/delets the fileName from working directory  
        * echo arguments:
            write arguments to the standard output(Screen)
        * date:
            Display or set date & time
        * source fileName:
           Takes the contents of fileName or resource & passes it to the 
           Tcl(Tool Command Line) interpreter as a text script  
        * pbcopy
            Provide copying & pasting to pasteboard/Clipboard from command line     
            
# Setup git:
    1. Once installed successfully, check for version of git installation
                $git --version 
      should report back version number marked on the .DMG file of installer
    2. If not same then 
            * We need to make sure the Terminal goes through the correct order 
              of folders to discover your newer version of Git.
        $ echo 
        "export PATH=/usr/local/git/bin:/usr/local/bin:/usr/local/sbin:$PATH" 
        >> ~/.bash_profile

             * Tell the Terminal to look at your bash_profile to get the updated 
               order of folders (your "$PATH")
                    $ source ~/.bash_profile -> hidden file under home directory
    3. Configuring Git identification
            * Set your username
                $ git config --global user.name "Your Name Here"
            * Set your email address
                $ git config --global user.email "your_name@domain.com"
# Setup Github:   
    ## Once you have created an account in Github, install a utility that allows 
       your system to authenticate with Github automatically without entring 
       username/passeword on each session      
    ## Check if the utility is already insatlled:
                $ git credential-osxkeychain
       returns below message if already installed
                Usage: git credential-osxkeychain <get|store|erase>
       returns below message if not already installed
            git: 'credential-osxkeychain' is not a git command. See 'git 
            --help' 
    
    ## SSH(Secure Shell) key basically lets your computer uniquely identify 
       itself when it connects to servers. 
       If Github is aware of the key your computer is using, you won’t have to 
       enter your Github username/password every time you connect.   
    ## Check for pre-existing SSH keys on your computer if not present then 
       generate a new SSH key
            1. Point the terminal to the directory that would contain SSH keys 
              for your user account:
                        $ cd ~/.ssh  
            2. If you get the response “No such file or directory" then you need 
              to generate SSH key else u already have one for your machine.
            3. Create a new SSH key to use with Github if not already present 
               using the email you entered while creating Github account
                         $ ssh-keygen -t rsa -C "your_email@domain.com"                                           
            4. When it asks you to enter a file name in which to save the key, 
              just press return/enter  -> SSH key goes into ~/.ssh folder
            5. You will then be asked to enter a passphrase & confirm it. Enter 
               a secure passphrase
      ## Add SSH key to Github:
            1. Copy the SSH key for the computer on to clicpboard
                 $ pbcopy < ~/.ssh/id_rsa.pub
            2. login to Github account
            3. Click Add SSH key
            4. Enter a descriptive title for the computer you’re currently on
            5. Paste your SSH key on clipboard into the Key field
            6. Click Add Key
            7. Enter your Github password
       ##  Test the Connectivity:
            1. Try to connect to Github using your SSH key from Terminal
                    $ ssh -T git@github.com 
            2. We may see the following warning:
                " The authenticity of host 'github.com (207.97.227.239)'
                   cant be established. RSA key fingerprint is             
                   16:27:ac:a5:76:28:2d:36:63:1b:56:4d:eb:df:a6:48. Are you sure 
                   you want to continue connecting (yes/no)? "
            3. Type yes & press return
            4. We will have to enter our recently selected passphrase 
            5. You should then see:
                "Hi username! You've successfully authenticated, but GitHub does 
                not provide shell access. "   
# How to move a bunch of files ina folder into Github repository(on Linux) :

    ## Create a new repository (Name=ThinPython) on github.
    ## Open the terminal & make the new directory
                $ mkdir /usr/../ThinkPython
    ## Copy your ProjectFolder to this ThinkPython
                $ cp -r /usr/../Chapter1-Welcome  /usr/../ThinkPython
    ## Change the present work directory to ThinkPython.
                $ cd /usr/../ThinkPython
    ## Run these commands
        1. Run initialization command tocreate a git repository from working 
          directory:
                $git init
                
        2. Add the modified program/folder to the GIT INDEX, which is a staging 
          area for objects prepared to be commited.
          That means that the git now knows about the change, but the change 
          hasn’t been permanently recorded in the repository yet
                $git add Chapter1-Welcome
                
        3. Include the staged changes i.e Commit the files in the GIT INDEX to 
          the LOCAL REPOSITORY & creates a new revision with a log
                $git commit -m "first commit"
          -m flag: Allows us to enter the Commit message in the same line. 
                  Commit messages are normally in present tense. 
                      
        4. See which remote servers you have configured, run below
                $ git remote
          Lists the shortnames of each remote handle you’ve specified. 
          If you’ve cloned your repository, you should at least see ORIGIN – 
          that is the default name Git gives to the server you cloned from  
        5. Display URLs that Git has stored for the shortnames to be used when 
          reading &  writing to remote:  
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
        10. Grabs online updates & merges them with your local work can be done 
            by just pull rather than fetch & merge:
                $ git pull origin YOUR_BRANCH_NAME
                       
                                  
            
          
            
