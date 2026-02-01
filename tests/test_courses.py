import pytest
from playwright.sync_api import expect, Page


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state: Page):
    page = chromium_page_with_state
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    course_header = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
    expect(course_header).to_be_visible()
    expect(course_header).to_have_text('Courses')

    there_is_no_results_header = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
    expect(there_is_no_results_header).to_be_visible()
    expect(there_is_no_results_header).to_have_text('There is no results')

    empty_block_icon = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
    expect(empty_block_icon).to_be_visible()

    results_will_be_displayed_here_header = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
    expect(results_will_be_displayed_here_header).to_be_visible()
    expect(results_will_be_displayed_here_header).to_have_text(
        'Results from the load test pipeline will be displayed here')

