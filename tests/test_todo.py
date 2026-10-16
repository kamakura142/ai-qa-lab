import pytest
from playwright.sync_api import Page, expect

URL = "https://demo.playwright.dev/todomvc/"


# 前提条件：TODOアプリを開いた状態（fixture）
@pytest.fixture
def todo_page(page: Page):
    page.goto(URL)
    return page


# 補助関数：TODOを1件追加する（何度も使うのでまとめる）
def add_todo(page, text):
    input_box = page.get_by_placeholder("What needs to be done?")
    input_box.fill(text)
    input_box.press("Enter")


# 既存：TODOを1件追加できる
def test_TODOを1件追加できる(todo_page):
    add_todo(todo_page, "牛乳を買う")
    expect(todo_page.get_by_test_id("todo-title")).to_have_text(["牛乳を買う"])


# ケース1：2件追加すると2件表示される
def test_TODOを2件追加できる(todo_page):
    add_todo(todo_page, "牛乳を買う")
    add_todo(todo_page, "たまごを買う")
    expect(todo_page.get_by_test_id("todo-item")).to_have_text(["牛乳を買う","たまごを買う"])


# ケース2：完了にできる
def test_TODOを完了にできる(todo_page):
    add_todo(todo_page, "牛乳を買う")
    checkbox = todo_page.get_by_test_id("todo-item").nth(0).get_by_role("checkbox")
    checkbox.check()
    expect(checkbox).to_be_checked()


# ケース3：削除できる
def test_TODOを削除できる(todo_page):
    add_todo(todo_page, "牛乳を買う")
    item = todo_page.get_by_test_id("todo-item").nth(0)
    item.hover()
    item.locator(".destroy").click()
    expect(todo_page.get_by_test_id("todo-item")).to_have_count(0)


# ケース4（異常系）：空のままEnterでは追加されない
def test_空のTODOは追加されない(todo_page):
    add_todo(todo_page, "")
    expect(todo_page.get_by_test_id("todo-item")).to_have_count(0)