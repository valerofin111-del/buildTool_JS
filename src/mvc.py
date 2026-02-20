import subprocess as bash
import json
from tools import *

def mvc_build(mvc_name : str):

    with open('package.json') as package_json:

        data = json.load(package_json)

        if 'fastify' in data.get('dependencies', {}):

            project_framework = 'fastify'

        else:

            print("Don't support now :(")

    match (project_framework):

        case 'fastify':

            controller = f"""export var {mvc_name} = async (req, reply) => {{

    return {{ message: "{mvc_name}" }}; 
}};"""
            
            script = f"cat <<'EOF' > {mvc_name}Controller.js\n{controller}\nEOF"

            bash.run(script, shell=True, cwd='./src/controllers')
            bash.run(f'sed -i "1i import {{ {mvc_name} }} from \'./controllers/{mvc_name}Controller.js\';" src/Router.js', shell=True)
            bash.run(fr'sed -i "/var Router = function/a \    app.get(\'/{mvc_name.lower()}\', {mvc_name});" src/Router.js', shell=True)

        case _:

            print('error')

    color = Style.BLUE if project_framework == 'fastify' else ''

    print(style(f'"{mvc_name}" created!', color=color , bg=''))
