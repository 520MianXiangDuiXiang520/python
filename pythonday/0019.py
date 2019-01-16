import itchat
import time


@itchat.msg_register(itchat.content.TEXT)
def reply_msg(msg):
    print("收到一条信息：", msg.text)


def get_info():
    wechatid = input("请输入你要轰炸的微信号: ")
    body = input("请输入你要轰炸的文字：")
    num = input("输入轰炸次数，建议不要太多，会被封号: ")
    for i in range(int(num)):
        itchat.send(body, toUserName=wechatid)
    itchat.run()
    chose = input("轰炸完成，您要退出（N）还是重新开始（Y）：")
    if (chose == "Y"):
        get_info()
    elif chose == "N":
        exit(1)
    else:
        chose = input("输入有误，重新输入： ")


def get_friend():
    friendList = itchat.get_friends()
    No = 0
    # print(friendList[0])
    for friend in friendList:
        # 如果是演示目的，把下面的方法改为print即可
        sex = friend["Sex"]
        if sex == 1:
            性别 = "男"
        elif sex == 0:
            性别 = "女"
        else:
            性别 = "其他"
        # print(repr(No),friend["NickName"],性别,friend["Signature"])
        print(f'{repr(No): ^10}{friend["NickName"]: ^10}{性别: ^10}{friend["Signature"]: ^20}{friend["City"]: ^20}')
        No += 1
        # print("jjj" % (friend['DisplayName']or friend['NickName']), friend['UserName'])
        time.sleep(.5)


def get_chatroom():
    chatroom_list = itchat.get_chatrooms()
    for room in chatroom_list:
        print(room["NickName"])


def get_mps():
    mps_list = itchat.get_mps()
    No = 0
    for mps in mps_list:
        sex = mps["Sex"]
        if sex == 1:
            性别 = "男"
        elif sex == 0:
            性别 = "女"
        else:
            性别 = "其他"
        print(f'{repr(No): ^10}{mps["NickName"]: ^10}{性别: ^10}{mps["City"]: ^10}{mps["Signature"]: ^50}')
        No += 1


def list():
    print("------ 1. 微信轰炸 -------")
    print("------ 2. 好友列表 -------")
    print("------ 3. 群聊列表 -------")
    print("------ 4. 公众号列表 -------")
    chose = input("请输入你要进行的操作： ")
    if chose == '1':
        get_info()
    elif chose == '2':
        get_friend()
    elif chose == '3':
        get_chatroom()
    elif chose == '4':
        get_mps()
    else:
        print("输入有误！！")
        exit(1)


if __name__ == '__main__':
    itchat.auto_login(hotReload=True)
    time.sleep(5)
    # get_info()
    # get_friend()
    # get_chatroom()
    # get_mps()
    list()

