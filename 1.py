# -*- coding: utf-8 -*-
from linepy import *
from datetime import datetime
from bs4 import BeautifulSoup
from threading import Thread
from googletrans import Translator
from gtts import gTTS
from time import strftime
import time,random,sys,json,codecs,threading,glob,urllib,urllib3,re,ast,os,subprocess,requests,tempfile,html5lib,wikipedia,goslate,profile,client,timeit
client = LineClient()
#client = LineClient(id='top511324@gmail.com', passwd='zaswdc12')
#client = LineClient(authToken='')
client.log("Auth Token : " + str(client.authToken))

channel = LineChannel(client)
client.log("Channel Access Token : " + str(channel.channelAccessToken))
cl = client
poll = LinePoll(client)
HelpMessagelist="""
"""
KAC=[cl]
mid = cl.getProfile().mid
Bots=[mid]
admin=["u2b37602c4f9f8d54917de47b09749130","u64fd0e930e2133c26491c4409e28af03",mid]
owner=["u2b37602c4f9f8d54917de47b09749130","u64fd0e930e2133c26491c4409e28af03",mid]
whitelist=["u2b37602c4f9f8d54917de47b09749130","u64fd0e930e2133c26491c4409e28af03",mid]
wait = {
    'contact':True,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':True,
    'message':"""
        """,
    "lang":"JP",
    "comment":"",
    "commentOn":True,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "blacklist":{},
    "Protectgr":False,
    "protectionOn":False,
    "atjointicket":True
}
wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
}
mulai = time.time()
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
def yt(query):
    with requests.session() as s:
        isi = []
        if query == "":
            query = "S1B tanysyz"
        s.headers['user-agent'] = 'Mozilla/5.0'
        url    = 'http://www.youtube.com/results'
        params = {'search_query': query}
        r    = s.get(url, params=params)
        soup = BeautifulSoup(r.content, 'html5lib')
        for a in soup.select('.yt-lockup-title > a[title]'):
            if '&list=' not in a['href']:
                if 'watch?v' in a['href']:
                    b = a['href'].replace('watch?v=', '')
                    isi += ['youtu.be' + b]
        return isi
def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours,24)
    return '%02d 天 %02d 小時 %02d 分 %02d 秒' % (days, hours, mins, secs)
