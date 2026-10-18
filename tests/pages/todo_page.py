from playwright.sync_api import Page


class TodoPage:
    """TODO画面のページオブジェクト：画面の部品と操作をまとめる"""

    URL = "https://demo.playwright.dev/todomvc/"

    def __init__(self, page: Page):
        # 画面の部品（ここだけ直せば、全テストに反映される）
        self.page = page
        self.input_box = page.get_by_placeholder("What needs to be done?")
        self.items = page.get_by_test_id("todo-item")
        self.titles = page.get_by_test_id("todo-title")

    # 操作：画面を開く
    def open(self):
        self.page.goto(self.URL)

    # 操作：TODOを1件追加する
    def add(self, text):
        self.input_box.fill(text)
        self.input_box.press("Enter")

    # 操作：指定した番号のTODOを完了にする（0から数える）
    def complete(self, index):
        self.items.nth(index).get_by_role("checkbox").check()

    # 部品：指定した番号のTODOのチェックボックス
    def checkbox(self, index):
        return self.items.nth(index).get_by_role("checkbox")

    # 操作：指定した番号のTODOを削除する
    def delete(self, index):
        item = self.items.nth(index)
        item.hover()
        item.locator(".destroy").click()