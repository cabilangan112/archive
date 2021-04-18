def validate_file_extention(value):
	import os
	from django.core.exceptions import ValidationError

	ext = os.path.splitext(value.name)[1]
	valid_extations = ['.pdf']

	if not ext.lower() in valid_extations:
		raise ValidationError(u'Unsupported file extention.')