#!/usr/bin/env python3

import sys
import os
import argparse

script_dir = os.path.dirname(os.path.realpath(__file__))
src_path = os.path.join(script_dir, 'src')
sys.path.insert(0, src_path)

from tools import *
from setup import *
from frontend import *
from backend import *
from jsx import *
from vue import *

# Main function
def build():

    # Add flags
    parser = argparse.ArgumentParser(description="buildTool_JS")

    parser.add_argument('-j', '--jsx', action='store_true', help="Create a React component ")
    parser.add_argument('-v', '--vue', action='store_true', help="Create a Vue component ")
    parser.add_argument('name', nargs='?', help="Name of component")

    flags = parser.parse_args()

    # Building process
    if (flags.jsx):
        
        if (not flags.name):

            error("!!! ADD COMPONENT NAME !!!")
            sys.exit(1)

        jsx_build(flags.name)

    elif (flags.vue):

        if (not flags.name):

            error("!!! ADD COMPONENT NAME !!!")
            sys.exit(1)

        vue_build(flags.name)

    else:
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

    except Exception as e:
        print()
        error("!!! EXIT !!!")
