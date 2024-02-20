git pull
kill $(ps -ef | grep 'python main.py' | grep -v grep | awk '{print $2}')
nohup python main.py > /dev/null 2>&1 &
