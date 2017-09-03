from urllib import request

csv1_url = 'http://samplecsvs.s3.amazonaws.com/Sacramentorealestatetransactions.csv'
url1 = "http://www.google.com"

def download_tran_data(csv_url):
    response = request.urlopen(csv_url)
    csv = response.read()
    csv_str = str(csv)
    print(csv_str)
    lines = csv_str.split('\r')
    dest_url = r'dest.csv'
    with open(dest_url, "w") as fw:
        for line in lines:
            fw.write(line)


download_tran_data(url1)