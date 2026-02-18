import subprocess as bash

indent = ',\n        '

# Styling functionality
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
    BG_WHITE   = '\033[47m'

    BOLD = '\033[1m'
    UNDERLINE  = '\033[4m'
    RESET = '\033[0m'

def style(text, color=Style.BLACK, bg=Style.BG_WHITE, bold=True, underline=False, reset=True):

    bold_text = Style.BOLD if bold else "" 
    underline_text = Style.UNDERLINE if underline else ""
    reset_colors = Style.RESET if reset else ""

    return (f"{bold_text}{underline_text}{bg}{color} {text} {reset_colors}")

# Build files function
def build_files(files, path):

    for filename, content in files.items():

        script = f"cat <<'EOF' > {filename}\n{content}\nEOF"
        bash.run(script, shell=True, cwd=path)

# Input function
def answer():

    return input(style(">>", color=Style.WHITE, bg=Style.BG_BLACK)).lower().strip()

# Print functions        
def question(text : str):

    return print(style(f"{text}", color=Style.CYAN))


def success(project_name = False, package_manager = False, run_script = False, component_name = False):

    if (project_name):

        print(style(f"cd {project_name}", color=Style.GREEN, bg=Style.BG_BLACK))

    if (package_manager):

        print(style(f"{package_manager} install", color=Style.GREEN, bg=Style.BG_BLACK))

    if (run_script):

        print(style(run_script, color=Style.GREEN, bg=Style.BG_BLACK))

    if (component_name):

        print(style(f'"{component_name}" created', color=Style.GREEN, bg=Style.BG_BLACK))


def error(text : str):

    return print(style(f"{text}", color=Style.RED, bg=Style.BG_BLACK))

# .gitignore file
git_ignore = f"""logs
*.log
npm-debug.log*
yarn-debug.log*
yarn-error.log*
pnpm-debug.log*
lerna-debug.log*

node_modules
dist
dist-ssr
*.local

.vscode/*
!.vscode/extensions.json
.idea
.DS_Store
*.suo
*.ntvs*
*.njsproj
*.sln
*.sw?"""
