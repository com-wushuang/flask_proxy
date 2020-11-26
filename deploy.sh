#!/bin/bash

# 删除container
docker rm -f hexo
# 启动一个新的容器
docker run --name hexo -d -p 80:80 hexo:latest
