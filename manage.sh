#!/bin/sh

py_start() {
    py_stop
    if [ ! -d "log" ]; then
      mkdir log
    fi
    chmod 777 gunicorn_py
    ./gunicorn_py -c gun.py app:app &
    echo "Server started."
}

py_stop() {
    pid=`ps -ef | grep '[g]unicorn_py -c gun.py app:app' | awk '{ print $2 }'`
    if [ "$pid" != "" ]; then
      kill -9 $pid 
      sleep 2
      pid_check=`ps -ef | grep '[g]unicorn_py -c gun.py app:app' | awk '{ print $2 }'`
      if [ "$pid_check" == "" ]; then
        echo "Server killed."
      else 
        echo "Server killed failing."
      fi
    fi
}

case "$1" in
  start)
    py_start
    ;;
  stop)
    py_stop
    ;;
  restart)
    py_stop
    py_start
    ;;
  *)
    echo "App {start|stop|restart}"
    exit 1
esac
exit 0
