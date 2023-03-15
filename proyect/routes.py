from flask import Blueprint, render_template, flash, Flask, request, redirect, url_for
from proyect.modules import UploadFileForm
from werkzeug.utils import secure_filename
import os

from proyect.verif import verificaciones, allowed_file



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
    form=UploadFileForm()
    if form.validate_on_submit():
        
        status=[]
        
        for file in form.file.data:
            status.append(f'Validando {file.filename}')
            if allowed_file(file.filename):
    
                isValid,flash=verificaciones(file, file.filename)
        
                if isValid:
                    ## Aca guardaria las files en static, no se si hay una mejor manera de hacerlo, si es que va a un server o algo asi.
                    file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),secure_filename(file.filename))) 
                
            else:
                status.append(f'Solo se aceptan formatos cvs y exel')
            
            for el in flash:
                status.append(el)    
            
        return render_template("validate.html",
        form=form,
        status=status)
        
        
    return render_template(
        "validate.html",
        form=form,
        
    )
