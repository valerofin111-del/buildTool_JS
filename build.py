#!/usr/bin/env python3

import sys
import os
import argparse
import subprocess as bash

script_dir = os.path.dirname(os.path.realpath(__file__))
src_path = os.path.join(script_dir, 'src')
sys.path.insert(0, src_path)

from tools import *
from setup import *
from frontend import *
from backend import *
from mvc import *
from jsx import *
from vue import *

# Main function
def build():

    # Add flags
    parser = argparse.ArgumentParser(description="buildTool_JS")

    flags = parser.add_mutually_exclusive_group()

    flags.add_argument('-f', '--frontend', action='store_true', help="Generate frontend project")
    flags.add_argument('-b', '--backend', action='store_true', help="Generate backend project")

    flags.add_argument('-m', '--mvc', action='store_true', help="Create a route && controller")

    flags.add_argument('-j', '--jsx', action='store_true', help="Create a React component ")
    flags.add_argument('-v', '--vue', action='store_true', help="Create a Vue component ")

    parser.add_argument('name', nargs='?', help="Name of project/component")

    args = parser.parse_args()

    # Building process
    match (args):

        case _ if (args.frontend):
            
            if (not args.name):

                error("!!! ADD PROJECT NAME !!!")
                sys.exit(1)

            project_name = args.name

            project_path = os.path.abspath(project_name)
            bash.run(f"mkdir {project_name}", shell=True)

            frontend_build(project_name, project_path)
            success(project_name, package_manager='<pm>', run_script='<pm> run dev')

        case _ if (args.backend):

            if (not args.name):

                error("!!! ADD PROJECT NAME !!!")
                sys.exit(1)

            project_name = args.name

            project_path = os.path.abspath(project_name)
            bash.run(f"mkdir {project_name}", shell=True)
            
            backend_build(project_name, project_path)
            success(project_name, package_manager='<pm>', run_script='<pm> run dev')

        case _ if (args.mvc):

            if (not args.name):

                error("!!! ADD ROUTE/CONTROLLER NAME !!!")
                sys.exit(1)

            mvc_build(args.name)

        case _ if (args.jsx):

            if (not args.name):

                error("!!! ADD COMPONENT NAME !!!")
                sys.exit(1)

            jsx_build(args.name)

        case _ if (args.vue):

            if (not args.name):
                
                error("!!! ADD COMPONENT NAME !!!")
                sys.exit(1)

            vue_build(args.name)

        case _:
            side, project_name, package_manager, run_script, project_path = setup_build()

            if (side == "frontend"):

                frontend_build(project_name, project_path)

            else:
                backend_build(project_name, project_path)

            success(project_name, package_manager, run_script)

# Entry point
if __name__ == "__main__":

    try:
        build()

    except SystemExit as e:

        sys.exit(e.code)

    except KeyboardInterrupt:
            
        print()    
        error("!!! EXIT !!!")
        sys.exit(130)

    except Exception:

        error("!!! ERROR !!!")
        sys.exit(1)
