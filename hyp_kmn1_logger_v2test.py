# HYP4850U100-H_parallel_KM-N1_Logger
# ----------初期設定
from pymodbus.client import ModbusSerialClient as Mod # Modbus組込
import serial # シリアル通信組込
import csv # CSVファイルモジュール組込
import datetime as dt # 時計モジュール組込
from time import sleep # タイマー組込
import tkinter as tk # GUIモジュール組込
import threading # スレッド組込
import concurrent.futures
import os
# オリジナルファイル組込
import SRNE_command as SRNE
import KMN1_command as KM
import commandlib as cmd
#import dessdata_chart as chart

interval1=0 # 待ち時間（秒）+10秒
# ----------Modbusデータ辞書読込
# [0:address,1:byte,2:x,3:y,4:type,5:name,6:unit,7:len,8:min,9:max,10:set,11:data...]
r_data=SRNE.read_command
w_data=SRNE.write_command
k_data=KM.read_command

# ----------オリジナルデータパラメーター
# [0:name,1:x,2:y,3:no,4:type,5:unit]
v_data=[["蓄電池総合電流",5,20,1,1,"A"],["蓄電池総合電力",5,21,2,1,"W"],
        ["PV発電総合電力",5,22,3,3,"W"],["AC入力総合電力",5,23,4,3,"VA"],
        ["AC出力総合電力",5,24,5,3,"W"],["損失電力",5,25,6,0,"W"],
         
        ["総合充電量",5,27,7,0,"Ah"],["総合放電量",5,28,8,0,"Ah"],
        ["総合発電量",5,29,9,1,"kWh"],["総合消費量",5,30,10,1,"kWh"],
        ["総合商用充電量",5,31,11,0,"Ah"],["総合商用消費量",5,32,12,1,"kWh"]]
# ----------表示項目データパラメーター
# [0:name,1:x,2:y,3:size]
t_data=[["日時",4,0,4],["L1側",1,1,1],["L2側",3,1,1],["L1側",6,1,1],
        ["L2側",8,1,1],["AC入力側",0,1,0],["AC出力側",0,6,0],
        ["総合データ",5,19,0],["蓄電池側",0,14,0],["PV入力側",0,21,0],
        ["内部システム",0,26,0],["当日積算データ",5,1,0],
        ["累積積算データ",5,10,0],["KM-N1データ",0,35,0],["入力側",1,35,1],
        ["出力側",3,35,1],["入力側",6,35,1],["出力側",8,35,1],
        ["充電電力",8,21,1],["VA",9,22,4],["VA",9,23,4],["効率",8,24,3],["%",9,25,4]]
