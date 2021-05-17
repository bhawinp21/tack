import constants as keys
from telegram.ext import *
import requests, json
import time
print('Bot is starting')

def start_command(update, context):
	update.message.reply_text('Yo, welcome to this bot')

def vaccine_command(update, context):
	a =5
	while a>0:
		time.sleep(1500)
		while a >0:
				a=a+1
				time.sleep(3)
				pin='311301'
				date='17-05-2021'
				url = f'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={pin}&date={date}'
				browser_header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
				print(url)
				response = requests.get(url, headers=browser_header)
				print(response)
				json_data = response.json()
				final_text = ''
				if len(json_data['sessions'])==0:
					print("\nSlots Not Available\n")
					continue
				else:
					for slots in json_data['sessions']:
						final_text = final_text + "\nName: "+str(slots['name']) +'\n'+ "Available Capacity: "+str(slots['available_capacity']) +'\n' + "Min Age Limit: "+str(slots['min_age_limit']) +'\n' + "Vaccine: "+str(slots['vaccine'])+ '\n'
						final_text = final_text + '----------------------------------------'
						update.message.reply_text(final_text)
					break






def main():
	updater = Updater(keys.API_KEY, use_context=True)
	dp = updater.dispatcher

	dp.add_handler(CommandHandler("start", start_command))
	#dp.add_handler(CommandHandler("help", help_command))
	dp.add_handler(CommandHandler("v", vaccine_command))

	


	updater.start_polling()
	updater.idle()

main()