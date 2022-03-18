def genaungpao():
    import random
    from json import loads
    from httpx import post
    config = loads(open("config.json","r",encoding="utf-8").read())

    choice = 'abcdefghijklmnopABCDEFGHIJKLMNOP1234567890'
    choice1 = 'abcdefghijklmnopABCDEFGHIJKLMNOP1234567890'
    while True:
        value = random.choice(choice)
        value2 = random.choice(choice)
        value3 = random.choice(choice)
        value4 = random.choice(choice)
        value5 = random.choice(choice)
        value6 = random.choice(choice)
        value7 = random.choice(choice)
        value8 = random.choice(choice)
        value9 = random.choice(choice)
        value10 = random.choice(choice1)
        value11 = random.choice(choice1)
        value12 = random.choice(choice1)
        value13 = random.choice(choice1)
        value14 = random.choice(choice1)
        value15 = random.choice(choice1)
        value16 = random.choice(choice1)
        value17 = random.choice(choice1)
        value18 = random.choice(choice1)

        
        aungpaoout = ('https://gift.truemoney.com/campaign/?v=' + value + value2 + value3 + value4 + value5 + value6 + value7 + value8 + value9 + value10 + value11 + value12 + value13 + value14 + value15 + value16 + value17 + value18)
        cnpflood = config["webhook-gen"]
        post(cnpflood,json={"content": aungpaoout})