# ----------SRNEデータパラメーター
h_data=[[0x010b,[1],[2]],[0x0100,[53],[54]],#'Battery_soc'
        [0x0101,[524],[525]],[0x0102,[10],[11]],[0x010e,[241],[242]],
        [0x0107,[0],[0]],#'PV_panel_voltage'
        [0x0108,[14],[15]],[0x0109,[241],[242]],[0x0224,[4],[5]],
        [0x0210,[5],[5]],#'Machine_state'
        [0x0216,[999],[1000]],[0x0217,[23],[24]],[0x0218,[5999],[6000]],[0x0219,[25],[25]],
        [0x021b,[0],[0]],#'Load_active_power'
        [0x021c,[761],[762]],[0x021f,[5],[6]],[0x0225,[20],[21]],
        [0x0212,[3930],[3931]],[0x0213,[0],[0]],#'Grid_voltage'
        [0x0214,[0],[0]],#'Grid_current'
        [0x0215,[0],[6001]],[0x021e,[0],[30]],
        [0x0220,[410],[411]],[0x0221,[404],[405]],[0x0222,[537],[538]],[0x0223,[549],[560]],
        [0xf02d,[28],[29]],[0xf02e,[11],[12]],[0xf02f,[17],[18]],[0xf030,[16],[17]],
        [0xf03c,[30],[31]],[0xf03d,[16],[17]],[0xf03e,[6],[7]],[0xf03f,[0],[0]],
        [0xf034,[4079,0],[4080,0]],[0xf036,[2488,0],[2499,0]],[0xf038,[3061,0],[3090,0]],[0xf03a,[2022,0],[2080,0]],
        [0xf046,[991,0],[1000,0]],[0xf048,[825,0],[900,0]],[0xf04a,[752],[753]],[0xf04b,[83],[84]],

        [0xe004,[6],[6]],[0xe20f,[2],[2]],[0xe002,[100],[100]],[0xe005,[150],[150]],
        [0xe006,[144],[144]],[0xe009,[142],[142]],[0xe01c,[20],[20]],[0xe008,[142],[142]],
        [0xe20a,[600],[600]],[0xe012,[120],[120]],[0xe022,[144],[144]],[0xe00a,[139],[139]],
        [0xe00b,[128],[128]],[0xe00c,[124],[124]],[0xe01b,[123],[123]],[0xe00d,[120],[120]],
        [0xe010,[55],[55]],[0xe00e,[116],[116]],[0xe206,[0],[0]],[0xe007,[142],[142]],
        [0xe011,[5],[5]],[0xe023,[10],[10]],[0xe013,[5],[5]],[0xdf0d,[0],[0]],
        [0xe215,[1],[1]],[0xe21b,[7],[7]],[0xe025,[0],[0]],[0xe01e,[11],[11]],
        [0xe00f,[5],[5]],[0xe01d,[100],[100]],[0xe01f,[0],[0]],[0xe020,[5],[5]],
        [0xe11f,[500],[500]],[0xe001,[800],[800]],[0xe120,[1000],[1000]],[0xe204,[2],[2]],
        [0xe209,[6000],[6000]],[0xe208,[1000],[1000]],[0xe129,[420],[420]],[0xe118,[50],[50]],
        [0xe20b,[1],[1]],[0xe201,[2],[4]],[0xe205,[300],[300]],[0xe037,[2],[2]],
        [0xe20c,[1],[1]],[0xe212,[0],[0]],[0xe200,[1],[2]],[0xe214,[0],[0]],
        [0xe207,[25],[25]],[0xe038,[0],[0]],[0xe213,[1],[1]],[0xe210,[0],[0]],
        [0xe211,[0],[0]],[0xe20d,[1],[1]],[0xe20e,[0],[0]],
        [0xe026,[5889],[5889]],[0xe027,[1595],[1595]],[0xe028,[0],[0]],[0xe029,[0],[0]],
        [0xe02a,[0],[0]],[0xe02b,[0],[0]],[0xe02c,[1],[1]],
        [0xe02d,[1792],[1792]],[0xe02e,[5889],[5889]],[0xe02f,[0],[0]],[0xe030,[0],[0]],
        [0xe031,[0],[0]],[0xe032,[0],[0]],[0xe033,[0],[0]],
        
        [0xdf00,[1],[0]]]
# ----------KM-N1データパラメーター
i_data=[[0x0000,[0,995],[0,986]],[0x0002,[0,1023],[0,1015]],[0x0004,[0,2034],[0,2021]],
        [0x0006,[0,2611],[0,5943]],[0x0008,[0,7803],[0,3466]],[0x000a,[0,5480],[0,3208]],
        [0x000c,[0,95],[0,93]],[0x000e,[0,600],[0,600]],[0x0010,[0,9831],[0,0]],
        [0x0012,[0xffff,0xffff],[0,8552]],
        [0x0200,[0,222],[0,0]],[0x0202,[0,6666],[0,0]],[0x0204,[0,99999],[0,0]],
        [0x0206,[0,333],[0,0]],[0x0208,[0,7777],[0,0]],
        [0x0220,[0,444],[0,0]],[0x0222,[0,8888],[0,0]],[0x0224,[0,99999],[0,0]],
        [0x0226,[0,555],[0,0]],[0x0228,[0xffff,0xffff],[0,0]]]
# ----------Modbus接続設定
p_list=[]
m_list=["ハイブリッドインバーターID1","ハイブリッドインバーターID2","KM-N1"]
p_list = [cmd.p_select(n_name=name, p_list=p_list) for name in m_list]
print(p_list)
client1=Mod(port=p_list[0],framer="rtu",baudrate=9600,bytesize=8,parity='N',stopbits=1,timeout=50) # Hybrid1
client2=Mod(port=p_list[1],framer="rtu",baudrate=9600,bytesize=8,parity='N',stopbits=1,timeout=50) # Hyblid2
client3=Mod(port=p_list[2],framer="rtu",baudrate=9600,bytesize=8,parity='N',stopbits=2,timeout=50) # KM-N1

