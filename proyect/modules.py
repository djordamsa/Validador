from flask_wtf import FlaskForm
from wtforms import MultipleFileField , SubmitField, validators, ValidationError

def my_length_check(form, field):
    file_names=['mesas', 'candidatos', 'candidaturas' , 'listas', 'mesas_certificados','mesas_candidaturas_seguridad_trep']
    if field.data.filename.split('.')[0] not in file_names:
        raise ValidationError('El nombre del archivo no se encuentra dentro de los nombre sugeridos.')


    
    
class UploadFileForm(FlaskForm):
    file=MultipleFileField("Selecciona Los Archivos")
    submit=SubmitField("Validar")