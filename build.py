import subprocess as bash
import os

def build():

    class Style:

        BLACK   = '\033[30m'
        RED     = '\033[31m'
        GREEN   = '\033[32m'
        YELLOW  = '\033[33m'
        BLUE    = '\033[34m'
        MAGENTA = '\033[35m'
        CYAN    = '\033[36m'
        WHITE   = '\033[37m'
        
        BG_BLACK   = '\033[40m'
        BG_RED     = '\033[41m'
        BG_GREEN   = '\033[42m'
        BG_YELLOW  = '\033[43m'
        BG_BLUE    = '\033[44m'
        BG_MAGENTA = '\033[45m'
        BG_CYAN    = '\033[46m'
        BG_WHITE   = '\033[47m'

        BOLD = '\033[1m'
        UNDERLINE  = '\033[4m'
        RESET = '\033[0m'

    def style(text, color=Style.BLACK, bg=Style.BG_WHITE, bold=True, underline=False, reset=Style.RESET):
        bold_text = Style.BOLD if bold else "" 
        underline_text = Style.UNDERLINE if underline else ""
        return (f"{bold_text}{underline_text}{bg}{color}{text}{reset}")

    def question():
        return str(input(">> ")).lower().strip()


    print(style("Choose a project name", color=Style.MAGENTA, bg=Style.BG_WHITE))
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
