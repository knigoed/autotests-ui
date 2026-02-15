from components.base_component import BaseComponent
from playwright.sync_api import Page, expect
from typing import Literal


class ChartViewComponent(BaseComponent):
    TITLES = {
        "students": "Students",
        "activities": "Activities",
        "courses": "Courses",
        "scores": "Scores",
    }

    def __init__(self, page: Page,
                 identifier: Literal['students', 'activities', 'courses', 'scores'],
                 chart_type: Literal['bar', 'line', 'pie', 'scatter']):
        super().__init__(page)

        self.identifier = identifier

        self.title = page.get_by_test_id(f'{identifier}-widget-title-text')
        self.chart = page.get_by_test_id(f'{identifier}-{chart_type}-chart')

    def check_visible(self):
        expect(self.title).to_be_visible()
        expect(self.title).to_have_text(self.TITLES[self.identifier])
        expect(self.chart).to_be_visible()



