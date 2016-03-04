import requests
import urllib
import datetime

# def download_file(url, startTime, endTime):
#     filename = startTime + "_" + endTime + ".csv"
#     testfile = urllib.URLopener()
#     testfile.retrieve(url, filename)
#     print "done"


def download_file(url, startTime, endTime):
    local_filename = startTime + "_" + endTime + ".csv"
    # NOTE the stream=True parameter
    r = requests.get(url, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024): 
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
                #f.flush() commented by recommendation from J.F.Sebastian
    print local_filename, "done"
    return local_filename


def main():
    end = datetime.date(2016, 3, 1)
    start = datetime.date(2015, 10, 1)
    # 4 months span
    delta = datetime.timedelta(152)
    while start.year > 1900:
    	startTime = start.isoformat()
    	endTime = end.isoformat()
    	URL = "http://earthquake.usgs.gov/fdsnws/event/1/query?format=csv&starttime=" + startTime + "&endtime=" + endTime + "&minmagnitude=2.5"
    	download_file(URL, startTime, endTime)
        start = start - delta
        end = end - delta

if __name__ == "__main__":
    main()