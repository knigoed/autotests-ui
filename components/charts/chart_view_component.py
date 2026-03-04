from components.base_component import BaseComponent
from playwright.sync_api import Page
from typing import Literal
from elements.text import Text
import allure


class ChartViewComponent(BaseComponent):
   def __init__(self,
                 page: Page,
                 identifier: Literal['students', 'activities', 'courses', 'scores'],
                 chart_type: Literal['bar', 'line', 'pie', 'scatter']):

        super().__init__(page)

        self.title = Text(page, f'{identifier}-widget-title-text', 'Title')
        self.chart = Text(page, f'{identifier}-{chart_type}-chart', 'Chart')

   @allure.step('Check visible chart view "{title}"')
   def check_visible(self, title: str):
        self.title.check_visible()
        self.title.check_have_text(title)

        self.chart.check_visible()



