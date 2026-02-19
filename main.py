import colorama
from colorama import Fore, Style
from textblob import TextBlob

# Initiate colorama for coloured output
colorama.init()

# Emojis for the start of the program
print(f"{Fore.CYAN} Welcome to Sentiment Spy! {Style.RESET_ALL}")

user_name = input(f"{Fore.MAGENTA}Please enter your name : {Style.RESET_ALL}").strip()
if not user_name:
    user_name = "Mystery Agent" 

conversation_history = []
print(f"\n{Fore.CYAN}Hello, Agent {user_name}")
print(f"Type a sentence and I will analyse your sentences with textblob and show you the sentiment")
print(f"Type {Fore.YELLOW}reset{Fore.CYAN}, {Fore.YELLOW}history{Fore.CYAN},"
      f"or {Fore.YELLOW}exit{Fore.CYAN} to quit.{Style.RESET_ALL}\n")


while True:
    user_input = input(f"{Fore.GREEN}>>{Style.RESET_ALL}").strip()
    if not user_input:
        print(f"{Fore.RED}Please enter some text or a valid command.{Style.RESET_ALL}")
        continue

    if user_input.lower() == "exit":
        print(f"\n{Fore.BLUE}exiting Sentiment Spy. Farewell, Aghent {user_name}! {Style.RESET_ALL}")
        break

    elif user_input.lower() == "reset":
        conversation_history.clear()
        print(f"{Fore.CYAN}All conversation history cleared!{Style.RESET_ALL} ")
        continue
    elif user_input.lower() == "history":
        if not conversation_history:
            print(f"{Fore.YELLOW}no conversation history yet{Style.RESET_ALL}")
        else:
            print(f"{Fore.CYAN}conversation history : {Style.RESET_ALL}")
            for idx, (text,polarity,sentiment_type) in enumerate(conversation_history, start = 1):
                if sentiment_type == "positive":
                    color = Fore.GREEN
                elif sentiment_type == "negetive":
                    color = Fore.RED
                else:
                    color = Fore.YELLOW
                print(f"{idx}.{color}{text}"
                      f"polarity: {polarity:.2f},{sentiment_type}{Style.RESET_ALL}")
        continue

    # Analyze sentiment

polarity = TextBlob(user_input).sentiment.polarity

if polarity > 0.25:
    sentiment_type = "Positive"
    color = Fore.GREEN
    emoji = "😊"
elif polarity < -0.25:
    sentiment_type = "Negative"
    color = Fore.RED
    emoji = "😞"
else:
    entiment_type = "Neutral"
    color = Fore.YELLOW
    emoji = "😭"
    conversation_history.append((user_input, polarity, sentiment_type))

print(f"{color}{emoji} {sentiment_type} sentiment detected!"
f"Polarity: {polarity:.2f}")