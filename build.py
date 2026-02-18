#!/usr/bin/env python3

import sys
import os

script_dir = os.path.dirname(os.path.realpath(__file__))
src_path = os.path.join(script_dir, 'src')
sys.path.insert(0, src_path)

from tools import *
from setup import *
from frontend import *
from backend import *

# Main function
def build():

    # Building process

    side, project_name, package_manager, run_script, project_path = setup_build()

    if (side == "frontend"):

        frontend_build(project_name, project_path)

    else:
        backend_build(project_name, project_path)

    # Advice
    advice(f"cd {project_name}")
    advice(f"{package_manager} install")
    advice(run_script)

# Entry point
if __name__ == "__main__":

    try:
        build()

    except:
        print()
        print(style("!!! Exit !!!", color=Style.RED, bg=Style.BG_BLACK))
