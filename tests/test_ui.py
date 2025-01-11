from playwright.sync_api import expect

def test_empty_polls_index_page(live_server, page):
    page.goto(live_server.url + "/polls")

    expect(page.get_by_text('No polls are available.')).to_be_visible()
