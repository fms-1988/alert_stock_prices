import smtplib

user = 'AKIAY23UVDNGE2CGZFO5'
pw   = 'wgBMh8c0hr8/u18YCMm7nuxXC8S6SvxOWdMa2G5E'
host = 'email-smtp.us-east-1.amazonaws.com'
port = 465
me   = u'alert@carbonprice.top'
you  = ('fms.morelli@gmail.com',)
body = 'Test'
msg  = ("From: %s\r\nTo: %s\r\n\r\n"
       % (me, ", ".join(you)))

msg = msg + body

s = smtplib.SMTP_SSL(host, port, 'yourdomain')
s.set_debuglevel(1)
s.login(user, pw)

s.sendmail(me, you, msg)
