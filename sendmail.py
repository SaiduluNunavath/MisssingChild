import smtplib

def sendmail(skey,email):
    TO = email
    SUBJECT = 'Match Found'
    TEXT =skey
    print(email)
    print(TEXT)
    # Gmail Sign In
    gmail_sender = "projectsfind2022@gmail.com"
    gmail_passwd = "fxgzjgjryisptjun"

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(gmail_sender, gmail_passwd)

    BODY = '\r\n'.join(['To: %s' % TO,
                        'From: %s' % gmail_sender,
                        'Subject: %s' % SUBJECT,
                        '', TEXT])

    try:
        server.sendmail(gmail_sender, [TO], BODY)
        print ('email sent')
    except:
        print ('error sending mail')

    server.quit()
