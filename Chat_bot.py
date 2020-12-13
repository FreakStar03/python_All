from time import sleep

#selenium
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# chrome_options = Options()
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-dev-shm-usage')
# driver = webdriver.Chrome(options=chrome_options)


print("🔴 "+" Hey Silly Bot, Here!"+" 🔴\n")
def wrong():
  print("Answer carefully, i am a Bot not moron.\n")
 
while True:
  name = input( "Hi, I'm Silly Bot, Whats Your name?\nAnswer: ")
  if name.isalpha() == True:

    sleep(5)
    done = 'true'
    print("\n" +" Hi " + name + ".\n")
    break
  else:
    wrong();

while True:
  age = input("How old are you?\nAnswer: ")
  if age.isnumeric() == True:
    print("\n" + "Huh, I'm " + age + " too.\n")
    break
  else:
    wrong()


hobby = input("What's your favorite thing to do?\nAnswer: ")
print(hobby + ".. Sounds fun.\n")

hopehome = input("If you could live anywhere, where would you live?\nAnswer: ")
print("Huh, I've always wanted to live in " + hopehome + " too.\n")

lang = input("What language do you speak?\nAnswer: ")
print(
    "yeah, I know, if you didn't speak english, you wouldn't be able to read the questions\n"
)

fear = input("what is your worst fear?\nAnswer: ")
print(fear + " are pretty scary\n")

change = input("what would you change about yourself if you could?\nAnswer: ")
print("I hear you, a lot of people hve that problem\n")

clinical_depression = input("do you have clinical depression?\nAnswer: ")
print("Well, I don't think so, I\'m a bot, XD\n")

#by freakstar
x = input("what do you prefer, Tea or coffee?\nAnswer: ")
if x == "tea":
  print("I prefer milk over tea!\n "),
elif x == "coffee":
  print("Hell no, i love tea!\n")
else:
  print("Moron, I gaved you option, never asked your opinion!\n")










