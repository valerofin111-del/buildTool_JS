import os
from tools import *

def vue_build(component_name : str):

    component_name = component_name.strip().capitalize()

    component_path = os.getcwd()

    component = f"""<script setup lang="js">

</script>

<template>
    <div class="{component_name}"> 
        {component_name}
    </div>
</template>

<style scoped>
    .{component_name} {{
        color: green;
    }}
</style>"""

    files = {
        f'{component_name}.vue': component
    }

    build_files(files, component_path)
    print(style(f'"{component_name}" created at {component_path}/{component_name}.vue', color=Style.GREEN , bg=''))