# -----------DataLogger
def logger():
    port3 = serial.Serial('COM13', baudrate=9600, bytesize=8, parity='N', stopbits=1, timeout=50)  # USBポート3
    port4 = serial.Serial('COM14', baudrate=9600, bytesize=8, parity='N', stopbits=1, timeout=50)  # USBポート4
    # データ保存用リスト
    data_from3 = []
    data_from4 = []
    def handle_port3():
        while True:
            if port3.in_waiting:
                received3 = port3.read(port3.in_waiting)
                port4.write(received3)
    def handle_port4():
        while True:
            if port4.in_waiting:
                received4 = port4.read(port4.in_waiting)
                port3.write(received4)
    # スレッド作成
    thread3 = threading.Thread(target=handle_port3, daemon=True)
    thread4 = threading.Thread(target=handle_port4, daemon=True)
    # スレッド開始
    thread3.start()
    thread4.start()

    print("通信がバックグラウンドで動作中。他のタスクを実行できます。")

    try:
        while True:
            # 他の処理（例: メインスレッドでGUIを動作させたりする）
            pass
    except KeyboardInterrupt:
        print("プログラム終了")

    # 保存されたデータを表示
    print("Data received from Port B (Binary):", data_from3)
    print("Data received from Port C (Binary):", data_from4)

    # ポートを閉じる
    port3.close()
    port4.close()
    return

# ----------Modbusデータ取得
port_lock = threading.Lock() # Create a global lock object

def process_client1(hy_add, hy_count, label, test_func, err):  # Hybrid1 processing function
    try:
        with port_lock:  # Ensure exclusive access to the port
            if client1.connect():
                read_data1 = client1.read_holding_registers(
                    address=hy_add, count=hy_count, slave=1)
                if read_data1.isError():
                    err.append(f"{label} read1 error: {hex(hy_add)}")
                    read_data1 = [0] * hy_count
                else:
                    read_data1 = read_data1.registers
            else:
                err.append(f"{label} No connect.")
                read_data1 = test_func(hy_add, hy_count, 1)
    except Exception as e:
        err.append(str(e))
        read_data1 = [0] * hy_count
    finally:
        with port_lock:  # Ensure safe disconnection
            client1.close()
    return {label: {"data1": read_data1, "errors": err}}
def process_client2(hy_add, hy_count, label, test_func, err):  # Hybrid2 processing function
    try:
        with port_lock:
            if client2.connect():
                read_data2 = client2.read_holding_registers(
                    address=hy_add, count=hy_count, slave=2)
                if read_data2.isError():
                    err.append(f"{label} read2 error: {hex(hy_add)}")
                    read_data2 = [0] * hy_count
                else:
                    read_data2 = read_data2.registers
            else:
                err.append(f"{label} No connect.")
                read_data2 = test_func(hy_add, hy_count, 2)
    except Exception as e:
        err.append(str(e))
        read_data2 = [0] * hy_count
    finally:
        with port_lock:
            client2.close()
    return {label: {"data2": read_data2, "errors": err}}
def process_client3(km_add, km_count, label, test_func, err):  # KM-N1 processing function
    try:
        with port_lock:
            if client3.connect():
                read_data3 = client3.read_holding_registers(
                    address=km_add, count=km_count, slave=1)
                read_data4 = client3.read_holding_registers(
                    address=km_add, count=km_count, slave=2)
                if read_data3.isError():
                    err.append(f"{label} read3 error: {hex(km_add)}")
                    read_data3 = [0] * km_count
                else:
                    read_data3 = read_data3.registers
                if read_data4.isError():
                    err.append(f"{label} read4 error: {hex(km_add)}")
                    read_data4 = [0] * km_count
                else:
                    read_data4 = read_data4.registers
            else:
                err.append(f"{label} No connect.")
                read_data3, read_data4 = test_func(km_add, km_count)
    except Exception as e:
        err.append(str(e))
        read_data3, read_data4 = [0] * km_count, [0] * km_count
    finally:
        with port_lock:
            client3.close()
    return {label: {"data3": read_data3, "data4": read_data4, "errors": err}}
def hy_test(hy_add, hy_count, slave):  # Hybrid未接続処理
    special_cases = {0xe003: ([48], [48]),0x0035: ([50] * 24, [51] * 24)}
    read_data1, read_data2 = special_cases.get(hy_add, next(
        ((item[1], item[2]) for item in h_data if item[0] == hy_add), ([0], [0])))
    return (read_data1 if slave == 1 else read_data2) * hy_count
