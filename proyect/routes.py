from flask import Blueprint, render_template, flash, Flask, request, redirect, url_for
from proyect.modules import UploadFileForm
from werkzeug.utils import secure_filename
import os
import pandas
from proyect.verif import verificaciones, allowed_file
from proyect.formater import cargos, paises, districtos, departamentos, localidades, establecimientos, mesas, listas, candidatos
import time
from pathlib import Path


pages = Blueprint(
    "pages", __name__, template_folder="templates", static_folder="static"
)


@pages.route("/", methods=['GET','POST'])
@pages.route("/home" ,methods=['GET','POST'])
def index():
    
        
    return render_template(
        "home.html",
        
        
        
    )
    
@pages.route("/validate" ,methods=['GET','POST'])
def validate():
    
    
    required_file_list_names=['mesas','listas', 'candidatos' , 'candidaturas'
                            ,'mesas_certificados', 
                            'mesas_candidaturas_seguridad_trep' ]
    
    form=UploadFileForm()
    if form.validate_on_submit():
        
        
        status=[]
        
        for file in form.file.data:
            status.append(f'Validando {file.filename}')
            if allowed_file(file.filename):
                
                if file.filename.rsplit('.')[0] in required_file_list_names:
                
                    isValid,flash=verificaciones(file, file.filename)
        
                    if isValid:
                    ## Aca guardaria las files en static, no se si hay una mejor manera de hacerlo, si es que va a un server o algo asi.
                    # los archivos excel se guaran dañados.Por lo tanto en verificaciones los guardo como csv.
                    #file.save(os.path.join(os.path.abspath(os.path.dirname('proyect/static/files/upload_files/')),secure_filename(file.filename))) 
                        print(f'{file.filename} fue guardado con exito')
                    
                    for el in flash:
                        status.append(el) 
                 
                else: status.append(f'{file.filename} no es el nombre de un archivo esperado')
        
                        
                    
            else: status.append(f'Solo se aceptan formatos cvs y exel')
            
                            
               
                
                
        ##formating
        
          
        
        required_file_list=['mesas.csv','listas.csv', 'candidatos.csv' , 'candidaturas.csv'
                            ,'mesas_certificados.csv', 
                            'mesas_candidaturas_seguridad_trep.csv' ]
            
        upload_directory=Path('proyect/static/files/upload_files')
        formated_directory=Path('proyect/static/files/formated_files')
        
        files=os.listdir(upload_directory)
        
        if set(files).intersection(required_file_list):
            
            print("Estan todos los archivos requeridos, inicio fomateo")
            paises(upload_directory)  
            districtos(upload_directory)
            departamentos(upload_directory)
            localidades(upload_directory)
            establecimientos(upload_directory)
            mesas(upload_directory)
            listas(upload_directory)
            candidatos(upload_directory, formated_directory)
            cargos(upload_directory)
        

                        
            
            
            
        return render_template("validate.html",
        form=form,
        status=status)
        
        
    return render_template(
        "validate.html",
        form=form,
        
    )
