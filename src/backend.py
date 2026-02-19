import subprocess as bash
from tools import *

# Backend libs versions
express_version = indent + '"express": "^4.19.0"'
fastify_version = indent + '"fastify": "^4.26.0"'
hono_version = indent + '"hono": "^4.0.0"' + indent + '"@hono/node-server": "^1.8.0"'

def backend_build(project_name, project_path):

    # Framework choice
    question("Chose a framework (q/w/e/r)")

    print(style('Vanilla Node.js / q', color=Style.BLACK))
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

    # Vanilla Node.js
    vanilla_index = f"""import http from 'node:http';
import 'dotenv/config';
import {{ routes }} from './routes/StartRoute.js';

var PORT = Number(process.env.PORT) || 3000;

var server = http.createServer((req, res) => {{

    if (routes[req.url]) {{
    
        routes[req.url](req, res);
    }}
}});

server.listen(PORT, () => {{

    console.log(`http://localhost:${{PORT}}`);
}});"""

    vanilla_route = f"""import {{ Start }} from '../controllers/StartController.js';

export var routes = {{ '/': Start }};"""

    vanilla_controller = f"""export var Start = (req, res) => {{
    
    res.writeHead(200, {{ 'Content-Type': 'application/json; charset=utf-8' }});
    res.end(JSON.stringify('{project_name}'));
}};"""

    # Express
    express_index = f"""import express from 'express';
import 'dotenv/config';
import router from './routes/StartRoute.js';

var PORT = Number(process.env.PORT) || 3000;
var app = express();

app.use('/', router);
app.listen(PORT, () => console.log(`http://localhost:${{PORT}}`));"""
    
    express_route = f"""import {{ Router }} from 'express';
import {{ Start }} from '../controllers/StartController.js';

var router = Router();
router.get('/', Start);

export default router;"""

    express_controller = f"""export var Start = (req, res) => res.json('{project_name}');"""

    # Fastify
    fastify_index = f"""import Fastify from 'fastify';
import 'dotenv/config';
import router from './routes/StartRoute.js';

var PORT = Number(process.env.PORT) || 3000;
var app = Fastify();

app.register(router);
app.listen({{ port: PORT }}, () => console.log(`http://localhost:${{PORT}}`));"""

    fastify_route = f"""import {{ Start }} from '../controllers/StartController.js';

export default async function (app) {{

    app.get('/', Start);
}};"""

    fastify_controller = f"""export var Start = async (req, reply) => {{
    
    reply.type('application/json'); 
    return JSON.stringify('123')
}};"""
    
    # Hono
    hono_index = f"""import {{ Hono }} from 'hono';
import {{ serve }} from '@hono/node-server';
import 'dotenv/config';
import router from './routes/StartRoute.js';

var PORT = Number(process.env.PORT) || 3000;
var app = new Hono();

app.route('/', router);
serve({{ fetch: app.fetch, port: PORT }}, () => console.log(`http://localhost:${{PORT}}`));"""

    hono_route = f"""import {{ Hono }} from 'hono';
import {{ Start }} from '../controllers/StartController.js';

var router = new Hono();
router.get('/', Start);

export default router;"""

    hono_controller = f"""export var Start = (c) => c.json('{project_name}');"""

    # Config files
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

            index_js = vanilla_index
            route_js = vanilla_route
            controller_js = vanilla_controller

        case "w":

            index_js = express_index
            route_js = express_route
            controller_js = express_controller

        case "e":

            index_js = fastify_index
            route_js = fastify_route
            controller_js = fastify_controller

        case "r":

            index_js = hono_index
            route_js = hono_route
            controller_js = hono_controller

        case _:
            index_js = vanilla_index
            route_js = vanilla_route
            controller_js = vanilla_controller

    bash.run("mkdir -p routes controllers", shell=True, cwd=project_path)

    files = {
        "index.js": index_js,
        "routes/StartRoute.js": route_js,
        "controllers/StartController.js": controller_js,
        "package.json": package_json,
        ".env": env,
        '.gitignore': git_ignore
    }

    build_files(files, project_path)
