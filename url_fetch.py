import requests
import json
import pandas as pd
from io import StringIO

appConf = {}
with open("config.json") as f:
    appConf = json.load(f)

feedUrl = appConf.get("fetchUrl", "")
outFilePath = appConf.get("urlOutFilePath", "urls.txt")
fetchSpan = appConf.get("urlSpan", "")
fetchToken = appConf.get("fetchToken", "")

reqHeaders = {
    'Authorization': fetchToken,
    'Content-Type': 'application/json'
}

urlFetchPayload = {
    "date": fetchSpan,
    "returnFormat": "csv",
    "published": "1",
    "type": "url"
}

urlFeedResponse = requests.request(
    method="POST", url=feedUrl, headers=reqHeaders, data=json.dumps(urlFetchPayload))
urlRespCsv = urlFeedResponse.text
df = pd.read_csv(StringIO(urlRespCsv))
urlDf = pd.DataFrame()
urlDf['value'] = df['value']

urlDf.to_csv(outFilePath, header=False, index=False)
