import pytest
from playwright.sync_api import expect
from tests.polls.factories import QuestionFactory
from tests.polls.pages import PollsPage

@pytest.fixture()
def polls_page(page, live_server):
    return PollsPage(page, live_server)


def test_empty_polls_index_page(polls_page):
    polls_page.navigate()

    expect(polls_page.page.get_by_text('No polls are available.')).to_be_visible()


def test_polls_index_page_with_default_question(polls_page):
    q = QuestionFactory()

    polls_page.navigate()

    expect(polls_page.page.get_by_text(q.question_text)).to_be_visible()
