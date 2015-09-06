import urllib.request
import json

"""
Working with a real-time JSON data feed from the USGS and processing the information.
"""

def print_results(data):
    the_json = json.loads(data)
    if "title" in the_json["metadata"]:
        print(the_json["metadata"]["title"] + "\n")

    count = the_json["metadata"]["count"]
    print(str(count) + " events recorded \n ")

    # print("Magnitude of 4 or greater:")
    #
    # for i in the_json["features"]:
    #     if i["properties"]["mag"] >= 4.0:
    #         print("%2.1f" % i["properties"]["mag"], i["properties"]["place"])

    print("Reports of felling an earthquake: \n")

    for i in the_json["features"]:
        felt_reports = i["properties"]["felt"]
        if felt_reports is not None:
            if felt_reports > 0:
                print("%2.1f" % i["properties"]["mag"], i["properties"]["place"], " reported " + str(felt_reports)
                      + " times")


def main():

    url_data = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"

    web_url = urllib.request.urlopen(url_data)
    print(web_url.getcode())
    if web_url.getcode() == 200:
        data = web_url.read()
        data = data.decode("utf=8")
        print_results(data)

if __name__ == "__main__":
    main()
