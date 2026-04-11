import pytest
from playwright.sync_api import Page

from data.Employee import Employee
from pages import pim
from pages.pim_page import PimPage


def test_add_employee_without_creds(page: Page, login_with_admin):
    pim = PimPage(page)
    add_employee_page = pim.visit_tab_add_employee()
    add_employee_page.add_employee_without_details()


@pytest.mark.parametrize("employee",
                         [Employee() for _ in range(1)]
                         )
def test_add_employee_with_differt_first_names(page: Page, login_with_admin, employee):
    pim = PimPage(page)
    add_employee_page = pim.visit_tab_add_employee()
    add_employee_page.add_employee_without_details(employee=employee)