def km_test(km_add, km_count): # KM-N1未接続を処理する関数
    read_data3, read_data4 = next(
        ((item[1], item[2]) for item in i_data if item[0] == km_add), ([0], [0]))
    return read_data3*km_count,read_data4* km_count
def modbus_read(hy_add, hy_count, km_add, km_count):  # 並列実行
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # 各クライアント処理をスケジュール
        futures = [
            executor.submit(process_client1, hy_add, hy_count, "Hybrid1", hy_test, []),
            executor.submit(process_client2, hy_add, hy_count, "Hybrid2", hy_test, []),
            executor.submit(process_client3, km_add, km_count, "KM-N1", km_test, [])
        ]
        results = [future.result() for future in concurrent.futures.as_completed(futures)]

    # データ格納辞書とエラーセット
    m_data = {key: None for key in ["data1", "data2", "data3", "data4"]}
    error_list = {error for result in results for key in result if "errors" in result[key]
                  for error in result[key]["errors"]}

    # データを辞書に更新
    for key, data_keys in [("Hybrid1", ["data1"]), 
                           ("Hybrid2", ["data2"]), 
                           ("KM-N1", ["data3", "data4"])]:
        for result in results:
            if key in result:
                m_data.update({dk: result[key].get(dk) for dk in data_keys})

    # エラーメッセージの結合
    err = "\n".join(f"- {error}" for error in sorted(error_list)) if error_list else "\nNo errors encountered."

    return m_data["data1"], m_data["data2"], m_data["data3"], m_data["data4"], err

def modbus_write(add,d_list,slave):  # Modbus write
    err=[]
    try:
        with port_lock:  # Ensure exclusive access to the port
            if client1.connect():
                writers=client1.write_registers(
                    address=add, values=d_list, slave=slave)
                if writers.isError():
                    err.append(f"write1 error: {hex(add)}")
            else:
                err.append(f"write1 No connect.")
    except Exception as e:
        err.append(str(e))
    finally:
        with port_lock:  # Ensure safe disconnection
            client1.close()
    return 
def inv_on(st): # インバータ―起動
            onoff1, onoff2,a,b,c = modbus_read(0xdf00, 1, 0, 1)
            
            if onoff1[0] == 0:
                modbus_write(0xdf00, [1], 1)  # ハイブリッドインバーター1起動開始
                st1 = f"{st}ID1{'起動失敗' if modbus_read(0xdf00, 1, 0, 1)[0][0] == 0 else '起動'}"
            else:st1 = f"{st}ID1運転中"
            if onoff2[0] == 0:
                modbus_write(0xdf00, [1], 2)  # ハイブリッドインバーター2起動開始
                st2 = f"{st}ID2{'起動失敗' if modbus_read(0xdf00, 1, 0, 1)[1][0] == 0 else '起動'}"
            else:st2 = f"{st}ID2運転中"
            st_text=f"{st1}\n{st2}"
            return st_text

