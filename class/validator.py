def validate_references(df):
  if len(df) > 0:
    if (
      str(type(df.code[0])) == "<class 'str'>"
    ) and (
      str(type(df.month[0])) == "<class 'str'>"
    ):
      return df


def validate_brand(df):
  if len(df) > 0:
    if (
      str(type(df.name[0])) == "<class 'str'>"
    ) and (
      str(type(df.id[0])) == "<class 'str'>"
    ) and (
      str(type(df.vehicleType[0])) == "<class 'str'>"
    ):
      return df


def validate_model(df):
  if len(df) > 0:
    if (
      str(type(df.name[0])) == "<class 'str'>"
    ) and (
      str(type(df.id[0])) == "<class 'str'>"
    ) and (
      str(type(df.brandId[0])) == "<class 'str'>"
    ) and (
      str(type(df.vehicleType[0])) == "<class 'str'>"
    ):
      return df


def validate_years_by_model(df):
  if len(df) > 0:
    if (
      str(type(df.name[0])) == "<class 'str'>"
    ) and (
      str(type(df.code[0])) == "<class 'str'>"
    ) and (
      str(type(df.modelId[0])) == "<class 'str'>"
    ) and (
      str(type(df.brandId[0])) == "<class 'str'>"
    ) and (
      str(type(df.vehicleType[0])) == "<class 'str'>"
    ):
      return df


def validate_fipe_info(df):
  if len(df) > 0:
    if (
      str(type(df['price'][0])) == "<class 'str'>"
    ) and (
      str(type(df['brand'][0])) == "<class 'str'>"
    ) and (
      str(type(df['model'][0])) == "<class 'str'>"
    ) and (
      str(type(df['modelYear'][0])) == "<class 'numpy.int64'>" or "<class 'numpy.int32'>"
    ) and (
      str(type(df['fuel'][0])) == "<class 'str'>"
    ) and (
      str(type(df['codeFipe'][0])) == "<class 'str'>"
    ) and (
      str(type(df['referenceMonth'][0])) == "<class 'str'>"
    ) and (
      str(type(df['vehicleType'][0])) == "<class 'numpy.int64'>" or "<class 'numpy.int32'>"
    ) and (
      str(type(df['fuelAcronym'][0])) == "<class 'str'>"
    ) and (
      str(type(df['vehicleType'][0])) == "<class 'str'>"
    ) and (
      str(type(df['brandId'][0])) == "<class 'str'>"
    ) and (
      str(type(df['modelId'][0])) == "<class 'str'>"
    ) and (
      str(type(df['yearId'][0])) == "<class 'str'>"
    ) and (
      str(type(df['referenceId'][0])) == "<class 'str'>"
    ):
      return df


def validate_years_by_fipe_code(df):
  if len(df) > 0:
    if(
      str(type(df['name'][0])) == "<class 'str'>"
    ) and (
      str(type(df['code'][0])) == "<class 'str'>"
    ):
      return df


def validate_fipe_info_by_fipe_code(df):
  if len(df) > 0:
    if(
      str(type(df['price'][0])) == "<class 'str'>"
    ) and (
      str(type(df['brand'][0])) == "<class 'str'>"
    ) and (
      str(type(df['model'][0])) == "<class 'str'>"
    ) and (
      str(type(df['modelYear'][0])) == "<class 'numpy.int64'>" or "<class 'numpy.int32'>"
    ) and (
      str(type(df['fuel'][0])) == "<class 'str'>"
    ) and (
      str(type(df['codeFipe'][0])) == "<class 'str'>"
    ) and (
      str(type(df['referenceMonth'][0])) == "<class 'str'>"
    ) and (
      str(type(df['vehicleType'][0])) == "<class 'numpy.int64'>" or "<class 'numpy.int32'>"
    ) and (
      str(type(df['fuelAcronym'][0])) == "<class 'str'>"
    ) and (
      str(type(df['vehicleType'][0])) == "<class 'str'>"
    ) and (
      str(type(df['yearId'][0])) == "<class 'str'>"
    ):
      return df


def validate_fipe_price_history_by_fipe_code(df):
  if len(df) > 0:
    if(
      str(type(df['brand'][0])) == "<class 'str'>"
    ) and (
      str(type(df['model'][0])) == "<class 'str'>"
    ) and (
      str(type(df['modelYear'][0])) == "<class 'numpy.int64'>" or "<class 'numpy.int32'>"
    ) and (
      str(type(df['fuel'][0])) == "<class 'str'>"
    ) and (
      str(type(df['codeFipe'][0])) == "<class 'str'>"
    ) and (
      str(type(df['vehicleType'][0])) == "<class 'numpy.int64'>" or "<class 'numpy.int32'>"
    ) and (
      str(type(df['fuelAcronym'][0])) == "<class 'str'>"
    ) and(
      str(type(df['priceHistory'][0])) == "<class 'dict'>"
    ) and (
      str(type(df['vehicleTypeStr'][0])) == "<class 'str'>"
    ) and (
      str(type(df['yearId'][0])) == "<class 'str'>"
    ):
      return df