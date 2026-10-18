import pytest
from playwright.sync_api import Page, expect
from pages.todo_page import TodoPage


# 前提条件：TODO画面を開いた状態
@pytest.fixture
def todo(page: Page):
    todo_page = TodoPage(page)
    todo_page.open()
    return todo_page


# 見本：TODOを1件追加できる
def test_TODOを1件追加できる(todo):
    todo.add("牛乳を買う")
    expect(todo.titles).to_have_text(["牛乳を買う"])


# ケース1：2件追加すると2件表示される
def test_TODOを2件追加できる(todo):
    todo.add ("牛乳を買う")
    todo.add ("たまごを買う")
    expect(todo.titles).to_have_text(["牛乳を買う","たまごを買う"])

# ケース2：完了にできる
def test_TODOを完了にできる(todo):
    todo.add("牛乳を買う")
    todo.complete(0)
    expect(todo.checkbox(0)).to_be_checked()


# ケース3：削除できる
def test_TODOを削除できる(todo):
    todo.add("牛乳を買う")
    todo.delete(0)
    expect(todo.items).to_have_count(0)

# ケース4（異常系）：空のままEnterでは追加されない
def test_空のTODOは追加されない(todo):
    todo.add("")
    expect(todo.items).to_have_count(0)