import reflex as rx
from rxconfig import config
from reflex_github_badge.github_badge import github_badge


@rx.page(
    route="/", title="Github Card", description="Portafolio de widgets hechos en reflex"
)
def index() -> rx.Component:
    return rx.vstack(
        rx.color_mode.button(position="top-right"),
        rx.heading("Github Card", size="6"),
        github_badge(username="xsismadn3ss", description="Hello world 👋"),
        rx.heading("¿How to use?"),
        rx.card(
            rx.heading(
                "1- Write this command on your terminal to install this package",
                size="3",
            ),
            rx.markdown(
                r"""
                ```bash
                pip install reflex-github-badge
                ```
                """
            ),
            rx.heading("2- Import reflex-github-badge", size="3"),
            rx.markdown(
                r"""
                ```python
                from reflex_github_badge.github_badge import github_badge
                ```
                """
            ),
            rx.heading(
                "3- Enter your github username and set a description(optional)",
                size="3",
            ),
            rx.markdown(
                r"""
                ```python
                github_badge(username="hello", description="hello world")
                ```
                """
            ),
            size="2",
        ),
        width="100%",
        align="center",
        justify="center",
        margin_top="2rem",
        margin_x="1rem",
    )
