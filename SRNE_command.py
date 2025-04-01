

#name:[0:address,1:byte,2:x,3:y,4:type,5:name,6:unit,7:len,8:min,9:max,10:set,11:list]
read_command={
    'Grid_voltage':[
        0x0213,1, 0, 2,1,"系統電圧"    ,"V(AC)"],#0
    'Grid_current':[
        0x0214,1, 0, 3,1,"系統電流"    ,"A(AC)"],#1
    'Grid_frequency':[
        0x0215,1, 0, 4,2,"系統周波数"  ,"Hz"],#2
    'Grid_charge_current':[
        0x021e,1, 0, 5,1,"系統充電電流","A(DC)"],#3
    'Machine_state':[
        0x0210,1, 0, 7,8,"機器状態"    ,"",
        0,0,0,"",["起動","待機","初期化","省電力","商用出力","インバーター出力","系統出力","混合出力","-","-","停止","故障"]],#4
    'Inverter_voltage':[
        0x0216,1, 0, 8,1,"出力電圧"    ,"V(AC)"],#5
    'Load_current':[
        0x0219,1, 0, 9,1,"出力電流"    ,"A(AC)"],#6
    'Inverter_frequency':[
        0x0218,1, 0,10,2,"出力周波数"  ,"Hz"],#7
    'Load_active_power':[
        0x021b,1, 0,11,0,"負荷有効電力","W"],#8
    'Load_apparent_power':[
        0x021c,1, 0,12,0,"負荷皮相電力","W"],#9
    'Load_ratio':[
        0x021f,1, 0,13,0,"負荷率"      ,"%"],#10
    'Charge_state':[
        0x010b,1, 0,15,8,"充電状態"    ,"",
        0,0,0,"",["未充電","定電流(CC)充電","定電圧(CV)充電","-","浮遊充電","-","充電中1","充電中2"]],#11
    'Battery_soc':[
        0x0100,1, 0,16,0,"蓄電池SOC"   ,"%"],#12
    'Battery_voltage':[
        0x0101,1, 0,17,1,"蓄電池電圧"  ,"V(DC)"],#13
    'Battery_current':[
        0x0102,1, 0,18,1,"蓄電池電流"  ,"A(DC)"],#14
    'Charge_power':[
        0x010e,1, 0,19,0,"充電電力"    ,"W"],#15
    'Inverter_current':[
        0x0217,1, 0,20,1,"INV電流 "    ,"A(AC)"],#16
    'PV_panel_voltage':[
        0x0107,1, 0,22,1,"PV入力電圧"  ,"V(DC)"],#17
    'PV_panel_current':[
        0x0108,1, 0,23,1,"PV入力電流"  ,"A(DC)"],#18
    'PV_charge_power':[
        0x0109,1, 0,24,0,"PV入力電力"  ,"W"],#19
    'PV_back_current':[
        0x0224,1, 0,25,1,"PV降圧電流"  ,"A(DC)"],#20
    'DC_bus_voltage':[
        0x0212,1, 0,27,1,"DCバス電圧"  ,"V(DC)"],#21
    'Back_current':[
        0x0225,1, 0,28,1,"降圧電流"    ,"A(DC)"],#22
    'PV_heatshink_temperature':[
        0x0220,1, 0,29,1,"PVHT温度"    ,"℃"],#23
    'Inverter_heatshink_temperature':[
        0x0221,1, 0,30,1,"INVHT温度"   ,"℃"],#24
    'Trans_temperature'  :[
        0x0222,1, 0,31,1,"Tr温度"      ,"℃"],#25
    'Inner_temperature'  :[
        0x0223,1, 0,32,1,"内部温度"    ,"℃"],#26
    'Today_Battry_charge':[
        0xf02d,1, 5, 2,0,"本日充電量"  ,"Ah"],#27
    'Today_battery_discharge':[
        0xf02e,1, 5, 3,0,"本日放電量"  ,"Ah"],#28
    'Today_PV_power':[
        0xf02f,1, 5, 4,1,"本日発電量"  ,"kWh"],#29
    'Today_Load_power' :[
        0xf030,1, 5, 5,1,"本日消費量"  ,"kWh"],#30
    'Today_main_charge':[
        0xf03c,1, 5, 6,0,"本日商用充電量","Ah"],#31
    'Today_bypass_load':[
        0xf03d,1, 5, 7,1,"本日商用電力消費量","kWh"],#32
    'Today_inverter_working':[
        0xf03e,1, 5, 8,0,"本日インバーター稼働時間","時間"],#33
    'Today_bypass_working':[
        0xf03f,1, 5, 9,0,"本日バイパス稼働時間","時間"],#34
    'Accumulated_Battry_charge':[
        0xf034,2, 5,11,0,"累積充電量"  ,"Ah"],#35
    'Accumulated_Battry_discharge':[
        0xf036,2, 5,12,0,"累積放電量"  ,"Ah"],#36
    'Accumulated_PV_power' :[
        0xf038,2, 5,13,0,"累積発電量"  ,"kWh"],#37
    'Accumulated_load_power':[
        0xf03a,2, 5,14,0,"累積負荷積算電力量","kWh"],#38
    'Accumulated_bypass_load' :[
        0xf046,2, 5,15,0,"累積商用充電量","kWh"],#39
    'Accumulated_main_charge' :[
        0xf048,2, 5,16,0,"累積商用負荷電力消費量","kWh"],#40
    'Accumulated_inverter_time':[
        0xf04a,1, 5,17,0,"累積インバーター稼働時間","時間"],#41
    'Accumulated_bypass_time':[
        0xf04b,1, 5,18,0,"累積バイパス稼働時間","時間"]}#42

