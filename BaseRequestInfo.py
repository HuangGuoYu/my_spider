
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3080.5 Safari/537.36'
}
cookie = "ASP.NET_SessionId=ajyypvwse0d4rux2kf0egrhg; gr_user_id=8a94c2ee-91cb-4bf0-a8a8-6f0902a00bea; UM_distinctid=16069bc2f8776e-0920bfa566e47c-18117450-1fa400-16069bc2f88756; Youzy.FirstSelectVersion=1; Uzy.AUTH=5F1321177E8C32758EB0AEB626029F3D79A98A419F2822BE4C16AB20EF7759F7A488A94EB59B94A1428455417276CA00F2E8A089AADFB2DEA63A0069A41F662912B2F9D99FE348B10B33F33EF99633FC6F03FFF7877B4BF8CEC32AE2D450CDF85DCCE13A655E70CDD0AF2A22F33F0F95CAAF268A; Youzy.CurrentVersion=%7b%22Name%22%3a%22%e8%be%bd%e5%ae%81%22%2c%22EnName%22%3a%22ln%22%2c%22ProvinceId%22%3a839%2c%22Domain%22%3a%22http%3a%2f%2fln.youzy.cn%22%2c%22Description%22%3a%22%22%2c%22QQGroup%22%3a%22%22%2c%22QQGroupUrl%22%3anull%2c%22IsOpen%22%3atrue%2c%22Sort%22%3a27%2c%22Province%22%3a%7b%22Name%22%3a%22%e8%be%bd%e5%ae%81%22%2c%22Id%22%3a839%7d%2c%22Id%22%3a30%7d; SERVER_ID=17777dd5-3a24a800; CNZZDATA1254568697=760543240-1513599279-null%7C1513604871; Hm_lvt_12d15b68f4801f6d65dceb17ee817e26=1513602430; Hm_lpvt_12d15b68f4801f6d65dceb17ee817e26=1513605276; gr_session_id_943f0f1daad3348b=fafa5a78-e872-4059-b7d9-5d784160fe5c"
cookies = {}
#处理cookie信息
for item in cookie.split(";"):
    result = item.split("=", 1)
    key = result[0]
    value = result[1]
    cookies[key] = value


