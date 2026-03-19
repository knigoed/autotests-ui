from playwright.sync_api import Page


def mock_static_recourses(page: Page):
    page.route("**/*.{ico,png,jpg,swg,web,mp3,mp4,woff,woff2}", lambda route: route.abort())