write_command={
    'Max_PV_charge_current':[
        0xe001,1, 5,11,1,"PV最大充電電流"  ,"A",800,0,800,"設定36"],#33
    'Nomal_battery_capacity':[
        0xe002,1, 0, 4,1,"蓄電池容量"      ,"Ah",900,0,900,""],#2
    'Battery_type':[
        0xe004,1, 0, 2,8,"蓄電池タイプ"    ,"",14,0,13,"設定08",
        ["ユーザー設定","密閉型鉛","開放型鉛","ゲル型鉛",
        "LFPx14","LEPx15","LFPx16","LFPx7","LFPx8","LFPx8",
        "NCAx7","NCAx8","NCAx13","NCAx14"]],#0
    'Over_voltage':[
        0xe005,1, 0, 5,4,"過電圧停止電圧"  ,"V",50,100,150,""],#3
    'Limit_charge_voltage':[
        0xe006,1, 0, 6,4,"充電上限電圧"    ,"V",50,100,150,""],#4
    'Battery_equalization_voltage':[
        0xe007,1, 0,21,4,"均等充電電圧"    ,"V",50,100,150,"設定17"],#19
    'Battery_boost_charge_voltage':[
        0xe008,1, 0, 9,4,"CC充電電圧"      ,"V",50,100,150,"設定09"],#7
    'Battery_floating_charge_voltage':[
        0xe009,1, 0, 7,4,"CV充電電圧"      ,"V",50,100,150,"設定11"],#5
    'Battery_charge_recovery':[
        0xe00a,1, 0,13,4,"充電再開電圧"    ,"V",50,100,150,"設定37"],#11
    'Battery_undervoltage_recovery':[
        0xe00b,1, 0,14,4,"低電圧復帰電圧"  ,"V",50,100,150,"設定35"],#12
    'Battery_undervoltage_alarm':[    
        0xe00c,1, 0,15,4,"低電圧警告電圧"  ,"V",50,100,150,"設定14"],#13
    'Battery_over_discharge_voltage':[
        0xe00d,1, 0,17,4,"過放電遅延オフ電圧","V",50,100,150,"設定12"],#15
    'Battery_discharge_limit_voltage':[
        0xe00e,1, 0,19,4,"放電停止電圧"    ,"V",50,100,150,"設定15"],#17
    'BMS_discharge_stop_SOC':[
        0xe00f,1, 5, 6,0,"放電停止SOC"     ,"%",100,0,100,"設定59"],#28    
    'Battery_over_discharge_delay_time':[
        0xe010,1, 0,18,0,"過放電遅延オフ時間","s",60,0,60,"設定13"],#16
    'Battery_equalization_time':[
        0xe011,1, 0,22,0,"均等充電時間"    ,"min",120,0,120,"設定18"],#20
    'Battery_boost_charge_time':[
        0xe012,1, 0,11,0,"CC充電遅延時間"  ,"min",120,0,120,"設定10"],#9
    'Battery_equalization_interval':[
        0xe013,1, 0,24,0,"均等充電間隔"    ,"day",7,0,7,"設定20"],#22
    'Turn_to_main_voltage':[
        0xe01b,1, 0,16,4,"バイパス切替電圧","V",50,100,150,"設定04"],#14
    'Stop_charge_current':[
        0xe01c,1, 0, 8,1,"充電停止電流"    ,"A",100,0,100,"設定57"],#6
    'BMS_charge_stop_SOC':[
        0xe01d,1, 5, 7,0,"充電停止SOC"     ,"%",100,0,100,"設定60"],#29
    'BMS_discharge_alarm_SOC':[
        0xe01e,1, 5, 5,0,"過放電警報SOC"   ,"%",100,0,100,"設定58"],#27
    'BMS_to_main_SOC':[
        0xe01f,1, 5, 8,0,"バイパス切替SOC" ,"%",100,0,100,"設定61"],#30
    'BMS_to_inverter_SOC':[
        0xe020,1, 5, 9,0,"INV切替SOC"      ,"%",100,1,100,"設定62"],#31
    'Turn_to_inverter_voltage':[
        0xe022,1, 0,12,4,"INV切替電圧"     ,"V",50,100,150,"設定05"],#10
    'Battery_equalization_charge_timeout':[
        0xe023,1, 0,23,0,"均等充電遅延"    ,"min",120,0,120,"設定19"],#21
    'BMS_charge_limit_mode':[
        0xe025,1, 5, 4,8,"充電制御"        ,"",3,0,2,"設定39",
        ["OFF","BMS制御","INV制御"]],#26
    '1-section_start_charge_time':[
        0xe026,1,10, 2,7,"充電開始時間１"  ,"",0,0,0,"設定40"],#55
    '1-section_end_charge_time':[
        0xe027,1,10, 3,7,"充電終了時間１"  ,"",0,0,0,"設定41"],#56
    '2-section_start_charge_time':[
        0xe028,1,10, 4,7,"充電開始時間２"  ,"",0,0,0,"設定42"],#57
    '2-section_end_charge_time':[
        0xe029,1,10, 5,7,"充電終了時間２"  ,"",0,0,0,"設定43"],#58
    '3-section_start_charge_time':[
        0xe02a,1,10, 6,7,"充電開始時間３"  ,"",0,0,0,"設定44"],#59
    '3-section_end_charge_time':[
        0xe02b,1,10, 7,7,"充電終了時間３"  ,"",0,0,0,"設定45"],#60
    'On_time_charge':[
        0xe02c,1,10, 8,6,"充電時間設定"    ,"",2,0,1,"設定46"],#61
    '1-section_start_discharge_time':[
        0xe02d,1,10, 9,7,"放電開始時間１"  ,"",0,0,0,"設定47"],#62
    '1-section_end_charge_time':[
        0xe02e,1,10,10,7,"放電終了時間１"  ,"",0,0,0,"設定48"],#63
    '2-section_start_discharge_time':[
        0xe02f,1,10,11,7,"放電開始時間２"  ,"",0,0,0,"設定49"],#64
    '2-section_end_charge_time':[
        0xe030,1,10,12,7,"放電終了時間２"  ,"",0,0,0,"設定50"],#65
    '3-section_start_discharge_time':[
        0xe031,1,10,13,7,"放電開始時間３"  ,"",0,0,0,"設定51"],#66
    '3-section_end_charge_time':[
        0xe032,1,10,14,7,"放電終了時間３"  ,"",0,0,0,"設定52"],#67
    'On_time_dischage':[
        0xe033,1,10,15,6,"放電時間設定"    ,"",0,0,0,"設定53"],#68
    'Grid_and_mixload':[
        0xe037,1, 5,21,8,"ハイブリッド出力","",3,0,2,"設定34",
        ["OFF","AC入力PV出力","AC出力PV出力"]],#43
    'Leakage_current_detection':[
        0xe038,1, 5,27,6,"漏電検知機能"    ,"",2,0,1,"設定56"],#49
    'Model_output_power_rate':[
        0xe118,1, 5,17,1,"定格出力"        ,"kW",100,0,100,""],#39
    'Model_PV_voltage_rate':[
        0xe11f,1, 5,10,0,"PV最大電圧"      ,"V",500,0,500,""],#32
    'Model_PV_max_charge_current':[
        0xe120,1, 5,12,1,"最大充電電流"    ,"A",1000,0,1000,""],#34       
    'RS485_address':[
        0xe200,1, 5,24,0,"RS485アドレス"   ,"",240,1,240,"設定30"],#46
    'Parallel_mode':[
        0xe201,1, 5,19,8,"並列運転モード"  ,"",8,0,7,"設定31",
        "単相","並列","2P0","2P1","2P2","3P1","3P2","3P3"],#41 
    'Output_priority':[
        0xe204,1, 5,13,8,"出力優先"        ,"",3,0,2,"設定01",
        ["PV優先","系統優先","蓄電池優先"]],#35
    'Max_AC_charge_current':[
        0xe205,1, 5,20,1,"AC充電最大電流"  ,"A",400,0,400,"設定28"],#42
    'Battery_equalization':[
        0xe206,1, 0,20,6,"均等充電有無"    ,"",2,0,1,"設定16"],#18
    'N-G_function':[
        0xe207,1, 5,26,6,"N相出力"         ,"",2,0,1,"設定63"],#48
    'Output_voltage':[
        0xe208,1, 5,15,1,"AC出力電圧"      ,"V",20,100,120,"設定38"],#37
    'Output_frequency':[
        0xe209,1, 5,14,2,"AC出力周波数"    ,"Hz",2,5000,6000,"設定02"],#36
    'Max_charge_current':[
        0xe20a,1, 0,10,1,"最大充電電流"    ,"A",600,0,600,"設定07"],#8
    'AC_input_voltage_range':[
        0xe20b,1, 5,18,8,"AC入力電圧範囲"  ,"",2,0,1,"設定03",
        "APL(90-280V)","UPS(90-140V)"],#40
    'Power_saving_mode':[
        0xe20c,1, 5,22,6,"省エネモード"    ,"",2,0,1,"設定22"],#44
    'Restart_when_overload':[
        0xe20d,1, 5,31,6,"過負荷停止再起動","",2,0,1,"設定23"],#53
    'Restart_when':[
        0xe20e,1, 5,32,6,"高温停止再起動"  ,"",2,0,1,"設定24"],#54
    'Charge_source_priority':[
        0xe20f,1, 0, 3,8,"充電モード"      ,"",4,0,3,"設定06",
        ["PV優先","系統優先","ハイブリッド","PV専用"]],#1
    'Ararm':[
        0xe210,1, 5,29,6,"警報音有無"      ,"",2,0,1,"設定25"],#51
    'Output_change_alarm':[
        0xe211,1, 5,30,6,"電源切替警報有無","",2,0,1,"設定26"],#52
    'Bypass_output_when_overload':[
        0xe212,1, 5,23,6,"バイパス出力有無","",2,0,1,"設定27"],#45
    'Record_fault_cord':[
        0xe213,1, 5,28,6,"障害記録"        ,"",2,0,1,""],#50
    'Split_phase':[
        0xe214,1, 5,25,6,"分相変圧器"      ,"",2,0,1,"設定29"],#47
    'BMS_conect':[
        0xe215,1, 5, 2,8,"BMS通信"         ,"",3,0,2,"設定32",
        ["OFF","RS485-BMS","CAN-BMS"]],#24
    'Model_inverter_max_current':[
        0xe129,1, 5,16,1,"最大出力電流"    ,"A",420,0,420,""],#38
    'BMS_protocol':[
        0xe21b,1, 5, 3,8,"BMSプロトコル"   ,"",18,0,17,"設定33",
        ["Pace","Rata","Allgrand","Oliter","PCT","Sunwoda","Dyness","SRNE","Pylontech",
        "","","","","","","","WS Technicals","Uz Energy"]],#25
    'Battery_equalization_immediately':[
        0xdf0d,1, 0,25,6,"均等充電有効化"    ,"",2,0,1,"設定21"]}#23
         
        #["設定54,55",""],