def mention(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
        akh = akh + 2
        aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
        strt = strt + 6
        akh = akh + 4
        bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print ("[Command] TagAll")
    try:
        cl.sendMessage(msg)
    except Exception as error:
        print ("error")
def tagall(to,nama):
    aa = ""
    bb = ""
    strt = int(12)
    akh = int(12)
    nm = nama
    for mm in nm:
        akh = akh + 2
        aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
        strt = strt + 6
        akh = akh + 4
        bb += "• @c \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "「Mention」\n"+bb
    msg.contentMetadata = {'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    try:
        cl.sendMessage(msg)
    except Exception as error:
        print (error)
def sendImageWithURL(self, to_, url):
    path = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        with open(path, 'w') as f:
            shutil.copyfileobj(r.raw, f)
    else:
        raise Exception('Download image failure.')
    try:
        self.sendImage(to_, path)
    except Exception as e:
        raise e
while True:
  try:
    ops=poll.singleTrace(count=50)
    if ops != None:
      for op in ops:
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))
        if op.type == 13:
            if mid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots or owner:
                  cl.acceptGroupInvitation(op.param1)
                else:
                  cl.rejectGroupInvitation(op.param1)
              else:
                print ("自動進群關閉")
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 26:
          msg = op.message
          msg.from_ = msg._from
          sender = msg._from
          receiver = msg.to
          if sender in admin:
            if msg.contentType == 13:
               if wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[顯示名稱]:\n" + msg.contentMetadata["顯示名稱"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[狀態消息]:\n" + contact.statusMessage + "\n[圖片網址]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[封面網址]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[顯示名稱]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[狀態消息]:\n" + contact.statusMessage + "\n[圖片網址]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[封面網址]:\n" + str(cu))
            elif msg.text in ['Help',"指令","幫助"]:
                cl.sendText(msg.to,HelpMessagelist)
                cl.sendText(msg.to,HelpMessage01)
                cl.sendText(msg.to,HelpMessage02)
                cl.sendText(msg.to,HelpMessage03)
                cl.sendText(msg.to,HelpMessage04)
            elif 'spic' in msg.text.lower():
                try:
                    key = eval(msg.contentMetadata["MENTION"])
                    u = key["MENTIONEES"][0]["M"]
                    a = client.getContact(u).pictureStatus
                    client.sendImageWithURL(receiver, 'http://dl.profile.line.naver.jp/'+a)
                except Exception as e:
                    client.sendText(receiver, str(e))
            elif 'scover' in msg.text.lower():
                try:
                    key = eval(msg.contentMetadata["MENTION"])
                    u = key["MENTIONEES"][0]["M"]
                    a = channel.getProfileCoverURL(mid=u)
                    client.sendImageWithURL(receiver, a)
                except Exception as e:
                    client.sendText(receiver, str(e))
            elif "Gc" in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    key = eval(msg.contentMetadata["MENTION"])
                    u = key["MENTIONEES"][0]["M"]
                    contact = cl.getContact(u)
                    cu = channel.getProfileCoverURL(mid=u)
                    try:
                        random.choice(KAC).sendText(msg.to,"名字:\n" + contact.displayName + "\n\n系統識別碼:\n" + contact.mid + "\n\n個性簽名:\n" + contact.statusMessage + "\n\n頭貼網址 :\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\n封面網址 :\n" + str(cu))
                    except:
                        random.choice(KAC).sendText(msg.to,"名字:\n" + contact.displayName + "\n\n系統識別碼:\n" + contact.mid + "\n\n個性簽名:\n" + contact.statusMessage + "\n\n封面網址:\n" + str(cu))
            elif ("Gn " in msg.text):
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Gn ","")
                    cl.updateGroup(X)
                else:
                    cl.sendText(msg.to,"無法使用在群組外")
            elif "Uk " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("Uk ","")
                random.choice(KAC).kickoutFromGroup(msg.to,[midd])
            elif "Ri " in msg.text:
              if msg.from_ in admin:
                Ri0 = msg.text.replace("Ri ","")
                Ri1 = Ri0.rstrip()
                Ri2 = Ri1.replace("@","")
                Ri3 = Ri2.rstrip()
                _name = Ri3
                gs = cl.getGroup(msg.to)
                targets = []
                for s in gs.members:
                    if _name in s.displayName:
                        targets.append(s.mid)
                if targets == []:
                    pass
                else:
                    for target in targets:
                        try:
                            cl.kickoutFromGroup(msg.to,[target])
                            cl.findAndAddContactsByMid(target)
                            cl.inviteIntoGroup(msg.to,[target])
                        except:
                            pass
            elif "Tk " in msg.text:
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                    try:
                        cl.kickoutFromGroup(msg.to,[target])
                    except:
                        pass
            elif "Mk " in msg.text:
              if msg.from_ in admin:
                Mk0 = msg.text.replace("Mk ","")
                Mk1 = Mk0.rstrip()
                Mk2 = Mk1.replace("@","")
                Mk3 = Mk2.rstrip()
                _name = Mk3
                gs = cl.getGroup(msg.to)
                targets = []
                for s in gs.members:
                    if _name in s.displayName:
                        targets.append(s.mid)
                if targets == []:
                    pass
                else:
                    for target in targets:
                        try:
                            cl.kickoutFromGroup(msg.to,[target])
                        except:
                            pass
            elif "Nk " in msg.text:
              if msg.from_ in admin:
                _name = msg.text.replace("Nk ","")
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _name in g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    pass
                else:
                    for target in targets:
                        try:
                            cl.kickoutFromGroup(msg.to,[target])
                        except:
                            pass
            elif "Inv " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("Inv ","")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to,[midd])
            elif msg.text in ["Me"]:
                random.choice(KAC).sendMessage(msg.to, None, contentMetadata={'mid': sender}, contentType=13)
            elif msg.text.lower() == 'time':
                times= time.strftime("%Y/%m/%d/ %X %a", time.localtime())
                cl.sendText(msg.to, times)
            elif msg.text in ["Ourl",]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = random.choice(KAC).getGroup(msg.to)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    random.choice(KAC).sendText(msg.to,"群組邀請已開啟")
                else:
                    random.choice(KAC).sendText(msg.to,"無法在群組外使用")
            elif msg.text in ["Curl"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = random.choice(KAC).getGroup(msg.to)
                    X.preventJoinByTicket = True
                    random.choice(KAC).updateGroup(X)
                    random.choice(KAC).sendText(msg.to,"群組邀請已關閉")
                else:
                    random.choice(KAC).sendText(msg.to,"無法在群組外使用")
            elif msg.text.lower() == 'ginfo':
              if msg.toType == 2:
                if msg.from_ in admin:
                  ginfo = cl.getGroup(msg.to)
                  try:
                    gCreator = ginfo.creator.displayName
                  except:
                    gCreator = "錯誤"
                  if wait["lang"] == "JP":
                    if ginfo.invitee is None:
                      sinvitee = "0"
                    else:
                      sinvitee = str(len(ginfo.invitee))
                      #if ginfo.preventJoinByTicket == True:
                      #QR = "關閉"
                      #else:
                      #QR = "開啟"
                      # random.choice(KAC).sendText(msg.to,"[群組名稱]\n" + "[☆]" + str(ginfo.name) + "\n\n[群組ID]\n" + msg.to + "\n\n[群組創建者]\n" + "[☆]" + gCreator + "\n\n[群組狀態]\n" + "[☆]群組網址 =>" + QR + "\n\n[群組圖片]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n\n群組成員數:" + str(len(ginfo.members)) + "\n群組邀請人數:" + sinvitee)
                    random.choice(KAC).sendText(msg.to,"[群組名稱]\n" + "[☆]" + str(ginfo.name) + "\n\n[群組ID]\n" + msg.to + "\n\n[群組創建者]\n" + "[☆]" + gCreator + "\n\n[群組狀態]\n" + "\n\n[群組圖片]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n\n群組成員數:" + str(len(ginfo.members)) + "\n群組邀請人數:" + sinvitee)
                  else:
                    random.choice(KAC).sendText(msg.to,"[群組名稱]\n" + str(ginfo.name) + "\n\n[群組ID]\n" + msg.to + "\n\n[群組創建者]\n" + gCreator + "\n\n[群組狀態]\n[群組圖片]:\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
            elif msg.text.lower() == 'mid':
                random.choice(KAC).sendText(msg.to, msg.from_)
            elif msg.text in ["Contact On","Contact on","contact on"]:
                if wait["contact"] == True:
                    cl.sendText(msg.to,"查看好友資料詳情開啟")
                else:
                    wait["contact"] = True
                    cl.sendText(msg.to,"已經開啟了")
            elif msg.text in ["Contact Off","Contact off","contact off"]:
                if wait["contact"] == False:
                    cl.sendText(msg.to,"查看好友資料詳情關閉")
                else:
                    wait["contact"] = False
                    cl.sendText(msg.to,"已經關閉了")
            elif msg.text in ["Join on","Auto join on"]:
                if wait["autoJoin"] == True:
                    cl.sendText(msg.to,"自動加入已開啟")
                else:
                    wait["autoJoin"] = True
                    cl.sendText(msg.to,"已經開啟了")
            elif msg.text in ["Join off","Auto join off"]:
                if wait["autoJoin"] == False:
                    cl.sendText(msg.to,"自動加入已關閉")
                else:
                    wait["autoJoin"] = False
                    cl.sendText(msg.to,"已經關閉了")
            elif msg.text in ["Leave on","Auto leave:on"]:
                if wait["leaveRoom"] == True:
                    cl.sendText(msg.to,"自動離開副本開啟")
                else:
                    wait["leaveRoom"] = True
                    cl.sendText(msg.to,"已經開啟了")
            elif msg.text in ["Leave off","Auto leave:off"]:
                if wait["leaveRoom"] == False:
                    cl.sendText(msg.to,"自動離開副本關閉")
                else:
                    wait["leaveRoom"] = False
                    cl.sendText(msg.to,"已經關閉了")
            elif msg.text in ["Share on","Share on"]:
                if wait["timeline"] == True:
                    cl.sendText(msg.to,"檢視文章詳情開啟")
                else:
                    wait["timeline"] = True
                    cl.sendText(msg.to,"已經開啟了")
            elif msg.text in ["Share off","Share off"]:
                if wait["timeline"] == False:
                    cl.sendText(msg.to,"檢視文章詳情關閉")
                else:
                    wait["timeline"] = False
                    cl.sendText(msg.to,"已經關閉了")
            elif msg.text in ["Status","Set","Set:test"]:
              if msg.from_ in admin:
                md = "⭐個人狀態⭐\n*==================*\n"
                if wait["contact"] == True: md+="[•]好友資料詳情 [開啟]\n"
                else: md+="[•]好友資料詳情 [關閉]\n"
                if wait["autoJoin"] == True: md+="[•]自動加入 [開啟]\n"
                else: md +="[•]自動加入 [關閉]\n"
                if wait["leaveRoom"] == True: md+="[•]自動離開副本 [開啟]\n"
                else: md+="[•]自動離開副本 [關閉]\n"
                if wait["timeline"] == True: md+="[•]文章詳情 [開啟]\n"
                else:md+="[•]文章詳情 [關閉]\n"
                if wait["autoAdd"] == True: md+="[•]好友自動添加 [開啟]\n"
                else:md+="[•]好友自動添加 [關閉]\n"
                cl.sendText(msg.to,md)
            elif msg.text in ["Add on","Auto add:on"]:
                if wait["autoAdd"] == True:
                    cl.sendText(msg.to,"好友自動加入開啟")
                else:
                    wait["autoAdd"] = True
                    cl.sendText(msg.to,"已經開啟了")
            elif msg.text in ["Add off","Auto add:off"]:
                if wait["autoAdd"] == True:
                    cl.sendText(msg.to,"好友自動加入關閉")
                else:
                    wait["autoAdd"] = False
                    cl.sendText(msg.to,"已經關閉了")
            elif msg.text.lower() == 'tagall':
                group = client.getGroup(receiver)
                nama = [contact.mid for contact in group.members]
                nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                if jml <= 100:
                    client.mention(receiver, nama)
                if jml > 100 and jml < 200:
                    for i in range(0, 100):
                        nm1 += [nama[i]]
                    client.mention(receiver, nm1)
                    for j in range(101, len(nama)):
                        nm2 += [nama[j]]
                    client.mention(receiver, nm2)
                if jml > 200 and jml < 300:
                    for i in range(0, 100):
                        nm1 += [nama[i]]
                    client.mention(receiver, nm1)
                    for j in range(101, 200):
                        nm2 += [nama[j]]
                    client.mention(receiver, nm2)
                    for k in range(201, len(nama)):
                        nm3 += [nama[k]]
                    client.mention(receiver, nm3)
                if jml > 300 and jml < 400:
                    for i in range(0, 100):
                        nm1 += [nama[i]]
                    client.mention(receiver, nm1)
                    for j in range(101, 200):
                        nm2 += [nama[j]]
                    client.mention(receiver, nm2)
                    for k in range(201, len(nama)):
                        nm3 += [nama[k]]
                    client.mention(receiver, nm3)
                    for l in range(301, len(nama)):
                        nm4 += [nama[l]]
                    client.mention(receiver, nm4)
                if jml > 400 and jml < 501:
                    for i in range(0, 100):
                        nm1 += [nama[i]]
                    client.mention(receiver, nm1)
                    for j in range(101, 200):
                        nm2 += [nama[j]]
                    client.mention(receiver, nm2)
                    for k in range(201, len(nama)):
                        nm3 += [nama[k]]
                    client.mention(receiver, nm3)
                    for l in range(301, len(nama)):
                        nm4 += [nama[l]]
                    client.mention(receiver, nm4)
                    for m in range(401, len(nama)):
                        nm5 += [nama[m]]
                    client.mention(receiver, nm5)
                client.sendText(receiver, "成員數 :"+str(jml))
            elif "Ban @" in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    print ("[Ban] 成功")
                    _name = msg.text.replace("Ban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                random.choice(KAC).sendText(msg.to,"已加入黑名單")
                            except:
                                random.choice(KAC).sendText(msg.to,"錯誤")
            elif "Mid @" in msg.text:
              if msg.from_ in owner:
                _name = msg.text.replace("Mid @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        random.choice(KAC).sendText(msg.to, g.mid)
                    else:
                        pass
                            # elif "Mc " in msg.text:
                            #  mmid = msg.text.replace("Mc ","")
                            # random.choice(KAC).sendMessage(receiver, None, contentMetadata={'mid': mmid}, contentType=13)
                            #print ("mid查看友資執行")
            elif "Vk:" in msg.text:
                if msg.from_ in owner:
                    midd = msg.text.replace("Vk:","")
                    cl.kickoutFromGroup(msg.to,[midd])
                    cl.findAndAddContactsByMid(midd)
                    cl.inviteIntoGroup(msg.to,[midd])
                    cl.cancelGroupInvitation(msg.to,[midd])
            elif "Vk " in msg.text:
                if msg.from_ in owner:
                    vkick0 = msg.text.replace("Vk ","")
                    vkick1 = vkick0.rstrip()
                    vkick2 = vkick1.replace("@","")
                    vkick3 = vkick2.rstrip()
                    _name = vkick3
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for s in gs.members:
                            if _name in s.displayName:
                                    targets.append(s.mid)
                    if targets == []:
                            sendMessage(msg.to,"用戶不存在")
                            pass
                    else:
                            for target in targets:
                                    try:
                                            cl.kickoutFromGroup(msg.to,[target])
                                            cl.findAndAddContactsByMid(target)
                                            cl.inviteIntoGroup(msg.to,[target])
                                            cl.cancelGroupInvitation(msg.to,[target])
                                    except:
                                            pass
            elif "Unban @" in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    print ("已解除黑名單")
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"沒有黑名單")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"帳號已解鎖")
                            except:
                                cl.sendText(msg.to,"錯誤")
            elif "Fbc:" in msg.text:
               bctxt = msg.text.replace("Fbc:","")
               t = cl.getAllContactIds()
               if msg.from_ in owner:
                   for manusia in t:
                       cl.sendText(manusia,(bctxt))
               else:
                   cl.sendText(msg.to,"你不是管理員")
            elif "Gbc:" in msg.text:
                bctxt = msg.text.replace("Gbc:","")
                n = cl.getGroupIdsJoined()
                if msg.from_ in owner:
                    for manusia in n:
                        cl.sendText(manusia,(bctxt))
                else:
                    cl.sendText(msg.to,"你不是管理員")
            elif msg.text.lower() == 'rebot':
                print ("======重新啟動=====")
                cl.sendText(msg.to, "重新啟動")
                restart_program()
            elif msg.text.lower() == 'runtime':
                eltime = time.time() - mulai
                van = "機器運行時間 :\n"+waktu(eltime)
                cl.sendText(msg.to,van)
            elif msg.text in ["sp","Sp","Speed","speed"]:
                start = time.time()
                time0 = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
                elapsed_time = time.time() - start
                str1 = str(time0)
                cl.sendText(msg.to, '處理速度\n' + str1 + '秒')
                cl.sendText(msg.to, "指令反應: %s秒" % (elapsed_time))
            elif msg.text in ["Ban"]:
              if msg.from_ in owner:
                wait["wblacklist"] = True
                cl.sendText(msg.to,"請丟出好友資料")
            elif msg.text in ["Unban"]:
              if msg.from_ in owner:
                wait["dblacklist"] = True
                cl.sendText(msg.to,"請丟出好友資料")
            elif msg.text in ["Creator"]:
              cl.sendMessage(receiver, None, contentMetadata={'mid': 'u2b37602c4f9f8d54917de47b09749130'}, contentType=13)
            elif msg.text in ["Banlist"]:
              if msg.from_ in admin:
                if wait["blacklist"] == {}:
                    random.choice(KAC).sendText(msg.to,"沒有黑名單")
                else:
                    random.choice(KAC).sendText(msg.to,"以下是黑名單")
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
            elif msg.text in ["Ban mid"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    cocoa = ""
                    for mm in matched_list:
                        cocoa += mm + "\n"
                    random.choice(KAC).sendText(msg.to,cocoa + "")
            elif msg.text in ["Kill ban"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        random.choice(KAC).sendText(msg.to,"沒有黑名單")
                        pass
                    for jj in matched_list:
                        random.choice(KAC).kickoutFromGroup(msg.to,[jj])
                        random.choice(KAC).kickoutFromGroup(msg.to,[jj])
                        random.choice(KAC).kickoutFromGroup(msg.to,[jj])
                        random.choice(KAC).kickoutFromGroup(msg.to,[jj])
                    random.choice(KAC).sendText(msg.to,"黑名單以踢除")
            if msg.text in ["c","C","cancel","Cancel"]:
              if msg.from_ in owner:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = (contact.mid for contact in X.invitee)
                        ginfo = cl.getGroup(msg.to)
                        sinvitee = str(len(ginfo.invitee))
                        start = time.time()
                        for cancelmod in gInviMids:
                            cl.cancelGroupInvitation(msg.to, [cancelmod])
                        elapsed_time = time.time() - start
                        cl.sendText(msg.to, "已取消完成\n取消時間: %s秒" % (elapsed_time))
                        cl.sendText(msg.to, "取消人數:" + sinvitee)
                    else:
                        cl.sendText(msg.to, "沒有任何人在邀請中！！")
            if msg.text in ["110"]:
              if msg.from_ in owner:
                    cl.sendText(msg.to,"1")
                    cl.sendText(msg.to,"2")
                    cl.sendText(msg.to,"3")
                    cl.sendText(msg.to,"4")
                    cl.sendText(msg.to,"5")
                    cl.sendText(msg.to,"6")
                    cl.sendText(msg.to,"7")
                    cl.sendText(msg.to,"8")
                    cl.sendText(msg.to,"9")
                    cl.sendText(msg.to,"10")
        if op.type == 55:
          try:
            if op.param1 in wait2['readPoint']:
              Name = cl.getContact(op.param2).displayName
              if Name in wait2['readMember'][op.param1]:
                 pass
              else:
                wait2['readMember'][op.param1] += "\n[•]" + Name
                wait2['ROM'][op.param1][op.param2] = "[•]" + Name
                print (time.time() + name)
            else:
              cl.sendText
          except:
             pass
        elif op.type == 55:
            try:
                if cctv['cyduk'][op.param1]==True:
                    if op.param1 in cctv['point']:
                        Name = cl.getContact(op.param2).displayName
                        if Name in cctv['sidermem'][op.param1]:
                            pass
                        else:
                            cctv['sidermem'][op.param1] += "\n~ " + Name
                            print (time.time() + Name)
                    else:
                        pass
                else:
                    pass
            except:
                pass
        if op.type == 59:
            print (op)
        poll.setRevision(op.revision)
  except Exception as e:
      client.log("[SINGLE_TRACE] ERROR : " + str(e))

