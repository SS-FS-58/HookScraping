body_json.BuJians[0].Width.Value = 440
body_json.BuJians[0].Height.Value = 260
body_json.BuJians[1].Width.Value = 440
body_json.BuJians[1].Height.Value = 260

body_json.ChengPinWidth = 260
body_json.ChengPinHeight = 180
body_json.ShuLiang = "1004"
body_json.ZhiJiaWidth = 440
body_json.ZhiJiaHeight = 260
body_json.ZhiJiaoHouDu = "2.5"
body_json.ChuanHuanBian = "210"//"140"
body_json.ChuanHuanYanSe = "黑白色"//"彩色"


//Text

body_json.BuJians[2].P = 12 = 6 * 2;
body_json.BuJians[2].ShuLiang = 6;
//Text gsm
//Inner
body_json.BuJians[0].ZhiZhang.LeiXing = 15;
body_json.BuJians[0].ZhiZhang.KeZhong = 112;
body_json.BuJians[0].SFYinShua = true;

//outer

body_json.BuJians[1].SFYinShua = true;
body_json.BuJians[1].ZhengMianColor.ZhuanSe = 9
// body_json.BuJians[1].FanMianColor.ZhuanSe = 7
//main
body_json.BuJians[2].ZhengMianColor.ZhuanSe = 9
body_json.BuJians[2].FanMianColor.ZhuanSe = 15
body_json.BuJians[2].ZhiZhang.LeiXing = 16;
body_json.BuJians[2].ZhiZhang.KeZhong = 115;
//inner
body_json.BuJians[0].ZhengMianColor.ZhuanSe = 7



"LeiXing": [
    "C2S": 14,
    "SBS": 16,
    "Wooden free paper": 15,
    "Kraft Paper"17,
]

"KeZhong": [
    "C2S": [
        "80": 13,
        "128": 9,
        "105": 123,
        "157": 111,
        "200": 11,
        "250": 102,
        "300": 103,
        "350": 14,
    ]
    "SBS": [
        "210": 114,
        "230": 115,
        "250": 116,
        "300": 117,
    ],
    "Wooden free paper": [
        "60": 21,
        "70": 18,
        "80": 112,
        "100": 16,
        "120": 17,
        "140": 19,
        "180": 113,
    ],
    "Kraft Paper": [
        "60": 161,
        "70": 105,
        "100": 167,
        "120": 163,
    ],
]

body_json.BuJians[2].ZhengMianColor.ZhuanSe = 8
body_json.BuJians[2].FanMianColor.ZhuanSe = 8
//Outer Liner Liner Whether to print
body_json.BuJians[2].SFYinShua = true;
//Inner  Liner Whether to print
body_json.BuJians[0].SFYinShua = true;


// FuMo
body_json.BuJians[1].HouGong.FuMo.FuMoZhongLei = "亮膜", "", "哑膜"
body_json.BuJians[1].HouGong.FuMo.Enable = true;
body_json.BuJians[1].HouGong.FuMo.ShuangMianFuMo = false; always

//Foil Stamping (silver)L*W
body_json.BuJians[1].HouGong.DanMianTangYin.Enable = true;
body_json.BuJians[1].HouGong.DanMianTangYin.Width = 12;
body_json.BuJians[1].HouGong.DanMianTangYin.Height = 34;

//Foil Stamping (gold)

body_json.BuJians[1].HouGong.DanMianTangJin.Enable = true;
body_json.BuJians[1].HouGong.DanMianTangJin.Width = 12;
body_json.BuJians[1].HouGong.DanMianTangJin.Height = 34;