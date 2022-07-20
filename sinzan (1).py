from colorama import Fore, Back , Style, init
for num in range(1 , 9):
	print(Fore.RED+"+" * num)
for num in range(9 , 1 , -1):
	print(Fore.GREEN+"×" * num)
from rubika.client import Bot
from rubika.tools import Tools
from rubika.encryption import encryption
import random
from random import choice
pa = input(Fore.YELLOW+"pleas inter file password : ")
while pa != "@ilumeme":
	print(Fore.RED+"password is false")
	pa = input(Fore.CYAN+"your password is false pleas inter true password : ")
target = input(Fore.GREEN+"pleas inter gap Guid : ")
answered,retries = [],{}
bot = Bot("AppName", auth= input(Fore.MAGENTA+"pleas inter your account auth : "))

while True:
	try:
		admins = [i["member_guid"] for i in bot.getGroupAdmins(target)["data"]["in_chat_members"]]
		min_id = bot.getGroupInfo(target)["data"]["chat"]["last_message_id"]
		while True:
			try:
				messages = bot.getMessages(target,min_id)
				break
			except:
				continue

		for msg in messages:
			try:
				if msg["type"]=="Text" and not msg.get("message_id") in answered:
					if msg.get("text").startswith("دستورات"):
							try:
								bot.sendMessage(target, "سلام به ربات سین زن امیر بات خوش امدید \n برای اریال لینک خود کلمه\n  سین زن فعال را ارسال کنید")
							except:
								print("error ersal start1")
					if msg.get("text").startswith("سین زن فعال"):
							try:
								bot.sendMessage(target, "دوست عزیز در پیام بعدی خود کلمه گپ ها را ارسال کرده و لینک هایی که میخاهید ربات در انها سین بزند را ارسال کنید توجه کنید که تایمر روی ربات اثر ندارد \n برای مثال \n گپ ها \n         https://rubika.ir/jdjdhdjdjdhdhdjdhdbdhdj \n https://rubika.ir/ehjdhdhdjwjdbfksbsixbsjshdej")
							except:
								print("error ersal start1")

					elif msg.get("text").startswith("گپ ها"):
							try:
								matnsingzf = open("banerlinkdoneSINZAN.txt","w",encoding='utf-8').write(str(msg.get("text").strip("جوین گروه")))
								matnsingz = open("banerlinkdoneSINZAN.txt").read().split("\n")
								bot.sendMessage(target,  "لینک شما ثبت شد برای شروع سین زنی روی بنر خود ریپلای کنید و کلمه سین رو ارسال کنید")
							
							except:
								print("error sabt_link-sinzan")

					elif msg.get("text").startswith("سین بزن"):
						while True:
							matntabb = list(matnsingz)
							randomli = choice(matntabb)
							writelin = open("TARGET_SINZAN.txt","w",encoding='utf-8').write(str(randomli))
							tabgligh = open("TARGET_SINZAN.txt","r",encoding='utf-8').read()
							tabeligh = bot.joinGroup(tabgligh)
							tabrligh = tabeligh['data']['group']['group_guid']
							bot.forwardMessages(target,[msg.get("reply_to_message_id")],tabrligh)
							bot.leaveGroup(tabrligh)

			except:
				continue
			answered.append(msg.get("message_id"))
			

	except KeyboardInterrupt:
		exit()

	except Exception as e:
		if type(e) in list(retries.keys()):
			if retries[type(e)] < 3:
				retries[type(e)] += 1
				continue
			else:
				retries.pop(type(e))
		else:
			retries[type(e)] = 1
			continue
