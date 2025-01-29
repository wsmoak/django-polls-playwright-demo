import pytest
from playwright.sync_api import expect
from tests.polls.factories import QuestionFactory
from tests.polls.pages import PollsPage

@pytest.fixture()
def polls_page(page, live_server):
    return PollsPage(page, live_server)


# Test that the question added in the 0002_add_initial_data.py migration is visible on the index page
@pytest.mark.django_db(serialized_rollback=True)
def test_initial_polls_index_page_with_data_from_migration(polls_page):
    polls_page.navigate()

    expect(polls_page.page.get_by_text('What is your favorite holiday?')).to_be_visible()


# Show that serialized_rollback is working as expected to restore the database after each test
@pytest.mark.django_db(serialized_rollback=True)
def test_that_serialized_rollback_restores_migrated_data(polls_page):
    polls_page.navigate()

    expect(polls_page.page.get_by_text('What is your favorite holiday?')).to_be_visible()
