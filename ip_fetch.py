import requests
import json
import pandas as pd
from io import StringIO

appConf = {}
with open("config.json") as f:
    appConf = json.load(f)

feedUrl = appConf.get("fetchUrl", "")
outFilePath = appConf.get("ipOutFilePath", "ips.txt")
fetchSpan = appConf.get("ipSpan", "")
fetchToken = appConf.get("fetchToken", "")

reqHeaders = {
    'Authorization': fetchToken,
    'Content-Type': 'application/json'
}

ipFetchPayload = {
    "date": fetchSpan,
    "returnFormat": "csv",
    "published": "1",
    "type": "ip-src"
}


ipFeedResponse = requests.request(
    method="POST", url=feedUrl, headers=reqHeaders, data=json.dumps(ipFetchPayload))
# print(response.text)
# with open("output.csv", mode='w') as f:
#    f.write(ipRespCsv)
ipRespCsv = ipFeedResponse.text
df = pd.read_csv(StringIO(ipRespCsv))
ipDf = pd.DataFrame()
ipDf['value'] = df['value']

ipDf.to_csv(outFilePath, header=False, index=False)
