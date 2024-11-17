def get_clean_val(param_value, extracted_key='title'):
	if extracted_key in param_value:
		return param_value.get(extracted_key)
	else:
		return param_value