# ----------データ変換    
def data_read(): # データ処理
    dt_now=dt.datetime.now().strftime('%y/%m/%d %H:%M:%S')                              # 日時を取得
    date_time=dt_now
    r_list=len(r_data)
    hywd1,hywd2,hyrd1,hyrd2,o_data,kmwd1,kmwd2,kmrd1,kmrd2,err=[],[],[],[],[],[],[],[],[],[]
    r_list=len(r_data)
    # データ処理関数
    def process_data(byte, d_type, r_data1, r_data2, sys_volt, a, r_data):
        if byte == 1:  # 16bitデータ変換
            return (
                cmd.change_type(d_type, r_data1[0], sys_volt, byte, r_data),
                cmd.change_type(d_type, r_data2[0], sys_volt, byte, r_data))
        else:  # 32bitデータ変換
            return (
                cmd.change_type(d_type, (r_data1[1] << 16) + r_data1[0], sys_volt, byte, r_data),
                cmd.change_type(d_type, (r_data2[1] << 16) + r_data2[0], sys_volt, byte, r_data))
    # ループ処理
    row1=list(r_data.items())
    row2=list(k_data.items())
    k_list=len(k_data)
    for a in range(r_list):
        if a>=k_list:b=0
        else:b=a
        byte, d_type = row1[a][1][1], row1[a][1][4]
        #print(hex(row1[a][1][0]),byte, hex(row2[b][1][0]),2)
        r_data1, r_data2,r_data3,r_data4, err = modbus_read(row1[a][1][0], byte, row2[b][1][0],2)
        #print(r_data1,r_data2,r_data3,r_data4)
        hyrd1.append(r_data1[0]),hyrd2.append(r_data2[0])
        data1, data2 = process_data(byte, d_type, r_data1, r_data2, sys_volt1[0], a, row1[a][1])
        #print(data1,data2)
        hywd1.append(data1),hywd2.append(data2)
        byte, d_type = row2[b][1][1], row2[b][1][4]
        if row2[b][1][0]<0x0010:
            data3, data4 = r_data3[1] / (10 ** d_type), r_data4[1] / (10 ** d_type)  # 16bitデータ変換
            if row2[b][1][0]==0x000c and r_data3[1]>100:data3=cmd.ffff(data3)
            if row2[b][1][0]==0x000c and r_data4[1]>100:data4=cmd.ffff(data4)
        else:  # 32bitデータ変換
            if row2[b][1][0]<0x0200:
                data3 = cmd.ffffx2(r_data3[0], r_data3[1])/10
                data4 = cmd.ffffx2(r_data4[0], r_data4[1])/10
            else:
                data3 = (r_data3[0] << 16) + r_data3[1]
                data4 = (r_data4[0] << 16) + r_data4[1]
        #print(data3,data4)
        if a<k_list:kmrd1.append(r_data3[0]), kmrd2.append(r_data4[0]),kmwd1.append(data3), kmwd2.append(data4)
        #print(hyrd1,hyrd2,hywd1,hywd2,kmrd1,kmrd2,kmwd1,kmwd2)
    csv_data0 = [date_time] + hywd1+hywd2+kmwd1+kmwd2
    csv_data1 = [date_time] + hywd1
    csv_data2 = [date_time] + hywd2
    csv_data3 = [date_time] + kmwd1 + kmwd2
    if r_data == r_data:# 必要な計算処理
        #print("\n",hywd1,"\n",hywd2)
        q_rdd = [cmd.ffff(hyrd1[14]), cmd.ffff(hyrd2[14]),
                cmd.ffff(hyrd1[8]), cmd.ffff(hyrd2[8])]
        i_calc = ((hyrd1[0] * hyrd1[1]) + (hyrd2[0] * hyrd2[1])) / 100  # AC入力電力
        o_calc = q_rdd[2] + q_rdd[3]  # AC出力電力(有効)
        p_calc = hyrd1[19] + hyrd2[19]  # PV入力電力
        b_calc = round(((hyrd1[13] * q_rdd[0] + hyrd2[13] * q_rdd[1]) / 100), 1)  # バッテリー電力
        b_curr = (q_rdd[0] + q_rdd[1]) / 10  # バッテリー電流
        s_calc = round((i_calc - o_calc + b_calc + p_calc), 1)  # 消費電力
        p_powr = round(((hyrd1[13] * hyrd1[20] + hyrd2[13] * hyrd1[20]) / 100), 1)  # PV充電電力
        g_powr = round(((hyrd1[13] * hyrd1[3] + hyrd2[13] * hyrd1[3]) / 100), 1)  # AC充電電力
        # 効率計算
        o_powr = round((o_calc) / (i_calc + p_calc + b_calc) * 100, 1) if b_calc < 0 else round(o_calc / (s_calc + o_calc) * 100, 1)
        # 計算結果のリスト化
        calc_list = [
            b_curr, b_calc, p_calc, i_calc, o_calc, s_calc,
            hyrd1[27] + hyrd2[27], hyrd1[28] + hyrd2[28],
            (hyrd1[29] + hyrd2[29]) / 10, (hyrd1[30] + hyrd2[30]) / 10,
            hyrd1[31] + hyrd2[31], (hyrd1[32] + hyrd2[32]) / 10,
            p_powr, g_powr, o_powr]
        # リスト内容を追加
        o_data.extend(calc_list)
    return date_time, hywd1, hywd2, kmwd1, kmwd2, o_data, csv_data0, csv_data1, csv_data2, csv_data3, err

