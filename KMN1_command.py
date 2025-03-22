read_command={
    'R-N:voltage':[
        0x0000,2,0,36,1,"電圧1","V"],
    'R:current':[
        0x0006,2,0,39,3,"電流1","A"],
    'T-N:voltage':[
        0x0002,2,0,37,1,"電圧2","V"],
    'T:current':[
        0x0008,2,0,40,3,"電流2","A"],
    'R-T:voltage':[
        0x0004,2,0,38,1,"電圧3","V"],
    'N:current':[
        0x000a,2,0,41,3,"電流3","A"],
    'Power_factor':[
        0x000c,2,0,42,2,"力率",""],
    'Frequency':[
        0x000e,2,0,43,1,"周波数","Hz"],
    'Active_Power':[
        0x0010,2,0,44,1,"有効電力","W"],
    'Reactive_Power':[
        0x0012,2,0,45,1,"無効電力","Var"],
    'Integrated active energy1':[
        0x0200,2,5,36,0,"積算有効電力量","Wh"],
    'Accumulated regenerative energy1':[
        0x0202,2,5,37,0,"積算回生電力量","Wh"],
    'Accumulated leading reactive energy1':[
        0x0204,2,5,38,0,"積算進み無効電力量","Varh"],
    'Accumulated lag reactive energy1':[
        0x0206,2,5,39,0,"積算遅れ無効電力量","Varh"],
    'Total integrated reactive energy1':[
        0x0208,2,5,40,0,"積算総合無効電力量","Varh"],
    'Integrated active energy2':[
        0x0220,2,5,41,0,"積算有効電力量","kWh"],
    'Accumulated regenerative energy2':[
        0x0222,2,5,42,0,"積算回生電力量","kWh"],
    'Accumulated leading reactive energy2':[
        0x0224,2,5,43,0,"積算進み無効電力量","kVarh"],
    'Accumulated lag reactive energy2':[
        0x0226,2,5,44,0,"積算遅れ無効電力量","kVarh"],
    'Total integrated reactive energy2':[
        0x0228,2,5,45,0,"積算総合無効電力量","kVarh"]}