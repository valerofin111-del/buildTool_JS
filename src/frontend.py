from tools import *

# Frontend libs versions
react_router_dom_version = indent + '"react-router-dom": "^7.13.0"'
vue_router_version = indent + '"vue-router": "^5.0.1"'
pinia_version = indent + '"pinia": "^3.0.4"'
sass_version =  indent + '"sass-embedded": "^1.97.3"'

def frontend_build(project_name, project_path):

    # Framework choice
    question("Choose a framework (q/w)")

    print(style("Vanilla JS / q", color=Style.BLACK))
    print(style("React / w", color=Style.BLUE))
    print(style("Vue / r", color=Style.GREEN))

    project_framework = answer()

    match (project_framework):

        case "q":

            project_framework = "vanilla_js"

        case "w": 

            project_framework = "react"

        case "r":

            project_framework = "vue"

    # React build
    if (project_framework == "react"):

        # Add libs
        question("Add react-router-dom? (y/n)")

        react_router_dom = answer()

        question("Add Sass? (y/n)")

        sass = answer()

        if (react_router_dom == "y"):
            
            react_router_dom = react_router_dom_version

        else:
            react_router_dom = ''


        if (sass == "y"):

            sass = sass_version
            
        else:
            sass = ''

        # Files for React project
        index_html = f"""<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{project_name}</title>
    </head>
    <body>
        <div id="root"></div>
        <script type="module" src="./App.jsx"></script>
    </body>
</html>"""

        vite_config = """import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
    plugins: [
        react()
    ],
})"""
        
        package_json = f"""{{
    "name": "{project_name}",
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
        "react-dom": "^18.2.0"{react_router_dom}
    }},
    "devDependencies": {{
        "@vitejs/plugin-react": "^4.0.0",
        "vite": "^4.4.0"{sass}
    }}
}}"""
        
        app_jsx = """import React from 'react'
import ReactDOM from 'react-dom/client'
import Main from './Main.jsx'

ReactDOM.createRoot(document.getElementById('root')).render(
    <React.StrictMode>
        <Main />
    </React.StrictMode>,
)"""

        main_jsx = f"""var Main = function () {{
return (
<>{project_name}</>
)
}}
export default Main"""
        
        main_jsx_router = f"""import {{ RouterProvider, createBrowserRouter }} from "react-router-dom";
var Main = function () {{

var routes = [
{{
    path: "/",
    element: <>{project_name}</>
}}    
]

var router = createBrowserRouter(routes)
return <RouterProvider router={{router}} />
}}
export default Main"""

        files = {
            "index.html": index_html,
            "vite.config.js": vite_config,
            "package.json": package_json,
            "App.jsx": app_jsx,
            "Main.jsx": main_jsx,
            ".gitignore": git_ignore
        }

        if (react_router_dom):

            files["Main.jsx"] = main_jsx_router

    # Vue build
    elif (project_framework == "vue"):

        # Add libs
        question("Add vue-router? (y/n)")

        vue_router = answer()

        question("Add Pinia? (y/n)")

        pinia = answer()

        question("Add Sass? (y/n)")

        sass = answer()

        if (vue_router == "y"):
            
            vue_router = vue_router_version

        else:
            vue_router = ''

        if (pinia == "y"):

            pinia = pinia_version
        
        else:
            pinia = ''

        if (sass == "y"):

            sass = sass_version

        else:
            sass = ''

        # Files for Vue project
        index_html = f"""<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{project_name}</title>
    </head>
    <body>
        <div id="root"></div>
        <script type="module" src="./App.js"></script>
    </body>
</html>"""
    
        vite_config = f"""import {{ defineConfig }} from 'vite'
import vue from '@vitejs/plugin-vue'
import vueDevTools from 'vite-plugin-vue-devtools'

export default defineConfig({{
    plugins: [
        vue(),
        vueDevTools(),
    ]
}})"""

        package_json = f"""{{
    "name": "{project_name}",
    "version": "0.0.0",
    "private": true,
    "type": "module",
    "scripts": {{
        "dev": "vite",
        "build": "vite build",
        "preview": "vite preview"
    }},
    "dependencies": {{
        "vue": "^3.5.27"{vue_router}{pinia}
    }},
    "devDependencies": {{
        "@vitejs/plugin-vue": "^6.0.3",
        "vite": "^7.3.1",
        "vite-plugin-vue-devtools": "^8.0.5"{sass}
    }},
    "engines": {{
        "node": "^20.19.0 || >=22.12.0"
    }}
}}"""

        app_js = f"""import {{ createApp }} from 'vue'
import Main from './Main.vue'
{"import router from './router.js'" if (vue_router) else ""}
{"import { createPinia } from 'pinia'" if (pinia) else ""}

createApp(Main){".use(router)" if (vue_router) else ""}{".use(createPinia())" if (pinia) else ""}.mount('#root')"""
        
        main_vue = f"""<script setup></script>

<template>{project_name}</template>

<style scoped></style>"""

        router_js = """import { createRouter, createWebHistory } from 'vue-router'

var router = createRouter({

    history: createWebHistory(import.meta.env.BASE_URL),
    routes: []
})
export default router
"""

        files = {
            "index.html": index_html,
            "vite.config.js": vite_config,
            "package.json": package_json,
            "App.js": app_js,
            "Main.vue": main_vue,
            ".gitignore": git_ignore
        }

        if (vue_router):

            files["router.js"] = router_js

    # Vanilla JS Build
    else:
        # Files for Vanilla JS build
        index_html = f"""<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{project_name}</title>
    </head>
    <body>
        <div id="root"></div>
        <script type="module" src="./App.js"></script>
    </body>
</html>"""

        package_json = f"""{{
    "name": "{project_name}",
    "private": true,
    "version": "0.0.0",
    "type": "module",
    "scripts": {{
        "dev": "vite",
        "build": "vite build",
        "preview": "vite preview"
    }},
    "devDependencies": {{
        "vite": "^7.3.1"
    }}
}}"""

        app_js = f"""var root = document.querySelector('#root')

root.innerHTML = '{project_name}'"""

        files = {
            "index.html": index_html,
            "package.json": package_json,
            "App.js": app_js,
            ".gitignore": git_ignore
        }

    build_files(files, project_path)
