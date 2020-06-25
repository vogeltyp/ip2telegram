#!/usr/bin/env python3
# SCRIPT:       ip2telegram
# AUTHOR:       Holger (holger@sohonet.ch)
# DATE:         20200625
# REVISION:     1.1
# PLATFORM:     Python
# PURPOSE:      get IP from FQDN via Hurrican Electric DNS and send telegram message
# REV. LIST:    DATE            AUTHOR      MODIFICATION
# 1.1           20200625        Holger      - added change-detection
# 1.0           20200624        Holger      - initial script


import telepot
import dns.resolver
import os.path


def cacheIP(ip):
    cachefile = open(cache, "w")
    cachefile.write(ip)
    cachefile.close()


def readCache():
    cachefile = open(cache, "r")
    cachedIP = cachefile.read()
    return cachedIP


if __name__ == "__main__":
    cache = "ip2telegram.cache"
    bot = telepot.Bot('YourTelegramBotToken')
    chatID = 'YourChatID'
    searchfqdn = 'thedomain.youwanttocheck.com'

    dns_resolver = dns.resolver.Resolver()
    dns_resolver.nameservers = ['216.218.130.2', '216.218.131.2', '216.218.132.2', '216.66.1.2', '216.66.80.18', '8.8.8.8']
    result = dns_resolver.query(searchfqdn, 'A')
    ip = ''
    for ipval in result:
        ip = ipval.to_text()

    if os.path.isfile(cache):
        cachedIP = readCache()
        if ip != cachedIP:
            cacheIP(ip)
            message = "```\n%s\n\nchanged IP\n\nfrom %s\nto   %s```" % (searchfqdn, cachedIP, ip)
            bot.sendMessage(chatID, message, parse_mode="Markdown")
    else:
        cacheIP(ip)
        message = "%s has IP %s" % (searchfqdn, ip)
        bot.sendMessage(chatID, message, parse_mode="Markdown")
