
default= True

def start_prompt():
    if default:
        x = r"C:\Users\abrya\Desktop\Test"
        return ('dummy', x, 'app_name')

    proj_name = input("Please input Project Name: ")

    app_name = input("Please input App Name: ")

    proj_location = input("And finally, where would you like this project to be stored?")
    
    print(f'Terrific, what I have is that you want your Project named {proj_name} with an app, {app_name} stored at {proj_location}. Is this correct?')

    finish_creation =input ('y/n: ')

    if finish_creation == 'y':
        print("Perfect. Starting file creation. One moment.")
        return proj_name, proj_location, app_name
    else:
        print("I'm sorry about about that, either I didn't undesrtand you, or you didn't input something right. Let's start again.")
        
    

