from playwright.sync_api import Page, expect


# TODOを1件追加すると、一覧に表示される
def test_TODOを1件追加できる(page: Page):
    # 手順1：TODOアプリを開く
    page.goto("https://demo.playwright.dev/todomvc/")

    # 手順2：入力欄に「牛乳を買う」と入力して、Enter
    input_box = page.get_by_placeholder("What needs to be done?")
    input_box.fill("牛乳を買う")
    input_box.press("Enter")

    # 期待結果：一覧に「牛乳を買う」が表示されている
    expect(page.get_by_test_id("todo-title")).to_have_text(["牛乳を買う"])