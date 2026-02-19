import os
from tools import *

def vue_build(component_name):

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
    print(style(f'"{component_name}" created!', color=Style.GREEN , bg=''))
