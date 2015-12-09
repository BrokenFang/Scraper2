class Scrapper:
    server = ''
    root_url = ''
    summoner_url = ''
    accounts = []
    how_much = 0

    def __init__(self, server, summoner, how_much):
        self.server = server
        self.summoner_url = summoner
        self.root_url = 'http://'+ server +'.op.gg/summoner/userName=' + summoner
        self.how_much = how_much

    def printitself(self):
        print (self.server)
        print (self.root_url)
        print (self.summoner_url)
        print (self.how_much)
        print (self.accounts)

    def export(self, how_much):
        f = open('output.txt', 'a', encoding='utf-8')
        for account in accounts:
            f.write('%s\n' % account)
        f.close()

class Account:
    username = ''
    password = ''

    def __init__(self, username, password):
        self.username = username
        self.password = password


c = Scrapper('eune','azakelis', 20)
c.printitself()
