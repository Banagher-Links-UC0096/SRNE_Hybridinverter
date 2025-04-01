import tkinter as tk
import serial.tools.list_ports

def p_select(n_name, p_list):  # p_list: 除外するポートリスト
    selected_port = None  # 選択されたポートを保持する変数

    def select_port():
        nonlocal selected_port
        selected_indices = listbox.curselection()
        if selected_indices:
            selected_port = listbox.get(selected_indices[0]).split(" - ")[0]
            root.destroy()  # ウィンドウを閉じる
        else:
            print("ポートを選択してください！")

    # Tkinterウィンドウの設定
    root = tk.Tk()
    root.title(n_name + " : USBポート選択")
    root.geometry("350x200+500+300")

    # USBポートのリストを取得
    ports = serial.tools.list_ports.comports()
    port_list = [f"{port.device} - {port.description}" for port in ports]

    # 除外するポートをフィルタリング
    port_list = [port for port in port_list if port.split(" - ")[0] not in p_list]

    # リストボックスの作成
    listbox = tk.Listbox(root, selectmode=tk.SINGLE, height=7, width=50)
    for item in port_list:
        listbox.insert(tk.END, item)

    listbox.pack(pady=20)

    # 選択ボタンを作成
    select_button = tk.Button(root, text="ポートを選択", command=select_port)
    select_button.pack(pady=10)

    # メインループ
    root.mainloop()

    return selected_port

# ----------データ変換    
def ffff(rdd):return rdd - 65536 if rdd > 32767 else rdd  # 16bit負変換  

def ffffx2(high_16bit, low_16bit): # 32bit負変換
    # 16ビットの上位データを符号付きに変換（符号拡張）
    if high_16bit & 0x8000:  # 符号ビットが1なら負数
        high_16bit -= 0x10000
    # 上位16ビットを左にシフトし、下位16ビットを結合
    combined_32bit = (high_16bit << 16) | (low_16bit & 0xFFFF)
    return combined_32bit

def change_type(d_type, rdd, sys_volt, byte, n_data): # データタイプ変換
    if d_type < 4:  # 1/10, 1/100, 1/1000 判定
        if byte == 1:rdd = ffff(rdd)
        d = rdd / (10 ** d_type)
    elif d_type == 4:d = (rdd / 10) * (2 if sys_volt == 24 else 4 if sys_volt == 48 else 1)  # 電圧データ判定 24V/48V
    elif d_type == 5:d = chr(rdd)  # 文字データ判定
    elif d_type == 6:d = "Off" if rdd else "On"  # ON/OFF 判定
    elif d_type == 7:  # 時刻判定
        ym = f"{hex(rdd)[2:].zfill(4)}"
        d = f"{int(ym[:2], 16):02}:{int(ym[2:], 16):02}"
    elif d_type == 8:
        d = n_data[rdd + 11]  # 拡張判定
    elif d_type == 9:  # デバッグ用
        print(rdd)
        d = None
    else:d = None
    return str(d) if d_type < 5 else d