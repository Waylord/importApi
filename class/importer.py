import pandas as pd
import requester
import validator

def import_references():
  df = pd.DataFrame.from_records(requester.get_references())
  
  return validator.validate_references(df)


def import_brand(vehicleType):
  df = pd.DataFrame.from_records(requester.get_brands(vehicleType))
  df.rename(columns = {"code": "id"}, inplace = True)
  df = df.assign(vehicleType = vehicleType)
  
  return validator.validate_brand(df)


def import_all_brands(vehicleTypes):
  frame = pd.DataFrame()
  
  for vehicleType in vehicleTypes:
    df = import_brand(vehicleType)
    if(frame.empty):
      frame = df
    else:
      frame = pd.concat([frame, df], ignore_index = True)

  return validator.validate_brand(frame)


def import_model(vehicleType, brandId):
  df = pd.DataFrame.from_records(requester.get_models(vehicleType, brandId))
  df.rename(columns = {"code": "id"}, inplace = True)
  df = df.assign(brandId = brandId, vehicleType = vehicleType)
  
  return validator.validate_model(df)


def import_all_models(brands):
  frame = pd.DataFrame()

  for brand in brands:
    df = import_model(brand['vehicleType'], brand['brandId'])
    if frame.empty:
      frame = df
    else:
      frame = pd.concat([frame, df], ignore_index = True)

  return validator.validate_model(frame)
    

def import_years_by_model(vehicleType, brandId, modelId):
  df = pd.DataFrame.from_records(requester.get_year_by_model(vehicleType, brandId, modelId))
  df = df.assign(modelId = modelId, brandId = brandId, vehicleType = vehicleType)

  return validator.validate_years_by_model(df)
    

def import_fipe_info(vehicleType, brandId, modelId, yearId, reference = '0'):
  df = pd.DataFrame.from_records(requester.get_fipe_info(vehicleType, brandId, modelId, yearId, reference), index = [0])
  df = df.assign(yearId = yearId, modelId = modelId, brandId = brandId, vehicleType = vehicleType, referenceId = reference)

  return validator.validate_fipe_info(df)


def import_all_fipe_info(years, reference = '0'):
  frame = pd.DataFrame()

  for i in range(len(years)):
    df = import_fipe_info(years['vehicleType'][i], years['brandId'][i], years['modelId'][i], years['code'][i], reference)
    if frame.empty:
      frame = df
    else:
      frame = pd.concat([frame, df], ignore_index = True)
    
  return validator.validate_fipe_info(frame)


def import_years_by_fipe_code(vehicleType, fipeCode):
  df = pd.DataFrame.from_records(requester.get_years_by_fipe_code(vehicleType, fipeCode))
  #TODO verificar se há necessidade de fazer join com alguma tabela para referenciar

  return validator.validate_years_by_fipe_code(df)


def import_fipe_info_by_fipe_code(vehicleType, fipeCode, yearId):
  df = pd.DataFrame.from_records(requester.get_fipe_info_by_fipe_code(vehicleType, fipeCode, yearId), index = [0])
  df = df.assign(vehicleType = vehicleType, fipeCode = fipeCode, yearId = yearId)

  return validator.validate_fipe_info_by_fipe_code(df)


def import_fipe_price_history_by_fipe_code(vehicleType, fipeCode, yearId):
  df = pd.DataFrame.from_records(requester.get_fipe_price_history_by_fipe_code(vehicleType, fipeCode, yearId))
  df = df.assign(vehicleTypeStr = vehicleType, yearId = yearId)

  return validator.validate_fipe_price_history_by_fipe_code(df)