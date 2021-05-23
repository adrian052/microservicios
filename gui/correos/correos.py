from client.services import post_request

auth_key = "9571aa06ac924429b53c415ca2c808e4"

def mandar_correo(params):
    response = post_request("http://127.0.0.1:8080/email_service/email/send/",params=params,auth_key=auth_key)
    if response:
      return response
    return 'No response'