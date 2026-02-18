from tools import *
import subprocess as bash
import os

def setup_build():

    # Side
    question('Choose (q/w)')

    print(style('Frontend / q', color=Style.RED))
    print(style('Backend / w', color=Style.BLACK))

    side = answer()

    if (side == "q"):

        side = "frontend"

    else:
        side = "backend"

    # Project name
    question("Choose a project name")

    project_name = answer()

    # Pm
    question("Choose pm (q/w/e/r)")

    print(style("npm / q", color=Style.RED))
    print(style("yarn / w", color=Style.MAGENTA))
    print(style("pnpm / e", color=Style.YELLOW))
    print(style("bun / r", color=Style.BLACK))

    package_manager = answer()

    match (package_manager):

        case "q":

            package_manager = "npm"

        case "w":

            package_manager = "yarn"

        case "e":

            package_manager = "pnpm"

        case "r":

            package_manager = "bun"

        case _:
            package_manager = "npm"

    if (package_manager == "npm"):

        run_script = "npm run dev"
    else:
        run_script = f"{package_manager} dev"

    # Create directory
    project_path = os.path.abspath(project_name)
    bash.run(f"mkdir {project_name}", shell=True)

    return side, project_name, package_manager, run_script, project_path
