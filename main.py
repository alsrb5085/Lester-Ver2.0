import sys
import time
import pynput
from threading import Thread
from win32gui import FindWindow, GetWindowRect
from hacks import casinofingerprint, casinokeypad, cayofingerprint, cayovoltage

try:
    from ctypes import windll
    windll.user32.SetProcessDPIAware()
except:
    pass

def print_banner():
    print('''
██╗░░░░░███████╗░██████╗████████╗███████╗██████╗░  ██╗░░░██╗███████╗██████╗░  ██████╗░░░░░█████╗░
██║░░░░░██╔════╝██╔════╝╚══██╔══╝██╔════╝██╔══██╗  ██║░░░██║██╔════╝██╔══██╗  ╚════██╗░░░██╔══██╗
██║░░░░░█████╗░░╚█████╗░░░░██║░░░█████╗░░██████╔╝  ╚██╗░██╔╝█████╗░░██████╔╝  ░░███╔═╝░░░██║░░██║
██║░░░░░██╔══╝░░░╚═══██╗░░░██║░░░██╔══╝░░██╔══██╗  ░╚████╔╝░██╔══╝░░██╔══██╗  ██╔══╝░░░░░██║░░██║
███████╗███████╗██████╔╝░░░██║░░░███████╗██║░░██║  ░░╚██╔╝░░███████╗██║░░██║  ███████╗██╗╚█████╔╝
╚══════╝╚══════╝╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝  ░░░╚═╝░░░╚══════╝╚═╝░░╚═╝  ╚══════╝╚═╝░╚════╝░
                                                                                          ''')

def print_credits():
    print('''
Made by JUSTDIE
Special thanks to RedHeadEmile
    ''')
    
def check_window():
    print('[*] Searching Grand Theft Auto V...')

    while True:
        hwnd = FindWindow(None, "Grand Theft Auto V")
        
        if hwnd:
            print('[*] Grand Theft Auto V Detected!')
            print('')
            print('=============================================')
            return GetWindowRect(hwnd)
        
        time.sleep(1)

def casino_fingerprint(bbox):
    thread = Thread(target=casinofingerprint.main, args=(bbox,))
    thread.start()

def casino_keypad(bbox):
    thread = Thread(target=casinokeypad.main, args=(bbox,))
    thread.start()

def cayo_fingerprint(bbox):
    thread = Thread(target=cayofingerprint.main, args=(bbox,))
    thread.start()

def cayo_voltage(bbox):
    thread = Thread(target=cayovoltage.main, args=(bbox,))
    thread.start()

def shutdown():
    sys.exit()

def main():
    print_banner()
    print_credits()

    # DPI 설정이 적용되지 않은 전체 창 bbox를 가져옵니다.
    full_bbox = check_window()
    if full_bbox:
        # 21:9 모니터의 전체 화면 크기를 기반으로 16:9 게임 화면의 bbox를 계산합니다.
        width = full_bbox[2] - full_bbox[0]
        height = full_bbox[3] - full_bbox[1]
        
        game_width = int(height * (16 / 9))
        black_bar_width = (width - game_width) // 2
        
        game_bbox = (full_bbox[0] + black_bar_width, full_bbox[1], full_bbox[2] - black_bar_width, full_bbox[3])
        
        print(f"[*] Full window bbox: {full_bbox}")
        print(f"[*] Calculated 16:9 game bbox: {game_bbox}")

        with pynput.keyboard.GlobalHotKeys({
                '<F4>': shutdown,
                '<F5>': lambda: casino_fingerprint(game_bbox),
                '<F6>': lambda: casino_keypad(game_bbox),
                '<F7>': lambda: cayo_fingerprint(game_bbox),
                '<F8>': lambda: cayo_voltage(game_bbox)}) as h:
            h.join()

if __name__ == "__main__":
    main()