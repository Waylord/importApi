import importer

#Fonte: http://deividfortuna.github.io/fipe/v2/

vehicleTypes = ['cars','motorcycles','trucks']

if __name__ == '__main__':
  # Primeiramente importa as marcas de veículos em um json
  references = importer.import_references()
  print(references)
  
  brands = importer.import_all_brands(vehicleTypes)
  print(brands)
  
  models = importer.import_model(brands['vehicleType'][0], brands['id'][0])
  print(models)

  years = importer.import_years_by_model(models['vehicleType'][0], models['brandId'][0], models['id'][0])
  print(years)

  fipe_info = importer.import_fipe_info(years['vehicleType'][0], years['brandId'][0], years['modelId'][0], years['code'][0], references['code'][0])
  print(fipe_info)

  all_fipe_info = importer.import_all_fipe_info(years, "278")
  print(all_fipe_info)

  years_by_fipe_code = importer.import_years_by_fipe_code(all_fipe_info['vehicleType'][0], all_fipe_info['codeFipe'][0])
  print(years_by_fipe_code)

  fipe_info_by_fipe_code = importer.import_fipe_info_by_fipe_code(all_fipe_info['vehicleType'][0], all_fipe_info['codeFipe'][0], all_fipe_info['yearId'][0])
  print(fipe_info_by_fipe_code)

  fipe_price_history_by_fipe_code = importer.import_fipe_price_history_by_fipe_code(all_fipe_info['vehicleType'][0], all_fipe_info['codeFipe'][0], all_fipe_info['yearId'][0])
  print(fipe_price_history_by_fipe_code)