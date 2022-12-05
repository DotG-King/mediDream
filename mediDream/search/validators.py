from django.core.exceptions import ValidationError
import os

def validate_file(value):
    filesize = value.size
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.jpg','.jpge']

    if filesize > 10485760:
        raise ValidationError("업로드 가능 최대 용량은 10MB 입니다!")
    else:
        if not ext in valid_extensions:
            raise ValidationError('업로드 가능 확장자는 .jpg .jpge 입니다!')
        return value
