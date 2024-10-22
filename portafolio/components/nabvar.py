import reflex as rx

def navbar():
    return rx.flex(
        rx.flex(
            rx.icon('square-terminal', size=30, stroke_width=2),
            rx.heading("Widget Gallery", size='7')
        ),
        rx.flex(
            rx.link('Inicio'),
            rx.link('Galeria'),
            rx.link('Contacto'),
            rx.link('Más'),
        ),
        width="100%",
        bg='#f3f3f3'
    )