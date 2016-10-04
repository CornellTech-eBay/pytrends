# @Author: Gao Bo
# @Date:   2016-10-03T22:39:11-04:00
# @Last modified by:   Gao Bo
# @Last modified time: 2016-10-03T23:48:14-04:00



from pytrends.request import *
import json

def parseTrendsJson(trends):
    tdate = 1
    # test: just get the most trending term of the first day of this week
    # date is a string
    date = trends["weeksList"][-1]["daysList"][tdate]["longFormattedDate"]
    # title if a string
    title = trends["weeksList"][-1]["daysList"][tdate]["data"]["trend"]["title"]
    # relatedSearchesList is a list of strings
    relatedSearchesList = trends["weeksList"][-1]["daysList"][tdate]["data"]["trend"]["relatedSearchesList"]

    print("On " + date)
    print("Most trending: " + title)
    print("Related searches:")
    print(", ".join(relatedSearchesList))
    # for term in relatedSearchesList:
    #     print()


if __name__ == "__main__":
    google_username = "cornelltechebay@gmail.com"
    google_password = "cornell&ebay"
    pytrends = TrendReq(google_username, google_password, custom_useragent=None)

    top30 = pytrends.top30in30()
    parseTrendsJson(top30)
    outfile = open('trendsOutput.txt', 'w')
    outfile.write(json.dumps(top30, sort_keys=True, indent=4, separators=(',', ': ')))
    outfile.close()
