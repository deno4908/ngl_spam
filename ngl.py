import requests
import uuid
import threading
import time
import random,re,shutil,os
class Color():
    BLACK = "\033[0;30m"
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    BROWN = "\033[0;33m"
    BLUE = "\033[0;34m"
    PURPLE = "\033[0;35m"
    CYAN = "\033[0;36m"
    LIGHT_GRAY = "\033[0;37m"
    DARK_GRAY = "\033[1;30m"
    LIGHT_RED = "\033[1;31m"
    LIGHT_GREEN = "\033[1;32m"
    YELLOW = "\033[1;33m"
    LIGHT_BLUE = "\033[1;34m"
    LIGHT_PURPLE = "\033[1;35m"
    LIGHT_CYAN = "\033[1;36m"
    LIGHT_WHITE = "\033[1;37m"
    BOLD = "\033[1m"
    FAINT = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    NEGATIVE = "\033[7m"
    CROSSED = "\033[9m"
    END = "\033[0m"
def ascii_img_boxed():
    def strip_ansi(text):
        return re.sub(r'\x1b\[[0-9;]*m', '', text)
    content = [
            "███╗░░██╗░██████╗░██╗░░░░░",
            "████╗░██║██╔════╝░██║░░░░░",
            "██╔██╗██║██║░░██╗░██║░░░░░",
            "██║╚████║██║░░╚██╗██║░░░░░",
            "██║░╚███║╚██████╔╝███████╗",
            "╚═╝░░╚══╝░╚═════╝░╚══════╝",
        Color.CYAN + "[*-*]" + Color.END + " => " + Color.RED + "YOUTUBE" + Color.END + " : " + Color.LIGHT_WHITE + "https://www.youtube.com/@wne9838" + Color.END,
        Color.CYAN + "[*-*]" + Color.END + " => " + Color.BLUE + "FB" + Color.END + " : " + Color.LIGHT_WHITE + "https://www.facebook.com/accngunghoatdongreal0" + Color.END
    ]
    max_len = max(len(strip_ansi(line)) for line in content)
    print("╔" + "═" * (max_len + 2) + "╗")
    for line in content:
        real_len = len(strip_ansi(line))
        padding = max_len - real_len
        print("║ " + line + " " * padding + " ║")
    print("╚" + "═" * (max_len + 2) + "╝")
def input_text(text1):
    return input(f"{Color.RED}[{Color.END}＄{Color.RED}]{Color.END} {Color.GREEN} ➤ {text1}: {Color.END}")
def draw_full_width_box(text):
    terminal_width = shutil.get_terminal_size().columns
    text_with_color = Color.YELLOW + text + Color.GREEN
    padding_total = terminal_width - 2 - len(text)
    padding_left = padding_total // 2
    padding_right = padding_total - padding_left
    print(Color.GREEN + "┌" + "─" * (terminal_width - 2) + "┐")
    print("│" + " " * padding_left + text_with_color + " " * padding_right + "│")
    print("└" + "─" * (terminal_width - 2) + "┘" + Color.END)
stop_event = threading.Event()

USER_AGENTS = [
    "Mozilla/5.0 (Linux; Android 9; Infinix X604) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; PIC-LX9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.1.1; ASUS_X00ID) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.96 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.1.1; ZC520KL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; FLA-LX1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.96 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-G965U1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.141 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 12; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.131 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.60 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Safari/605.1.15",
]

def spam(message, target):
    while not stop_event.is_set():
        headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9,vi-VN;q=0.8,vi;q=0.7',
            'cache-control': 'no-cache',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'dnt': '1',
            'origin': 'https://ngl.link',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': f'https://ngl.link/{target}',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'x-requested-with': 'XMLHttpRequest',
            'user-agent': random.choice(USER_AGENTS), 
        }

        data = {
            'username': str(target),
            'question': str(message),
            'deviceId': str(uuid.uuid4()),
            'gameSlug': '',
            'referrer': '',
        }

        try:
            r = requests.post(
                url="https://ngl.link/api/submit",
                data=data,
                headers=headers,
                timeout=10
            )
            if r.status_code == 200:
                print(f"Đã spam {r.status_code} với UA: {headers['user-agent']}")
            elif r.status_code == 429:
                print("Bị Limit, chờ 20s...")
                time.sleep(20)
        except Exception as e:
            print("Lỗi:", e)

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    ascii_img_boxed()
    try:
        username = input_text("Nhập Tên Target")
        message = input_text("Nhập Tên Message")
        while True:
            try:
                threads = int(input_text("Nhập số luồng"))
                break
            except:
                pass
        draw_full_width_box("Đang AUTO")
        for i in range(threads):
            t = threading.Thread(target=spam, args=(message, username), daemon=True)
            t.start()
        while True:
            time.sleep(0.1)

    except KeyboardInterrupt:
        print("\nThoát bằng Ctrl+C")
        stop_event.set()
        time.sleep(1) 

if __name__ == "__main__":
    main()