# ----------モニター画面
def create_gui(): # GUI作成
    root=tk.Tk()
    root.geometry('830x1000+0+0') # ウインドウサイズ
    root.title("HYP4850U100-H 並列モニター") # ウインドウタイトル
    frame=tk.Frame(root)
    frame.grid(row=0,column=0,sticky=tk.NSEW,padx=5,pady=10)
    wid=[19,13,5,13,5]
    col1='#0000ff' # データ文字色
    col2='#cccccc' # データ背景色
    r_list,t_list,v_list,k_list=len(r_data),len(t_data),len(v_data),len(k_data)
    r1_data,k1_data=list(r_data.items()),list(k_data.items())
    n_data,n_list=[r1_data,k1_data],[r_list,k_list]
    err,states=["\n \n \n"],[""]
    [tk.Label(frame, width=wid[t_data[i][3]], text=t_data[i][0], # font=("MS Gothic", 9,),
        anchor=tk.W).grid(column=t_data[i][1], row=t_data[i][2]) for i in range(t_list)] # 項目表示

    label0=tk.Label(frame,width=wid[0],text=date_time,#font="bold",# 種別表示"bold"太字
                    anchor=tk.W,borderwidth=1)
    label0.grid(column=5,row=0) # ログ日時表示
    label1=tk.Label(frame,width=wid[0],text=err,#font="bold",# 種別表示"bold"太字
                    anchor=tk.W,borderwidth=1)
    label1.grid(column=0,row=0) # error表示
    label2=tk.Label(frame,width=wid[1],text=states,#font="bold",# 種別表示"bold"太字
                    anchor=tk.W,borderwidth=1)
    label2.grid(column=1,row=0) # ステータス表示

    for j in range(2):
        [tk.Label(frame, width=wid[0], text=n_data[j][i][1][5], anchor=tk.W) 
                .grid(column=n_data[j][i][1][2], row=n_data[j][i][1][3])for i in range(n_list[j])] # list表示
        for k in range(2):  
            [tk.Label(frame, width=wid[4], text=n_data[j][i][1][6], anchor=tk.W)
                .grid(column=n_data[j][i][1][2] + 2 + 2 * k, row=n_data[j][i][1][3])
                for i in range(n_list[j])] # 単位表示 

    labels1=[tk.Label(frame,width=wid[1],text=hywd1[x]
                      ,anchor=tk.E,relief=tk.SOLID,borderwidth=1 # ID1データ表示
                      ,foreground=col1,background=col2)for x in range(r_list)]
    [labels1[h].grid(column=r1_data[h][1][2]+1,row=r1_data[h][1][3])for h in range(r_list)]
    labels2=[tk.Label(frame,width=wid[3],text=hywd1[x]
                      ,anchor=tk.E,relief=tk.SOLID,borderwidth=1 # ID2データ表示
                      ,foreground=col1,background=col2)for x in range(r_list)]
    [labels2[h].grid(column=r1_data[h][1][2]+3,row=r1_data[h][1][3])for h in range(r_list)]
    labels4=[tk.Label(frame,width=wid[1],text=kmwd1[x]
                      ,anchor=tk.E,relief=tk.SOLID,borderwidth=1 # km1データ表示
                      ,foreground=col1,background=col2)for x in range(k_list)]
    [labels4[h].grid(column=k1_data[h][1][2]+1,row=k1_data[h][1][3])for h in range(k_list)]
    labels5=[tk.Label(frame,width=wid[3],text=kmwd1[x]
                      ,anchor=tk.E,relief=tk.SOLID,borderwidth=1 # km2データ表示
                      ,foreground=col1,background=col2)for x in range(k_list)]
    [labels5[h].grid(column=k1_data[h][1][2]+3,row=k1_data[h][1][3])for h in range(k_list)]
    
    for i in range(v_list): # 追加項目表示
        tk.Label(frame, width=wid[0], text=v_data[i][0], 
        anchor=tk.W).grid(column=v_data[i][1], row=v_data[i][2]) # list表示
        tk.Label(frame, width=wid[4], text=v_data[i][5], 
        anchor=tk.W).grid(column=v_data[i][1] + 2, row=v_data[i][2]) # 単位表示
    labels3=[tk.Label(frame,width=wid[1],text=o_data[x]
                      ,anchor=tk.E,relief=tk.SOLID,borderwidth=1 # 追加データ表示1
                      ,foreground=col1,background=col2)for x in range(v_list)]
    [labels3[h].grid(column=v_data[h][1]+1,row=v_data[h][2])for h in range(v_list)]
    labels6=[tk.Label(frame,width=wid[1],text=o_data[v_list+x]
                      ,anchor=tk.E,relief=tk.SOLID,borderwidth=1 # 追加データ表示2
                      ,foreground=col1,background=col2)for x in range(2)]
    [labels6[h].grid(column=v_data[h][1]+3,row=v_data[h][2]+2)for h in range(2)]
    labels7=tk.Label(frame,width=wid[1],text=o_data[len(o_data)-1]
                      ,anchor=tk.E,relief=tk.SOLID,borderwidth=1 # 追加データ表示3
                      ,foreground=col1,background=col2)
    labels7.grid(column=8,row=25)

    button1=tk.Button(frame,text="計測終了",command=root.destroy) # ループ終了
    button1.grid(column=8,row=0)
    button2=tk.Button(frame,text="機器設定",command=root.destroy) # ループ終了
    button2.grid(column=6,row=0)
    button3=tk.Button(frame,text="チャート表示",command=root.destroy)  # チャート移動
    button3.grid(column=3,row=0)

    thread1 = threading.Thread(target=update_data,
    args=(label0, labels1, labels2, labels3, labels4, labels5, labels6, labels7, label1,label2))

    thread1.daemon=True # スレッド終了
    thread1.start() # スレッド処理開始

    root.mainloop() # メインループ開始

