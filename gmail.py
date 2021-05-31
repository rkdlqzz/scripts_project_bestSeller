# -*- coding: cp949 -*-
import smtplib
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
import func

def makeText(bookList):
    text = ''
    for i in range(len(bookList)):
        text += '<br><img src='+bookList[i].image+'/>'
        text += '<p><br>����: '+bookList[i].title+'<br>'
        text += '<br>����: '+bookList[i].author+'<br>'
        text += '<br>�Ⱓ��: '+func.changeDate(bookList[i].pubdate)+'<br>'
        text += '<br>����: '+bookList[i].price+'��<br>'
        text += '<br>�ٰŸ�: '+bookList[i].description+'<br>'
        text += '<br>��ũ(������): '+bookList[i].link+'<br>'
        text += '</p><br><hr>'
    return text
def sendMail(bookList, rAddr):
    #global value
    host = "smtp.gmail.com" # Gmail STMP ���� �ּ�.
    port = "587"
    htmlText = '<html><header></header><body><h1><b>Bestseller</b></h1><hr>'+makeText(bookList)+'</body></html>'

    senderAddr = "bestseller802@gmail.com"     # ������ ��� email �ּ�.
    recipientAddr = rAddr   # �޴� ��� email �ּ�.

    msg = MIMEBase("multipart", "alternative")
    msg['Subject'] = "Favorites"
    msg['From'] = senderAddr
    msg['To'] = recipientAddr

    # MIME ������ �����մϴ�.
    HtmlPart = MIMEText(htmlText, 'html', _charset='UTF-8')

    # ������� mime�� MIMEBase�� ÷�� ��Ų��.
    msg.attach(HtmlPart)

    # ������ �߼��Ѵ�.
    s = smtplib.SMTP(host, port)
    #s.set_debuglevel(1)        # ������� �ʿ��� ��� �ּ��� Ǭ��.
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(senderAddr, "best802seller!")
    s.sendmail(senderAddr, [recipientAddr], msg.as_string())
    s.close()