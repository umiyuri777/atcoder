"""
行ごとに日時がyyyy-MM-dd HH:mm:ss の形式で入力されます。

入力された日付を日本標準時間（JST）として、これを協定世界時（UTC）に変換した上で、以下の2つの日付をyyyy-MM-dd/yyyy-MM-dd の形式で出力してください。

入力された日付より5日以上過去にある中で最も近い平日（月曜〜金曜）の日付
入力された日付より5日以上未来にある中で最も近い平日（月曜〜金曜）の日付
入力の先頭行には、その後に何行の入力が続くかが自然数で書いてあります。

ヒント：日本標準時間（JST）は、協定世界時（UTC）より9時間進んでいます。
2000-01-01 00:00:00 (UTC) は、2000-01-01 09:00:00 (JST) と同じ時刻を示します。

入力サンプル
3
2000-01-26 12:00:00
2000-01-25 00:00:00
2000-01-27 09:00:00

出力サンプル
2000-01-21/2000-01-31
2000-01-19/2000-01-31
2000-01-21/2000-02-01

"""


# Python 3.13.0

import datetime

# 最も近い平日を探す関数
def search_weekday(target_day, direction):
    for idx in range(3):
        ans = target_day - datetime.timedelta(days = (5 + idx) * direction)
        if ans.weekday() < 5:
            return ans

N = int(input())
date_and_time = [input() for _ in range(N)]

utc_dt = []

# JST →　UTCへの変換
for dt in date_and_time:
    utc_dt.append(datetime.datetime.strptime(dt, "%Y-%m-%d %H:%M:%S") - datetime.timedelta(hours = 9))

ans = []
for u in utc_dt:
    before_day = search_weekday(u, -1)
    after_day = search_weekday(u, 1)
    ans.append("/".join((str(after_day.date()), str(before_day.date()))))

for a in ans:
    print(a)