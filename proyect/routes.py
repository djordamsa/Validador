from flask import Blueprint, render_template
from proyect.modules import UploadFileForm
from werkzeug.utils import secure_filename
import os
from flask import Flask
from proyect.verif import verificaciones


pages = Blueprint(
    "pages", __name__, template_folder="templates", static_folder="static"
)


@pages.route("/", methods=['GET','POST'])
@pages.route("/home" ,methods=['GET','POST'])
def index():
    form=UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data
        
        ## aca tendria que entrar las verificiaciones, pero
        ## la funcion verificaciones esta hecha usando el nombre de el archivo y llamando los samples que me dio maxi.
        ## tendria que ver como hago para inicializar la funcion pasandole el archivo como parametro.
        isValid,flash=verificaciones(file)
        
        if isValid:
            ## Aca guardaria las files en static, no se si hay una mejor manera de hacerlo, si es que va a un server o algo asi.
            file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),secure_filename(file.filename))) 
            return "Archivo cargado con exito"
        else:
            return ### aca irian los flash de los errores. Despues busco como se hace que no recuerdo.
    
    return render_template(
        "home.html",
        form=form,
    )