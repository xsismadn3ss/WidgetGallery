import reflex as rx


def instructions() -> rx.card:
    return rx.card(
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
                def GithubCard() -> rx.Component:
                    return github_badge(
                        username="hello", 
                        description="hello world"
                    )
                ```
                """
        ),
        size="2",
    )
