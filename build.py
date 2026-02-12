import subprocess as bash
import os

def build():

    # Functions
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

            return input(style(">> ", color=Style.MAGENTA)).lower().strip()


    # Project name
    print(style("Choose a project name", color=Style.CYAN))
    project_name = question()

    # Pm
    print(style("\ncreate with npm or bun? (q/w/e/r)\n", color=Style.CYAN))

    print(style("npm / q", color=Style.MAGENTA))
    print(style("yarn / w", color=Style.MAGENTA))
    print(style("pnpm / e", color=Style.MAGENTA))
    print(style("bun / r\n", color=Style.MAGENTA))

    package_manager = question()

    if (package_manager == "q"):
        package_manager = "npm"
    elif (package_manager == "w"):
        package_manager = "yarn"
    elif (package_manager == "e"):
        package_manager = "pnpm"
    elif (package_manager == "r"):
        package_manager = "bun"
    else:
        package_manager = "npm"

    install_command = "add"
    if (package_manager == "npm"):
        install_command = "install"

    pm_install = f"{package_manager} install" 

    add_lib = f"{package_manager} {install_command}"

    # Framework choice
    print(style("\nChoose a framework (q/w)", color=Style.CYAN))

    print(style("React / q", color=Style.BLUE))
    print(style("Vue / w\n", color=Style.GREEN))

    project_framework = question()

    if (project_framework == "q"):
        project_framework = "react"
    elif (project_framework == "w"):
        project_framework = "vue"

    # React build
    if (project_framework == "react"):

        index_html =    f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{project_name}</title>
</head>
    <body>
        <div id="root"></div>
            <script type="module" src="./Init.jsx"></script>
    </body>
</html>"""
        
        vite_config =    """import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
    plugins: [react()],
})"""
        
        package_json =  f"""{{"name": "{project_name}",
"private": true,
"version": "0.0.0",
"type": "module",
"scripts": {{
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview"
}},
"dependencies": {{
    "react": "^18.2.0",
    "react-dom": "^18.2.0"
}},
"devDependencies": {{
    "@types/react": "^18.2.0",
    "@types/react-dom": "^18.2.0",
    "@vitejs/plugin-react": "^4.0.0",
    "vite": "^4.4.0"
}}
}}"""
        
        init_jsx =       """import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'

ReactDOM.createRoot(document.getElementById('root')).render(
    <React.StrictMode>
        <App />
    </React.StrictMode>,
)"""
        
        app_jsx =       f"""import React from 'react'

var App = function () {{
    return (
        <>{project_name}</>
    )
}}

export default App"""

        files = {
            "index.html": index_html,
            "vite.config.js": vite_config,
            "package.json": package_json,
            "Init.jsx": init_jsx,
            "App.jsx": app_jsx
        }

        project_path = os.path.abspath(project_name)
        os.makedirs(project_path, exist_ok=True)

        for filename, content in files.items():

            script = f"cat <<'EOF' > {filename}\n{content}\nEOF"
            bash.run(script, shell=True, cwd=project_path)
        
        bash.run(pm_install, shell=True, cwd=project_path)


        print(style("\nAdd react-router-dom? (y/n)", color=Style.CYAN))

        react_router_dom = question()

        if (react_router_dom == "y"):

            bash.run(f"{add_lib} react-router-dom@latest", shell=True, cwd=project_path)

        print(style("\nAdd Sass? (y/n)", color=Style.CYAN))


        sass = question()

        if (sass == "y"):

            bash.run(f"{add_lib} -g sass", shell=True, cwd=project_path)


    # Vue build
    elif (project_framework == "vue"):

        bash.run()

        print("Add vue-router? (y/n)")

        vue_router = question()

        if (vue_router == "y"):

            bash.run(f"{add_lib} react-router-dom@latest", shell=True, cwd=project_path)


        sass = question()

        if (sass == "y"):

            bash.run(f"{add_lib} -g sass", shell=True, cwd=project_path)

if __name__ == "__main__":

    try:
        build()

    except Exception as e:
        print(e)
