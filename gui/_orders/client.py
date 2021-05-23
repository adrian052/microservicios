from client.services import post_request

auth_key = "6c901c1c19fe4dee8d6a7c06b302bf99"

def post_order(params):
   response = post_request('http://127.0.0.1:8080/orders_service/order/',auth_key=auth_key,params=params)
   if response:
      return response
   return 'No response'

def post_orderitem(params):
   response = post_request('http://127.0.0.1:8080/orders_service/order_item/',auth_key=auth_key,params=params)
   if response:
      return response
   return 'No response'