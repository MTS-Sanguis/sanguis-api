rsync -rzvaP -e 'ssh -i ~/.ssh/google_compute_engine' swagger_server ../sanguis/questionnaire.yaml sanguis:/tmp/

ssh -i ~/.ssh/google_compute_engine -T sanguis '
cd /tmp
cat server.pid | xargs sudo kill
sudo nohup python -m swagger_server 80 > /tmp/server.out 2> /tmp/server.err < /dev/null & echo $! > server.pid
'
