# Alfred.py
import time
from Open_Whatsapp import open_wpp, search_wpp
from Read_and_save import get_messages, read_and_save_messages
import os

def main():
    open_wpp()
    search_wpp()
    wpp_window = search_wpp()
    get_messages(wpp_window)
    read_and_save_messages()


if __name__ == "__main__":
    main()

