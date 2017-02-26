#coding:utf-8
import easytrader

#  创建雪球账户
xq_user = easytrader.use('xq')
# xq_user.prepare(user='',account='13621914510', password='pass.123_xq', portfolio_code='ZH967491')
xq_user.prepare(account='13621914510', password='1q9g8q8s_xq', portfolio_code='ZH967491')

# 创建 jq 账户
jq_follower = easytrader.follower('jq')
jq_follower.login(user='13621914510', password='1q9g8q8s_jk')


# 关联jq模拟交易到雪球账户

#jq_follower.follow(xq_user, 'https://www.joinquant.com/algorithm/live/index?backtestId=13828898d2308b31c33af713acca0070')

moni_url1 = 'https://www.joinquant.com/algorithm/live/index?backtestId=13828898d2308b31c33af713acca0070'
#小市值
moni_url2 = 'https://www.joinquant.com/algorithm/live/index?backtestId=04c80ec713ae86b6eb5f2bf39b0b069d'


#测试用
# jq_follower.follow(users=[xq_user], strategies=[moni_url1],trade_cmd_expire_seconds=1000000000,cmd_cache=False,track_interval=10)

#！！！生产用！！！
# jq_follower.follow(users=xq_user, strategies=[moni_url1,moni_url2],trade_cmd_expire_seconds=120,cmd_cache=True,track_interval=5)
#单独的模拟交易
jq_follower.follow(users=xq_user, strategies=[moni_url1],trade_cmd_expire_seconds=240,cmd_cache=True,track_interval=8)