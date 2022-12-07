from django.core.exceptions import ValidationError
import os

def validate_file(value):
    filesize = value.size
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.jpg','.jpeg']

    if filesize > 10485760:
        raise ValidationError("10MB 초과 이미지는 업로드 불가합니다")
        
    else:
        if not ext in valid_extensions:
            raise ValidationError('.jpg .jpeg 이외 이미지는 업로드 불가합니다')
        return value
