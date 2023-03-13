import pandas , csv




def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ['cvs','xlsx']

def verificaciones(file, filename: str):
    df = pandas.read_excel(file, engine='openpyxl')
    
    
    
    filename= filename.split('.')[0]
    print(filename)
    flash=[]
    tags_list={
        'mesas':['codeleccion',
                'deseleccion',
                'coddepartamento',
                'desdepartamento',
                'coddistrito',
                'desdistrito',
                'codzona',
                'deszona',
                'codlocal',
                'deslocal',
                'mesa',
                'tipo',
                'id_credencial'],
        
        'candidatos':['IDCANDIDATO',
                    'CODCANDIDATURA',
                    'CODELECCION',
                    'CODDEPARTAMENTO',
                    'CODDISTRITO',
                    'CODZONA',
                    'CODLISTA',
                    'ORDEN',
                    'NOMBRE'],
        
        'candidaturas': ['codcandidatura',
                    'descripcion',
                    'nivel',
                    'nro_orden',
                    'tipo',
                    'descripcion_corta'],
        
        'listas':['COD_ELECCION',
                  'CODLISTA',
                  'DESCRIPCION',
                  'DESCRIPCION_CORTA',
                  'NUMLISTA',
                  'NRO_ORDEN'],
        
        'mesas_candidaturas_seguridad_trep':['codeleccio',
                                             'deseleccio',
                                             'cod_candid',
                                             'descandida',
                                             'coddeparta',
                                             'desdeparta',
                                             'coddistrit',
                                             'desdistrit',
                                             'codzona',
                                             'deszona',
                                             'codlocal',
                                             'deslocal',
                                             'mesa',
                                             'codseguridad',
                                             'ctx']
        
        
        
        
    }
    
    
    
    types={'mesas':{'codeleccion': int,
        'deseleccion': str,
        'coddepartamento': int,
        'desdepartamento': str,
        'coddistrito': int,
        'desdistrito':str,
        'codzona':int,
        'deszona': str,
        'codlocal': int,
        'deslocal': str,
        'mesa': int,
        'tipo': str,
        'id_credencial' : int},
           
        'candidatos':{
            'IDCANDIDATO': int,
            'CODCANDIDATURA': int,
            'CODELECCION': int,
            'CODDEPARTAMENTO':int,
            'CODDISTRITO': int,
            'CODZONA': int,
            'CODLISTA': int,
            'ORDEN': int,
            'NOMBRE': str,},
        
        'candidaturas':{ 
            'codcandidatura': int,
            'descripcion':str,
            'nivel':str,
            'nro_orden': int,
            'tipo': int,
            'descripcion_corta':str,
        },
        
        'listas':{
            'COD_ELECCION': int,
            'CODLISTA':int,
            'DESCRIPCION': str,
            'DESCRIPCION_CORTA':str,
            'NUMLISTA':str, 
            'NRO_ORDEN': int, 
        },
        
        'mesas_candidaturas_seguridad_trep':{'codeleccio': int,
                                             'deseleccio': str,
                                             'cod_candid': int,
                                             'descandida': str,
                                             'coddeparta': int,
                                             'desdeparta': str,
                                             'coddistrit': int,
                                             'desdistrit': str,
                                             'codzona': int,
                                             'deszona':str,
                                             'codlocal':int,
                                             'deslocal':str,
                                             'mesa':int,
                                             'codseguridad':int,
                                             'ctx':int,
                                             },
        
            
            
            
            
        }
        
        
        
        
           
           
  
    
    for el in df.columns.to_list():
        if el not in tags_list[filename]:
            flash.append(f'el titulo "{el}"  de la columna no coincide con los titulos de la lista precisada')
            flash.append(f'La lista debe contener los siguientes titulos de columna {tags_list[filename]}')
    
   
    if len(df.columns.to_list()) != len(tags_list[filename]):
        flash.append(f'El numero de columnas del archivos mesas.xlsx es de {len(df.columns.to_list())}, este deberia tener {len(tags_list[filename])}. Por favor revise el archivo')


    ## aca hay un error cuando en el excel hay 0, al pasarlos a pandas me toma como que son float y marcaria error.
    ## que recomendarias hacer en este caso??
    for el in tags_list[filename]:
        if len(set([type(row) for row in df[el].to_list()])) == 1:
            if types[filename][el] in set([type(row) for row in df[el].to_list()]):
                pass
            else:
                flash.append(f'error en {el} sus datos deberian ser {types[filename][el]}')
        else:
            flash.append(f'error en {el}, hay mas de un tipo de datos en la columna')
            
    
    if len(flash) > 0:
        return False, flash
    else: 
        return True , "Archivo cargado con exito"