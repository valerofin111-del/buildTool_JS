import subprocess as bash
import os as script

def build():

    print("Choose a project name")
    project_name = str(input(">> ")).lower()

    print("Choose a framework (num): 1 - React, 2 - Vue")
    project_framework = str(input(">> ")).lower()

    bash.run(["npm", "create", "vite@latest", project_name, ""])
    script.chdir(project_name)
    bash.run(["npm", "install"])

    if (project_framework == "1"):
        print("Add react-router-dom? (y/n)")
        react_router = input(">> ")

        if (react_router == "y"):
            bash.run(["npm", "install", "react-router-dom@latest"])

    elif (project_framework == "2"):
        print("Add vue-router? (y/n)")
        vue_router = input(">> ")

        if (vue_router == "y"):
            bash.run(["npm", "install", "vue-router@latest"])

if __name__ == "__main__":
    try:
        build()
    except Exception as e:
        print(e)
