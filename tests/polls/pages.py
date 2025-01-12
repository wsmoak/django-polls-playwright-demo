# https://playwright.dev/python/docs/pom
# Large test suites can be structured to optimize ease of authoring and maintenance.
# Page object models are one such approach to structure your test suite.

class PollsPage:
    def __init__(self, page, live_server):
        self.page = page
        self.live_server = live_server
        self.url = live_server.url + "/polls"

    def navigate(self):
        self.page.goto(self.url)