# ----------ファイル操作
def file_setup(file_time): # ファイル作成
    file_name1 = id_name1 + file_time + ".csv"
    file_name2 = id_name2 + file_time + ".csv"
    file_name3 = id_name3 + file_time + ".csv"
    print("新しいファイルが作成されました")
    print("ID1 ログファイル名:", file_name1)
    print("ID2 ログファイル名:", file_name2)
    print("電力計ログファイル名:", file_name3)
    return file_name1, file_name2, file_name3
def file_make(file_name0,file_name1,file_name2,file_name3): # ファイル書込
    with open(file_name1,'w',newline='')as file1: # hybrid1 file
        writer1=csv.writer(file1)
        [writer1.writerow([n_data1,u_data1][i])for i in range(2)]# ヘッダー書込
        writer1.writerow(csv_data1)
    with open(file_name2,'w',newline='')as file2: # hybrid2 file
        writer2=csv.writer(file2)
        [writer2.writerow([n_data2,u_data2][i])for i in range(2)]
        writer2.writerow(csv_data2)
    with open(file_name3,'w',newline='')as file3: # KM-N1 file
        writer3=csv.writer(file3)
        [writer3.writerow([n_data3,u_data3][i])for i in range(2)]
        writer3.writerow(csv_data3)
    with open(file_name0,'w', newline='') as file: # log file                  
        writer=csv.writer(file)
        writer.writerow(csv_data0)
    return
        
