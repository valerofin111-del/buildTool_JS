import subprocess as bash
import os

def build():

    def question():
        return str(input(">> ")).lower().strip()


    print("Choose a project name")
    project_name = question()


    print("create with npm or bun? (q/w/e/r)")
    print("npm - q")
    print("yarn - w")
    print("pnpm - e")
    print("bun - r")
    package_manager = question()

    if (package_manager == "q"):
        package_manager = "npm"
    elif (package_manager == "w"):
        package_manager == "yarn"
    elif (package_manager == "e"):
        package_manager = "pnpm"
    elif (package_manager == "r"):
        package_manager = "bun"
    else:
        package_manager = "npm"


    install_command = "add"
    if (package_manager == "npm"):
        install_command = "install"


    project_framework = ""

    if (package_manager != "bun"):

        print("Choose a framework (q/w)")
        print("React - q")
        print("Vue - w")
        project_framework = question()

        if (project_framework == "q"):
            project_framework = "react"
        elif (project_framework == "w"):
            project_framework = "vue"


        print("Add TypeScript? (y/n)")
        typescript = question()

        if (typescript == "y"):
            template = project_framework + "-ts"


        bash.run(f"{package_manager} create vite@latest {project_name} -- --template {template} --yes", shell=True)
        os.chdir(project_name)

    elif (package_manager == "bun"):

        bash.run(f"bun create vite@latest {project_name}", shell=True) 
        os.chdir(project_name)


    add_lib = package_manager, install_command

    if (project_framework == "react"):

        print("Add react-router-dom? (y/n)")
        react_router_dom = question()

        print("Add state manager? (q/w/n)")
        print("Zustand - q")
        print("Jotai - w")
        print("no - n")
        state_manager = question()

        print("Add React Hook Form? (y/n)")
        react_hook_form = question()

        print("Add Tanstack Query? (y/n)")
        tanstack_query = question()

        zod = "n"
        if (typescript == "y"):
            print("Add Zod? (y/n)")
            zod = question()
        
        if (state_manager == "q"):
            bash.run([add_lib, "zustand@latest"])
        elif (state_manager == "w"):
            bash.run([add_lib, "jotai@latest"])

        if (react_router_dom == "y"):
            bash.run([add_lib, "react-router-dom@latest"])

        if (react_hook_form == "y"):
            bash.run([add_lib, "react-hook-form@latest"])

            if (zod == "y"):
                bash.run([add_lib, "@hookform/resolvers@latest"])
        
        if (zod == "y"):
            bash.run([add_lib, "zod@latest"])

        if (tanstack_query == "y"):
            bash.run([add_lib, "@tanstack/react-query@latest"])

    elif (project_framework == "vue"):

        print("Add vue-router? (y/n)")
        vue_router = question()

        if (vue_router == "y"):
            bash.run([add_lib, "vue-router@latest"])


if __name__ == "__main__":

    try:
        build()

    except Exception as e:
        print(e)
