
#!/bin/bash

PORT=`grep SERVICE_PORT settings.py | awk -F "=" '{print $2}' | awk -F "," '{print $1}' | xargs echo`

if [ "$_SERVICE_MODE" == "develop" ]; then
    python manage.py runserver 0.0.0.0 $PORT
else
	gunicorn server:app \
        --reload \
        --bind 127.0.0.1:$PORT \
        --env API_GATEWAY=api.test.com \
        --env MODE=deploy \
        --env DB_NAME=$_DB_NAME \
        --env DB_USER=$_DB_USER \
        --env DB_HOST=$_DB_HOST \
        --env DB_PORT=$_DB_PORT \
        --env DB_PASSWORD=$_DB_PASSWORD \
        --env _ENABLE_API_SERVICE_CONSOLE=0
fi

