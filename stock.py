import re
import requests as req
import bs4
import csv
with open('stock.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile,delimiter=',')
    ow=[]
    for i in range(1,10):
        for j in range(1,5):
            url='https://pchome.megatime.com.tw/group/mkt0/cid0{0}_{1}.html'.format(i,j)
            headers = {"Referer": str(url).encode("utf-8").decode("latin1")}

            htmlfile=req.get(url = url, headers = headers)
            obj=bs4.BeautifulSoup(htmlfile.text,"html.parser")

            obs=obj.find_all("td",{'class':'ct'})
                    
            for i in obs:
                ow.append(i.text)

    
                        
    for o in range(0,len(ow),9):
        writer.writerow(ow[o:o+9])


                
            




