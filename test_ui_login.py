import time
import subprocess
import pytest
import pyautogui
import pyperclip
import os
import win32gui
from pywinauto import Desktop

EXE_PATH = r"E:\y-ydj\ydjanzhuang\yindaojing\阴道镜.exe"
SCREENSHOT_DIR = r"E:\数据监控分析\ui_screenshots"
WIN_TITLE = "电子阴道镜成像系统"

CORRECT_USER = "admin"
CORRECT_PASS = "admin"

USERNAME_POS = (764, 348)
PASSWORD_POS = (740, 409)
LOGIN_BTN_POS = (783, 520)
SWITCH_USER_POS = (537, 72)
CONFIRM_POS = (805, 443)


def launch():
    subprocess.Popen([EXE_PATH])
    time.sleep(5)
    desktop = Desktop(backend="uia")
    win = desktop.window(title=WIN_TITLE)
    win.wait("visible", timeout=10)
    win32gui.MoveWindow(win.handle, 0, 0, 1280, 800, True)
    time.sleep(1)
    print("窗口已固定")


def close_app():
    os.system("taskkill /f /im 阴道镜.exe >nul 2>&1")
    time.sleep(2)


def paste_text(pos, text):
    pyautogui.click(pos)
    time.sleep(0.3)
    pyautogui.hotkey("ctrl", "a")
    time.sleep(0.2)
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl", "v")
    time.sleep(0.3)


def clear_field(pos):
    """清空输入框"""
    pyautogui.click(pos)
    time.sleep(0.3)
    pyautogui.hotkey("ctrl", "a")
    time.sleep(0.2)
    pyautogui.press("delete")
    time.sleep(0.2)


def clear_all_fields():
    """清空所有输入框"""
    clear_field(USERNAME_POS)
    clear_field(PASSWORD_POS)
    print("🧹 已清空所有输入框")


def login(user, pwd):
    clear_all_fields()
    paste_text(USERNAME_POS, user)
    paste_text(PASSWORD_POS, pwd)
    pyautogui.click(LOGIN_BTN_POS)
    time.sleep(3)


def logout():
    pyautogui.click(SWITCH_USER_POS)
    time.sleep(1)
    pyautogui.click(CONFIRM_POS)
    time.sleep(3)


def screenshot(name):
    path = os.path.join(SCREENSHOT_DIR, f"{name}.png")
    pyautogui.screenshot(path)
    print(f"📸 截图: {name}.png")


def test_login_success():
    """正确账号密码登录成功"""
    close_app()
    launch()
    login(CORRECT_USER, CORRECT_PASS)
    screenshot("01_login_success")
    print("✅ 正确账号密码登录成功")
    logout()


def test_login_wrong_password():
    """错误密码被拦截"""
    clear_all_fields()
    login(CORRECT_USER, "wrongpassword")
    screenshot("02_wrong_password")
    print("✅ 错误密码被拦截")


def test_login_empty_username():
    """空账号被拦截"""
    clear_all_fields()
    paste_text(PASSWORD_POS, CORRECT_PASS)
    pyautogui.click(LOGIN_BTN_POS)
    time.sleep(1)
    screenshot("03_empty_username")
    print("✅ 空账号被拦截")


def test_login_empty_password():
    """空密码被拦截"""
    clear_all_fields()
    paste_text(USERNAME_POS, CORRECT_USER)
    pyautogui.click(LOGIN_BTN_POS)
    time.sleep(1)
    screenshot("04_empty_password")
    print("✅ 空密码被拦截")


def test_login_both_empty():
    """账号密码均为空"""
    clear_all_fields()
    pyautogui.click(LOGIN_BTN_POS)
    time.sleep(1)
    screenshot("05_both_empty")
    print("✅ 账号密码均为空被拦截")


def test_login_wrong_username():
    """不存在账号被拦截"""
    clear_all_fields()
    login("notexist_user", CORRECT_PASS)
    screenshot("06_wrong_username")
    print("✅ 不存在账号被拦截")


def test_login_success_final():
    """最终正常登录验证"""
    clear_all_fields()
    login(CORRECT_USER, CORRECT_PASS)
    screenshot("07_final_success")
    print("✅ 最终登录成功")
    close_app()