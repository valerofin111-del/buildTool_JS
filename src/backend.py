import subprocess as bash
from tools import *

# Backend libs versions
express_version = indent + '"express": "^4.19.0"'
fastify_version = indent + '"fastify": "^4.26.0"'
hono_version = indent + '"hono": "^4.0.0"' + indent + '"@hono/node-server": "^1.8.0"'

def backend_build(project_name, project_path):

    # Framework choice
    question("Chose a framework (q/w/e/r)")

    print(style('Vanilla JS / q', color=Style.BLACK))
    print(style('Express / w', color=Style.YELLOW))
    print(style('Fastify / e', color=Style.BLUE))
    print(style('Hono / r', color=Style.MAGENTA))

    project_framework = answer()

    match (project_framework):
        
        case "q":

            dependcies = ''

        case "w":

            dependcies = express_version

        case "e":

            dependcies = fastify_version

        case "r":

            dependcies = hono_version
        
        case _:
            dependcies = ''

    # Files for backend project
    index_js_vanilla = f"""import http from 'node:http';
import 'dotenv/config';

var PORT = Number(process.env.PORT) || 3000;

var server = http.createServer((req, res) => {{
res.writeHead(200, {{ 'Content-Type': 'application/json; charset=utf-8' }});

if (req.url === '/') {{

    res.end(JSON.stringify('{project_name}'));
}}
}});

server.listen(PORT, () => {{
    console.log(`http://localhost:${{PORT}}`);
}});"""

    index_js_express = f"""import express from 'express';
import 'dotenv/config';

var PORT = Number(process.env.PORT) || 3000;

var app = express();

app.get('/', (req, res) => res.json('{project_name}'));

app.listen(PORT, () => console.log(`http://localhost:${{PORT}}`));"""

    index_js_fastify = f"""import Fastify from 'fastify';
import 'dotenv/config';

var PORT = Number(process.env.PORT) || 3000;

var app = Fastify();

app.get('/', async (req, reply) => {{

    reply.type('application/json'); 

    return JSON.stringify('123')
}});

app.listen({{ port: PORT }}, () => console.log(`http://localhost:${{PORT}}`));"""        

    index_js_hono = f"""import {{ Hono }} from 'hono';
import {{ serve }} from '@hono/node-server';
import 'dotenv/config';

var PORT = Number(process.env.PORT) || 3000;

var app = new Hono();

app.get('/', (c) => c.json('{project_name}'));

serve({{
    fetch: app.fetch,
    port: PORT
}}, (info) => {{
    console.log(`http://localhost:${{info.port}}`)
}});"""

    package_json = f"""{{
    "name": "{project_name}",
    "version": "1.0.0",
    "description": "",
    "main": "index.js",
    "scripts": {{
        "dev": "node --watch index.js"
    }},
    "dependencies": {{
        "dotenv": "^16.4.7"{dependcies} 
    }},
    "keywords": [],
    "author": "",
    "license": "ISC",
    "type": "module"
}}"""

    env = f"""PORT=''
DATABASE_URL=''
API_KEY=''"""

    match (project_framework):
        
        case "q":

            index_js = index_js_vanilla

        case "w":

            index_js = index_js_express

        case "e":

            index_js = index_js_fastify

        case "r":

            index_js = index_js_hono

        case _:
            index_js = index_js_vanilla

    files = {
        "index.js": index_js,
        "package.json": package_json,
        ".env": env,
        '.gitignore': git_ignore
    }

    build_files(files, project_path)

    bash.run("mkdir routes", shell=True, cwd=project_path)
    bash.run("mkdir controllers", shell=True, cwd=project_path)
