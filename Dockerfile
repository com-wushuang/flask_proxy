FROM busybox:latest
ADD run.sh /run.sh
EXPOSE 80
CMD ["sh"]