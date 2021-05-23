from client.services import get_request

auth_key = '616f8871af944bad98c58668dd83f41e'

def get_categories():
   response = get_request('http://127.0.0.1:8080/catalog_service/category/',auth_key)
   if response:
      return response
   return 'No response'

def get_category(id):
   response = get_request('http://127.0.0.1:8080/catalog_service/category/'+id,auth_key)
   if response:
      return response
   return 'No response'

def get_products():
   response = get_request('http://127.0.0.1:8080/catalog_service/product/',auth_key)
   if response:
      return response
   return 'No response'

def get_product(id):
   response = get_request('http://127.0.0.1:8080/catalog_service/product/'+id,auth_key)
   if response:
      return response
   return 'No response'

