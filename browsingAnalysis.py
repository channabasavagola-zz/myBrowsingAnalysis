import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from urllib.parse import urlparse

# Copy History from location of Chrome
os.system("cp ~/Library/Application\ Support/Google/Chrome/Default/History ~/Projects/myBrowsingAnalysis/")
# Getting all links and it's details
os.system("sh get_history.sh")


historyData = pd.read_csv("out.csv")
historyData.dropna(inplace=True)
# historyData.date = pd.to_datetime(historyData.date)
historyData.date = pd.to_datetime(historyData.date, errors='coerce')

parser = lambda u: urlparse(u).netloc
historyData.url = historyData.url.apply(parser)

site_frequencies = historyData.url.value_counts().to_frame()
site_frequencies = site_frequencies.reset_index().rename(columns = {"index": "domainName", "url": "count"})

topN = 20
plt.figure(1, figsize=(10,10))
plt.title('Top $n Sites Visited'.replace('$n', str(topN)))
pie_data = site_frequencies['count'].head(topN).tolist()
pie_labels = site_frequencies['domainName'].head(topN).tolist()
plt.pie(pie_data, autopct='%1.1f%%', labels=pie_labels)
plt.show()