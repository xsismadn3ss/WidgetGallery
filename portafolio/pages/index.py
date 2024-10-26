import reflex as rx
from rxconfig import config
from .views.instructions import instructions
from .views.demo import demo


@rx.page(
    route="/", title="Github Card", description="Portafolio de widgets hechos en reflex"
)
def index() -> rx.Component:
    return rx.vstack(
        rx.color_mode.button(position="top-right"),
        rx.heading("Github Card", size="6"),
        demo(),
        rx.heading("¿How to use?"),
        instructions(),
        width="100%",
        align="center",
        justify="center",
        margin_top="2rem",
        margin_x="1rem",
    )
