import win32api, win32con
import time


def click():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def double_click():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def move(x, y):
    win32api.SetCursorPos((x, y))


def move_from(fx, fy, tx, ty):
    dx = tx - fx
    dy = ty - fy
    moves = 50
    hx = float(dx) / moves
    hy = float(dy) / moves
    for i in range(moves):
        move(fx + int(i * hx), fy + int(i * hy))
        delay(0.001)


def move_click(x, y, d=0.01):
    move(x, y)
    delay(d)
    click()


def delay(d=0.01):
    time.sleep(d)
