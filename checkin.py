import requests,json,os

# server酱开关，填off不开启(默认)，填on同时开启cookie失效通知和签到成功通知
sever = os.environ["SERVE"]
# 填写server酱sckey,不开启server酱则不用填
sckey = os.environ["SCKEY"]
#'SCU89402Tf98b7f01ca3394b9ce9aa5e2ed1abbae5e6ca42796bb9'
# 填入glados账号对应cookie
cookie = os.environ["COOKIE"]
#'_ga=GA1.1.2042766244.1699326900; _ga_CZFVKMNT9J=GS1.1.1715831152.12.1.1715831405.0.0.0; koa:sess=eyJ1c2VySWQiOjQyOTAxOCwiX2V4cGlyZSI6MTc1ODE2MDI2NTM4OSwiX21heEFnZSI6MjU5MjAwMDAwMDB9; koa:sess.sig=9uiaK9y8emnURLJZP89lllTVnNE'



def start():
    
    url= "https://glados.rocks/api/user/checkin"
    url2= "https://glados.rocks/api/user/status"
    body={'token': 'glados.one'}
    checkin = requests.post(url,data=json.dumps(body),headers={'cookie': cookie, 'Content-Type': 'application/json'})
    state =  requests.get(url2,headers={'cookie': cookie})
    #print(checkin.text)
    #print(state.text)

    if 'message' in checkin.text:
        mess = checkin.json()['message']
        time = state.json()['data']['leftDays']
        time = time.split('.')[0]
        print(time)
        if sever == 'on':
            requests.get('https://sc.ftqq.com/' + sckey + '.send?text='+mess+'，you have '+time+' days left')
    else:
        requests.get('https://sc.ftqq.com/' + sckey + '.send?text=cookie过期')

def main_handler(event, context):
  return start()

if __name__ == '__main__':
    start()

    
