import os
from tools import *

def jsx_build(component_name):

    component_name = component_name.strip().capitalize()

    component_path = os.path.join(os.getcwd(), component_name)
    os.makedirs(component_path, exist_ok=True)

    styles = f""".{component_name} {{
        color: blue;
}}"""

    component = f"""import styles from './{component_name}.css'

var {component_name} = () => {{
    return (
        <div className={{styles.{component_name}}} >
            {component_name}
        </div>
    )
}};
export default {component_name};"""

    files = {
        f'{component_name}.jsx': component,
        f'{component_name}.css': styles
    }

    build_files(files, component_path)
    success(component_name = component_name)
