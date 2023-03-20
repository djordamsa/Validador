import re


en_apostrofe = re.compile("'([a-zA-Z\.áéíóúñü]+)'", re.IGNORECASE | re.UNICODE)
en_apostrofe_d = re.compile("''([a-z\.\sA-Záéíóúñü]+)''", re.IGNORECASE | re.UNICODE)
en_doble_comilla = re.compile('"([a-z\.\s\'1-9A-Záéíóúñü]+)"', re.IGNORECASE | re.UNICODE)

en_comilla = re.compile('’([a-z\.A-Záéíóúñü]+)’', re.IGNORECASE | re.UNICODE)
en_comilla_ds = re.compile('’’([a-z\.\sA-Záéíóúñü]+)’’', re.IGNORECASE | re.UNICODE)

en_comilla_doble = re.compile('″([a-z\.\sA-Záéíóúñü]+)″', re.IGNORECASE | re.UNICODE)
en_comilla_dd = re.compile('″″([a-z\.\sA-Záéíóúñü]+)″″', re.IGNORECASE | re.UNICODE)


en_comilla_raras = re.compile('´([a-z\.A-Záéíóúñü]+)´', re.IGNORECASE | re.UNICODE)
en_comilla_ds_raras = re.compile('´´([a-z\.\sA-Záéíóúñü]+)´´', re.IGNORECASE | re.UNICODE)
en_comilla_ds_raras_ext1 = re.compile('´´´([a-z\.\sA-Záéíóúñü]+)´´', re.IGNORECASE | re.UNICODE)
en_comilla_ds_raras_inv = re.compile('``([a-z\.\sA-Záéíóúñü]+)``', re.IGNORECASE | re.UNICODE)

busqueda_verbose = False

def buscar_comillas_comunes(texto):
    
    encom = en_apostrofe_d.search(texto)
    if encom:
        a_reemplazar = "''"+encom.group(1)+"''"
        texto = texto.replace(a_reemplazar, '“'+encom.group(1)+'”')
        if busqueda_verbose:
            print(a_reemplazar, texto)
        
    encom = en_apostrofe.search(texto)
    if encom:        
        a_reemplazar = "'"+encom.group(1)+"'"
        texto = texto.replace(a_reemplazar, '“'+encom.group(1)+'”')
        if busqueda_verbose:
            print(a_reemplazar, texto)
        
    encom = en_doble_comilla.search(texto)
    if encom:
        a_reemplazar = '"'+encom.group(1)+'"'
        texto = texto.replace(a_reemplazar, '“'+encom.group(1)+'”')
        if busqueda_verbose:
            print(a_reemplazar, texto)
        
    return texto

def buscar_comillas(texto):
    encom = en_comilla_ds.search(texto)
    if encom:        
        a_reemplazar = '’’'+encom.group(1)+'’’'
        texto = texto.replace(a_reemplazar, '“'+encom.group(1)+'”')
        if busqueda_verbose:
            print(a_reemplazar, texto)

    encom = en_comilla.search(texto)
    if encom:
        a_reemplazar = '’'+encom.group(1)+'’'
        texto = texto.replace(a_reemplazar, '“'+encom.group(1)+'”')
        if busqueda_verbose:
            print(a_reemplazar, texto)
    return texto

def buscar_comillas_raras(texto):
    
    encom = en_comilla_ds_raras_ext1.search(texto)
    if encom:        
        a_reemplazar = '´´´'+encom.group(1)+'´´'
        texto = texto.replace(a_reemplazar, '“'+encom.group(1)+'”')
        if busqueda_verbose:
            print(a_reemplazar, texto)
        
    encom = en_comilla_ds_raras.search(texto)
    if encom:        
        a_reemplazar = '´´'+encom.group(1)+'´´'
        texto = texto.replace(a_reemplazar, '“'+encom.group(1)+'”')
        if busqueda_verbose:
            print(a_reemplazar, texto)
    
    encom = en_comilla_ds_raras_inv.search(texto)
    if encom:        
        a_reemplazar = '``'+encom.group(1)+'``'
        texto = texto.replace(a_reemplazar, '“'+encom.group(1)+'”')
        if busqueda_verbose:
            print(a_reemplazar, texto)

    encom = en_comilla_raras.search(texto)
    if encom:
        a_reemplazar = '´'+encom.group(1)+'´'
        texto = texto.replace(a_reemplazar, '“'+encom.group(1)+'”')
        if busqueda_verbose:
            print(a_reemplazar, texto)
    return texto

def buscar_comillas_dobles(texto):
    encom = en_comilla_dd.search(texto)
    if encom:        
        a_reemplazar = '″″'+encom.group(1)+'″″'
        texto = texto.replace(a_reemplazar, '“'+encom.group(1)+'”')
        if busqueda_verbose:
            print(a_reemplazar, texto)

    encom = en_comilla_doble.search(texto)
    if encom:
        a_reemplazar = '″'+encom.group(1)+'″'
        texto = texto.replace(a_reemplazar, '“'+encom.group(1)+'”')
        if busqueda_verbose:
            print(a_reemplazar, texto)
    return texto


def quitar_comillas(original):
    texto = buscar_comillas_comunes(original)
    texto = buscar_comillas(texto)
    texto = buscar_comillas_raras(texto)
    texto = buscar_comillas_dobles(texto)
    # Si queda algun apóstrofe o comillas dobles dando vuelta lo reemplazamos
    texto = texto.replace("'","’")
    texto = texto.replace('"',"’")
    if original != texto and busqueda_verbose:
        print(original,'---' , texto)
    return texto
    