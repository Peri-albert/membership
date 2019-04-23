
SERVICE_NAME=`grep SERVICE_NAME settings.py | awk -F "=" '{print $2}' | awk -F "," '{print $1}' | xargs echo`

docker build -t registry.cn-hangzhou.aliyuncs.com/aix/$SERVICE_NAME:latest .

