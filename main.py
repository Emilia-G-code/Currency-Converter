import requests 

response = requests.get("https://www.cbar.az/currency/rates?language=en")

class CurrencyConverter:
    def __init__(self, exchange_rate):
        self.exchange_rate = exchange_rate

    def convert(self, amount):
        return amount / self.exchange_rate

response = requests.get("https://coinmarketcap.com")

print(response.text, "\n\n")

response_text = response.text
response_parse = response_text.split("<span>")
for parse_elem1 in response_parse:
    if ( parse_elem1.startswith("AZN")):
        for parse_elem2 in parse_elem1.split("</span>"):
            if (parse_elem2.startswith("AZN") and parse_elem2[1].isdigit()):
                print(parse_elem2)

    exchange_rate = parse_elem2
    converter = (exchange_rate)
    amount = int(input("Enter the amount of your currency: "))
    usd_amount = converter.convert(amount(int))

    print(f"{amount} of the Manat is equal to {usd_amount} US dollars.")
