import reflex as rx
from ..components.nabvar import navbar
from rxconfig import config

@rx.page(route='/', title='Inicio', description='Portafolio de widgets hechos en reflex')
def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.flex(
        navbar()
    )