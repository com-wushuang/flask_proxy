FROM python:2.7.16
ADD run.sh /run.sh
EXPOSE 80
CMD ["sh"]