import pandas , csv
from typing import List
import numpy as np



def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ['csv','xlsx']

def verificaciones(file, name: str):
    
    flash=[]
    print(f"Analizando {name}")
     
    
    filename,ftype= name.rsplit('.')
   
    
    
   
    if ftype == 'xlsx':
        df = pandas.read_excel(file, engine='openpyxl')
    elif ftype=='csv':
        df= pandas.read_csv(file)
    
    
    
   
    
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
                                             'ctx'],
        
        'mesas_certificados':['codeleccion'
                              , 'deseleccio',
                              'codcandidatura',
                              'descandida',
                              'coddepartamento',
                              'desdeparta',
                              'coddistrito',
                              'desdistrit',
                              'codzona',
                              'deszona',
                              'codlocal',
                              'deslocal',
                              'mesa',
                              'codseguridad',
                              'ctx']
        
        
        
        
    }
    
    
    
    types={'mesas':{'codeleccion':['int'],
        'deseleccion':['str'],
        'coddepartamento':['int'],
        'desdepartamento':['str'],
        'coddistrito':['int'],
        'desdistrito':['str'],
        'codzona':['int'],
        'deszona':['str'],
        'codlocal':['int'],
        'deslocal':['str'],
        'mesa':['int'],
        'tipo':['str'],
        'id_credencial' :['int']},
           
        'candidatos':{
            'IDCANDIDATO': ['int'],
            'CODCANDIDATURA': ['int'],
            'CODELECCION': ['int'],
            'CODDEPARTAMENTO':['int'],
            'CODDISTRITO': ['int'],
            'CODZONA': ['int'],
            'CODLISTA': ['int'],
            'ORDEN': ['int'],
            'NOMBRE': ['str'],},
        
        'candidaturas':{ 
            'codcandidatura': ['int'],
            'descripcion':['str'],
            'nivel':['str'],
            'nro_orden': ['int'],
            'tipo': ['int'],
            'descripcion_corta':['str'],
        },
        
        'listas':{
            'COD_ELECCION': ['int'],
            'CODLISTA':['int'],
            'DESCRIPCION': ['str'],
            'DESCRIPCION_CORTA':['str'],
            'NUMLISTA':['str','int'], 
            'NRO_ORDEN': ['int'], 
        },
        
        'mesas_candidaturas_seguridad_trep':{'codeleccio': ['int'],
                                             'deseleccio': ['str'],
                                             'cod_candid': ['int'],
                                             'descandida': ['str'],
                                             'coddeparta': ['int'],
                                             'desdeparta': ['str'],
                                             'coddistrit': ['int'],
                                             'desdistrit': ['str'],
                                             'codzona': ['int'],
                                             'deszona':['str'],
                                             'codlocal':['int'],
                                             'deslocal':['str'],
                                             'mesa':['int'],
                                             'codseguridad':['int'],
                                             'ctx':['int'],
                                             },
        
        'mesas_certificados':{'codeleccion': ['int'],
                              'deseleccio': ['str'],
                              'codcandidatura':['int'],
                              'descandida': ['str'],
                              'coddepartamento': ['int'],
                              'desdeparta':['str'],
                              'coddistrito': ['int'],
                              'desdistrit': ['str'],
                              'codzona': ['int'],
                              'deszona':['str'],
                              'codlocal':['int'],
                              'deslocal':['str'],
                              'mesa':['int'],
                              'codseguridad':['int'],
                              'ctx':['int'],}
        
            
            
            
            
        }
        
        
   
  
    # Analisis de titulos de las columnas
    for el in df.columns.to_list():
        if el not in tags_list[filename]:
            flash.append(f'el titulo "{el}"  de la columna no coincide con los titulos de la lista precisada. La lista debe contener los siguientes titulos de columna {tags_list[filename]}')
    
   # Analisis de cantidad de columnas
    if len(df.columns.to_list()) != len(tags_list[filename]):
        flash.append(f'El numero de columnas del archivo es de {len(df.columns.to_list())}, este deberia tener {len(tags_list[filename])}. Por favor revise el archivo')




    for el in tags_list[filename]:
        
        if filename != 'candidatos':
        ## Analisis de elementos NaN
            hasnull: bool = False
            for row in df[el]:
                if pandas.isna(row):
                    hasnull= True
            if hasnull:
                flash.append(f"{el} posee filas vacias")
        
        #Analisis de type (necesito que esten todas las filas llenas).
        
            # typo de datos permitidos
           
                #Correccion en caso de que el pandas me tome los numeros por floats
            if set([type(row) for row in df[el].to_list()]) == {float}:
                df[el].astype(int)
                    
                #verificacion que el tipo de datos es el esperado
            actual_types=list(set([type(row).__name__ for row in df[el].to_list()]))
            
            
            if not all(el for types[filename][el] in actual_types):
               flash.append(f'error en {el} sus datos de la columna {el}')
                
        else:
            for col in ['CODDEPARTAMENTO','CODDISTRITO','CODZONA']:
                df[col] = df[col].fillna(-1)
                df[col] = df[col].astype(int)
                df[col] = df[col].astype(str)
                df[col] = df[col].replace('-1', np.nan)
            
            
                    
                  
    
   
           
    
    
    if len(flash) > 0:
        return False, flash
    else: 
        df.to_csv(f'proyect/static/files/upload_files/{filename}.csv', index = False, header=True)
        flash.append("El Archivo fue cargado con exito")
        return True , flash
    
    
  