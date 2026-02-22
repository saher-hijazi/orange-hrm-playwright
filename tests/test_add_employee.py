import re
from playwright.sync_api import Page, expect

def test_add_new_employee_flow(page: Page):
    # 1. الانتقال للموقع
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    
    # 2. تسجيل الدخول
    page.get_by_placeholder("Username").fill("Admin")
    page.get_by_placeholder("Password").fill("admin123")
    page.get_by_role("button", name="Login").click()
    
    # 3. تنفيذ خطوات الإضافة
    page.get_by_role("link", name="PIM").click()
    page.get_by_role("button", name="Add").click()
    
    # 4. تعبئة البيانات
    page.get_by_placeholder("First Name").fill("Saher")
    page.get_by_placeholder("Last Name").fill("Hijazi")
    page.get_by_role("button", name="Save").click()
    
    # 5. التأكد من النجاح
    expect(page.get_by_text("Saher Hijazi").first).to_be_visible(timeout=10000)