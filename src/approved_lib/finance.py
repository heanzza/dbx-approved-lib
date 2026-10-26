from datetime import date

_ERAS = [
    (date(2019, 5, 1), "令和"),
    (date(1989, 1, 8), "平成"),
    (date(1926, 12, 25), "昭和"),
]


def to_wareki(d: date) -> str:
    """西暦の日付を和暦文字列に変換する。"""
    for start, name in _ERAS:
        if d >= start:
            n = d.year - start.year + 1
            return f"{name}{'元' if n == 1 else n}年{d.month}月{d.day}日"
    raise ValueError("昭和より前は未対応")


def yen(amount: float) -> str:
    """金額を円表記にする。"""
    return f"¥{amount:,.0f}"
