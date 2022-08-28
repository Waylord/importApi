import requests

def get_references():
  response = requests.get('https://parallelum.com.br/fipe/api/v2/references', headers={"User-Agent": "XY"})
  if(response.status_code == 200):
    return response.json()
  
def get_brands(vehicleType):
  response = requests.get('https://parallelum.com.br/fipe/api/v2/' + vehicleType + '/brands', headers={"User-Agent": "XY"})
  if(response.status_code == 200):
    return response.json()

def get_models(vehicleType, brandId):
  response = requests.get('https://parallelum.com.br/fipe/api/v2/' + vehicleType + '/brands/' + str(brandId) + '/models', headers={"User-Agent": "XY"})
  if(response.status_code == 200):
    return response.json()

def get_year_by_model(vehicleType, brandId, modelId):
  response = requests.get('https://parallelum.com.br/fipe/api/v2/' + vehicleType + '/brands/' + str(brandId) + '/models/' + str(modelId) + '/years', headers={"User-Agent": "XY"})
  if(response.status_code == 200):
    return response.json()

def get_fipe_info(vehicleType, brandId, modelId, yearId, reference = '0'):
  if(reference == 0):
    response = requests.get('https://parallelum.com.br/fipe/api/v2/' + vehicleType + '/brands/' + str(brandId) + '/models/' + str(modelId) + '/years/' + str(yearId), headers={"User-Agent": "XY"})
    
  else:
    response = requests.get('https://parallelum.com.br/fipe/api/v2/' + vehicleType + '/brands/' + str(brandId) + '/models/' + str(modelId) + '/years/' + str(yearId) + '?reference=' + str(reference), headers={"User-Agent": "XY"})
  
  if(response.status_code == 200):
    return response.json()

def get_years_by_fipe_code(vehicleType, fipeCode):
  response = requests.get('https://parallelum.com.br/fipe/api/v2/' + vehicleType + '/' + fipeCode + '/years', headers={"User-Agent": "XY"})
  if(response.status_code == 200):
    return response.json()

def get_fipe_info_by_fipe_code(vehicleType, fipeCode, yearId):
  response = requests.get('https://parallelum.com.br/fipe/api/v2/' + vehicleType + '/' + fipeCode + '/years/' + yearId, headers={"User-Agent": "XY"})
  if(response.status_code == 200):
    return response.json()

def get_fipe_price_history_by_fipe_code(vehicleType, fipeCode, yearId):
  response = requests.get('https://parallelum.com.br/fipe/api/v2/' + vehicleType + '/' + fipeCode + '/years/' + yearId + '/history', headers={"User-Agent": "XY"})
  if(response.status_code == 200):
    return response.json()
