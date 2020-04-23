# Mail Dataset Kit

Process of creating dataset of email using python

Libraries used: BeautifulSoup, NLTK

1) Label the emails you want to download into single label in gmail
2) Go to Google account -> Data -> Download your data
3) Scroll to Gmail and select the label you just created
4) Download the zip file and upload it to website given below,
https://www.coolutils.com/online/MBOX-to-TXT
5) unzip the output file and paste txttocsv.py into it
6) Change encoding for file as per your need given in line no. 21 in the code
7) Change the format for the csv files, add columns as per your requirement in line no. 82
8) Run the python code to get csv file of emails in file newdataset.csv
