from tools import *

def mvc_build(mvc_name : str):

    route_name = mvc_name + 'Route'
    controller_name = mvc_name + 'Controller'

    print(style(f'"{mvc_name}" created!', color=Style.CYAN , bg=''))
