from signedqr import *

message = '$12,450.00'
message2 = 'JUAN PEREZ'
message3 = 'CTA-1234567890'

sub = 'qrcodes'
if not os.path.isdir(sub):
    os.makedirs(sub)

payload = dict(monto=message, nombre=message2,
               cuenta=message3, docid='00001-20190402')
signature = get_signature(payload, get_secret())
payload.update(dict(s=signature))
url = get_url(payload)
print(url)
save_qr(url, os.path.join(sub, 'qr.png'))
