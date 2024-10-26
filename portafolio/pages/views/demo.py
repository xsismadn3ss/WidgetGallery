import reflex as rx
from reflex_github_badge.github_badge import github_badge


def card():
    return github_badge(username="xsismadn3ss", description="Hello world 👋")


def links(width="auto", height="max-content"):
    return rx.card(
        rx.tablet_only(
            rx.inset(
                rx.avatar(
                    fallback="🔗🔗🔗🔗🔗🔗🔗🔗",
                    width="100%",
                    font_zise="large",
                    size="7",
                    radius="none",
                    color_scheme="purple",
                ),
                side="top",
                pb="1rem",
            ),
        ),
        rx.vstack(
            rx.flex(
                rx.icon("link", color="gray"),
                rx.heading("Links", size="5"),
                spacing="1",
            ),
            rx.flex(
                rx.icon("box", color="#4b6f8c"),
                rx.link(
                    rx.text("Read more about in Pypi"),
                    href="https://pypi.org/project/reflex-github-badge/",
                    color_scheme="gray",
                ),
                spacing="1",
            ),
            rx.flex(
                rx.icon("github", color="#4b6f8c"),
                rx.link(
                    rx.text("Source code"),
                    href="https://github.com/xsismadn3ss/Github_badge_component",
                    color_scheme="gray",
                ),
                spacing="1",
            ),
            margin_top="0.5rem",
            justify="center",
            height="auto",
        ),
    )


def demo():
    return (
        rx.tablet_and_desktop(rx.flex(card(), links(), spacing="3")),
        rx.mobile_only(rx.flex(card(), links(), spacing="3", direction="column")),
    )