# ----------データ更新処理
def update_data(label0, labels1, labels2, labels3, labels4, labels5, labels6, labels7, label1,label2): # データ更新
    # 初期設定
    current_date = dt.datetime.now().strftime("_20%y_%m_%d")  # 初期の日付
    global file_name1, file_name2, file_name3, file_name0

    while True:
        # データ取得
        r_list, k_list = len(r_data), len(k_data)
        date_time, hywd1, hywd2, kmwd1, kmwd2, o_data, csv_data0, csv_data1, csv_data2, csv_data3, err = data_read()

        # 日付が変わった場合、新しいファイルを作成
        new_date = dt.datetime.now().strftime("_20%y_%m_%d")
        if new_date != current_date:  # 日付が変わった場合
            current_date = new_date  # 現在の日付を更新
            file_time = dt.datetime.now().strftime("_20%y_%m_%d_%H%M")
            file_name1, file_name2, file_name3 = file_setup(file_time)
            
            # 'today_logfile.csv' ファイルを削除して新規作成
            if os.path.exists(file_name0):
                os.remove(file_name0)  # 既存ファイル削除
            with open(file_name0, 'w', newline='') as file:
                writer = csv.writer(file)
                #writer.writerow(["日時", "データ1", "データ2", "..."])  # 新しいヘッダーを記述
            print(f"新しい {file_name0} ファイルが作成されました")

        # CSVデータ更新
        with open(file_name1, 'a', newline='') as file1:
            writer1 = csv.writer(file1)
            writer1.writerow(csv_data1)
        with open(file_name2, 'a', newline='') as file2:
            writer2 = csv.writer(file2)
            writer2.writerow(csv_data2)
        with open(file_name3, 'a', newline='') as file3:
            writer3 = csv.writer(file3)
            writer3.writerow(csv_data3)
        with open(file_name0, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(csv_data0)

        # GUIデータ更新
        label0.config(text=f"{date_time}")
        [labels1[x].config(text=f"{hywd1[x]}") for x in range(r_list)]
        [labels2[x].config(text=f"{hywd2[x]}") for x in range(r_list)]
        [labels3[x].config(text=f"{o_data[x]}") for x in range(len(v_data))]
        [labels4[x].config(text=f"{kmwd1[x]}") for x in range(k_list)]
        [labels5[x].config(text=f"{kmwd2[x]}") for x in range(k_list)]
        [labels6[x].config(text=f"{o_data[len(o_data) - 3 + x]}") for x in range(2)]
        labels7.config(text=f"{o_data[len(o_data) - 1]}")
        label1.config(text=f"{err}")
        #print(f"エラー内容: {err}")

        # インバーター監視
        st = "Hy_Inv:"
        row1=list(r_data.items())
        if kmwd1[0] == 0 or kmwd2[0] == 0: # 系統電力停電中
            st_text = "自立運転中" if float(hywd1[0]) == 0 or float(hywd2[0]) == 0 and hywd1[4] == row1[4][1][11][5] and hywd2[4] == row1[4][1][11][5] else inv_on(st)
        else:  # 系統電力受電中
            if hywd1[4] == row1[4][1][11][5] and hywd2[4] == row1[4][1][11][5]:  # インバーター運転中
                if float(hywd1[8]) == 0 and float(hywd2[8]) == 0:  # インバータ―出力無
                    if float(hywd1[17]) == 0 and float(hywd2[17]) == 0: # PV入力無
                        if float(hywd1[0]) == 0 and float(hywd2[0]) == 0: # AC入力無
                            modbus_write(0xdf00, [0], 1)  # ハイブリッドインバーター1停止
                            modbus_write(0xdf00, [0], 2)  # ハイブリッドインバーター2停止
                            st1 = f"{st}ID1{'停止失敗' if modbus_read(0xdf00, 1, 0, 1)[0][0] == 1 else '停止'}"
                            st2 = f"{st}ID2{'停止失敗' if modbus_read(0xdf00, 1, 0, 1)[1][0] == 1 else '停止'}"
                            st_text=f"{st1}\n{st2}"  
                        else:st_text="商用充電(待機)中" # AC入力有
                    else:st_text="PV充電(待機)中" # PV入力有
                else: st_text = "Inv出力中" if float(hywd1[17]) == 0 and float(hywd2[17]) == 0 and float(hywd1[0]) == 0 and float(hywd2[0]) == 0 else "充電/待機" # インバータ―出力有
            else:   # インバーター停止中
                if hywd1[4] == row1[4][1][11][4] and hywd2[4] == row1[4][1][11][4]:st_text="バイパス出力中" # バイパス出力中
                else:st_text = "Hy_Inv停止中" if float(hywd1[17]) == 0 and float(hywd2[17]) == 0 and float(hywd1[0]) == 0 and float(hywd2[0]) == 0 else inv_on(st)   
        label2.config(text=f"{st_text}")

        sleep(interval1 + 1.8)  # インターバルタイマー
        
# ----------CSVファイル設定
sys_volt1,sys_volt2,a,a,err=modbus_read(0xe003,1,0,1) # システム電圧読込
sys_id1,sys_id2,a,a,err=modbus_read(0x0035,20,0,1) # プロダクトID読込
dt_now = dt.datetime.now() # 日時を取得
file_time=dt_now.strftime('_20%y_%m_%d_%H%M')
id_name1,id_name2,id_name3='','','KM-N1'
for a in range(20):
    id_name1=id_name1+chr(sys_id1[a])
    id_name2=id_name2+chr(sys_id2[a])
file_name0='today_logfile.csv'
file_name1,file_name2,file_name3=file_setup(file_time)

for a in range(3):
    m_data1=[r_data,r_data,k_data]
    n_data,u_data=[file_time],["日付"]
    for b in range(len(m_data1[a])):
        row=list(m_data1[a].items())
        n_data.append(row[b][1][5])
        u_data.append(row[b][1][6])
    if a==0:n_data1,u_data1=n_data,u_data
    if a==1:n_data2,u_data2=n_data,u_data
    if a==2:n_data3,u_data3=n_data+n_data[1:],u_data+u_data[1:]
    
# ----------ファイル作成
date_time,hywd1,hywd2,kmwd1,kmwd2,o_data,csv_data0,csv_data1,csv_data2,csv_data3,err=data_read()
file_make(file_name0,file_name1,file_name2,file_name3)

# ----------実行
if __name__ == "__main__":
    create_gui()
