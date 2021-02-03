# nordbayern_news
download pdf e-newspaper from nordbayern.de (for registered accounts)

# prerequisites
- only standard python modules requets, os, platform, datetime
- be paying customer of nordbayern.de e-paper

# usage
- change username and pw in sh/bat file (yes, its in plain text)
- change newspaper name in py file (line 31) from Pegnitzzeitung to your newspaper
- pray that they haven't modified their website yet
- run py file

# known issues
- today's paper tellin today's news: downloads today's newspaper, will thus fail on sunday
- else: just alter the datestring in l. 28 if you want older news
- might be fragile, token is extracted from 404 page since digging it from regular answer failed
