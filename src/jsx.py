import os
from tools import *

def jsx_build(component_name : str):

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
    print(style(f'"{component_name}" created at {component_path}/{component_name}.jsx', color=Style.BLUE , bg=''))
