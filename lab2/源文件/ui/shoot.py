import subprocess
import sys
from pathlib import Path

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
UI = Path(r"D:\软工实验\_lab2_build\ui")
OUT = UI / "shots"
OUT.mkdir(exist_ok=True)

PAGES = [
    ("c1_shop.html", "顾客-01_店铺与菜品筛选", 390, 844),
    ("c2_spec.html", "顾客-02_规格选择", 390, 844),
    ("c3_cart.html", "顾客-03_购物车", 390, 844),
    ("c4_order.html", "顾客-04_确认订单", 390, 844),
    ("c5_paid.html", "顾客-05_支付结果", 390, 844),
    ("c6_orders.html", "顾客-06_订单列表", 390, 844),
    ("c7_order_detail.html", "顾客-07_订单详情", 390, 844),
    ("c8_address.html", "顾客-08_收货地址", 390, 844),
    ("m1_workbench.html", "商家-01_接单工作台", 390, 844),
    ("m1b_reject.html", "商家-02_拒单原因", 390, 844),
    ("m2_menu.html", "商家-03_菜品与规格管理", 390, 844),
    ("m3_stats.html", "商家-04_经营统计", 390, 844),
    ("d1_pool.html", "配送-01_抢单池", 390, 844),
    ("d2_delivery.html", "配送-02_配送执行", 390, 844),
    ("a1_admin.html", "平台-01_数据总览", 1440, 900),
    ("a2_audit.html", "平台-02_日志审计", 1440, 900),
]

only = sys.argv[1:] or None

for fname, name, w, h in PAGES:
    if only and fname not in only:
        continue
    url = (UI / fname).as_uri()
    png = OUT / (name + ".png")
    cmd = [
        CHROME, "--headless=new", "--disable-gpu", "--no-sandbox",
        "--hide-scrollbars", "--force-device-scale-factor=2",
        "--window-size=%d,%d" % (w, h),
        "--screenshot=" + str(png), url,
    ]
    r = subprocess.run(cmd, capture_output=True)
    ok = png.exists()
    print(("OK   " if ok else "FAIL ") + name + "  " + (str(png.stat().st_size) + "B" if ok else ""))
    if not ok:
        print(r.stderr.decode("utf-8", "ignore")[-400:])
