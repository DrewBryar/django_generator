import shutil, os, sys

from user_prompt import *

# Prompt the User to give vital Info

# Ask for the Project Name and App Name
# proj_name = input("Please input Project Name: ")

# app_name = input("Please input App Name: ")

# proj_location = input("And finally, where would you like this project to be stored?")

def generateProj():
    cwd = os.path.dirname(os.path.realpath(__file__))
    result = start_prompt()
    # Asking the big questions. What, who and where.
    proj_name, proj_location, app_name = result
    try:
        
        os.chdir(proj_location)
        os.system("django-admin startproject "+proj_name)
        print(f'Created a file named {proj_name}.')
    except FileExistsError:
        print(f'Directory Already Exists.')
    
    os.remove(proj_location +"/"+ proj_name + "/" + proj_name+"/urls.py")
    # The above shoudl remove our old urls.py and...
     
    os.chdir(proj_location +"/"+ proj_name)
    shutil.copy2(cwd+"/prourls.py", proj_name+"/urls.py")
    
    # We need to build our "apps" folder.
    os.mkdir("apps")
    # Move into proj_name/proj_name to replace URLS
    
    
    # Move into apps.
    os.chdir(proj_location +"/"+ proj_name+"/apps")
    os.mkdir(app_name)
    os.chdir(proj_location +"/"+ proj_name+"/apps/"+ app_name)
    print(os.getcwd())
generateProj()