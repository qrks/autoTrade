# coding:utf-8

import subprocess
import os

#  下载或升级 easytrader
git_dir = 'easytrader_git'
# 不存在则下载 easytrader 的项目
if not os.path.exists(git_dir):
    subprocess.getoutput('git clone http://github.com/shidenggui/easytrader')

    # 重命名防止跟后面link出来的 easytrader 包冲突
    subprocess.getoutput('mv easytrader {}'.format(git_dir))

    # link easytrader 包到外部方便 import
    subprocess.getoutput('ln -s `pwd`/{}/easytrader easytrader'.format(git_dir))
# 如果存在则更新 easytrader 项目到最新版本
else:
    subprocess.getoutput('cd {} && git pull'.format(git_dir))

