#!/usr/bin/env python3
# SCRIPT:       ip2telegram
# AUTHOR:       Holger (holger@sohonet.ch)
# DATE:         20200624
# REVISION:     1.0
# PLATFORM:     Python
# PURPOSE:      get IP from FQDN via Hurrican Electric DNS and send telegram message
# REV. LIST:    DATE            AUTHOR      MODIFICATION
# 1.0           20200624        Holger      - initial script


import telepot
import dns.resolver

if __name__ == "__main__":
    bot = telepot.Bot('TelegramBotToken')
    chatID = 'YourChatID'
    searchfqdn = 'fqdn.youliketocheck.com'

    dns_resolver = dns.resolver.Resolver()
    dns_resolver.nameservers = ['216.218.130.2', '216.218.131.2', '216.218.132.2', '216.66.1.2', '216.66.80.18', '8.8.8.8']
    result = dns_resolver.query(searchfqdn, 'A')
    ip = ''
    for ipval in result:
        ip = ipval.to_text()

    message = "%s has IP %s" % (searchfqdn, ip)

    bot.sendMessage(chatID, message)
