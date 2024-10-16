import requests
import json
import time
import winsound
ids = [50139,21748]
print('小电驴查询 by shy & ghr')

def read_file():
    path = r"Info.txt"
    file = {}
    try:
        with open(path, "r") as f:
            info = f.read()
        # print(info.split("\n"))
        for item in info.split("\n"):
            file[item.split(":")[0]] = item.split(":")[1]
        return file
    except():
        return -1


def border(font):
    if font == 2:
        print("==================================================================")
    elif font == 1:
        print("——————————————————————————————————————————————————————————————————")


def jiao():
    type = read_file()['jiao']
    if type == '1':
        winsound.MessageBeep(winsound.MB_ICONHAND)
    if type == '2':
        winsound.MessageBeep(winsound.MB_OK)
    if type == '3':
        winsound.MessageBeep(winsound.MB_ICONEXCLAMATION)
    if type == "0":
        """额"""


def list(stationids):
    print(f"充电站名称\t插座编号\t  状态\t    电话   \t   插座编号")
    for stationid in stationids:
        if stationid == 50139:
            station_name = "新世纪17栋"
        elif stationid == 21748:
            station_name = "新世纪驿站"
        else:
            station_name = str(stationid)
        response = requests.get(f'https://api.issks.com/issksapi/V2/ec/chargingList.shtml?stationId={stationid}')
        data = json.loads(response.text)
        border(1)
        for outlet in data["list"]:
            if outlet['vLastMobile'] == "":
                tel = "-----------"
            else:
                tel = outlet['vLastMobile']

            if outlet["status"] == 1 :
                status = '可用'
                jiao()
            else:
                status = '不可用'
            print(f"{station_name}\t{outlet['vOutletName']}\t\t{status}\t{tel}\t{outlet['vOutletNo']}")
            
            with open(r"log.csv", "a") as f:
                f.write(f'''{stationid},{time.strftime("%Y/%m/%d,%H:%M:%S")},{outlet['vOutletName']},{outlet["status"]},{status},'{tel}',{outlet['vOutletNo']},\n''')



with open(r"Info.txt", "r") as f:
    print(f.read())
sleep_time = float(read_file()['sleeptime'])
jiao()
border(1)
while 1:
    list(ids)

    border(1)

    flg = False
    print(f"省流助手：\n")
    for stationid in ids:
        if stationid == 50139:
            station_name = "新世纪17栋"
        elif stationid == 21748:
            station_name = "新世纪驿站"
        else:
            station_name = str(stationid)

        response = requests.get(f'https://api.issks.com/issksapi/V2/ec/chargingList.shtml?stationId={stationid}')
        data = json.loads(response.text)

        for outlet in data["list"]:
            if outlet["status"] == 1 :
                print(f"{station_name}\t{outlet['iOutletSerialNo']}")
                flg = True
    if not flg:
        print("再等等")
    border(1)

    print("")
    time.sleep(sleep_time)
