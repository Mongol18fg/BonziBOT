import telebot

bot = telebot.TeleBot('7634811055:AAGLWknySQ9UKuO6KPhaHKWFMp_UGAwcDPc')
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
	if message.text == "/start":
		bot.send_message(message.from_user.id, "Well...Hello there! I am bonzi! Your best friend in telegramm!I can joke,fact,sing,news,memes!")
	elif message.text == "/help":
		bot.send_message(message.from_user.id, "я устал писать код......")
	else:
		bot.send_message(message.from_user.id, "you can write command /help")
	if message.text == "/bonzi_joke":
		bot.send_message(message.from_user.id, "A tender for the construction of a building is being held in Moscow. The project is represented by a German company. Estimate 10 million. Then the Turkish company – 5 million. The turn of the Russian company is approaching. They have an estimate of 15 million. - Why so much? - Well, how about that? 5 million for us, 5 million for you and 5 Turks to build. And they win the tender!")
	if message.text == "/bonzi_sing":
		bot.send_message(message.from_user.id, "https://www.youtube.com/watch?v=dtw-6Jvim4c")
	if message.text == "/bonzi_fact":
		bot.send_message(message.from_user.id, "Why is the keyboard keys not in alphabetical order?The reason dates back to the time of manual typewriters. When first invented , they had keys arranged in an alphabetical order, but people typed so fast that the mechanical character arms got tangled up. So the keys were randomly positioned to actually slow down typing and prevent key jams.")
	if message.text == "/bonzi_news":
		bot.send_message(message.from_user.id, "bbc.com or ria.ru")
	if message.text == "/bonzi_memes":
		bot.send_message(message.from_user.id, "sure... http://zorgv.w10.site/memes.htm")
bot.polling(none_stop=True, interval=0)	
