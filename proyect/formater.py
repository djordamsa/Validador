import pandas
from proyect.text_formater import quitar_comillas
import json

def paises(upload_directory:str):
    
    
    df= pandas.read_csv(f'{upload_directory}/mesas.csv')
    
    df_paises = pandas.DataFrame(columns=['id_pais','descripcion'])
    
    for index,row in df.iterrows():
        df_paises.at[index,'id_pais'] = row['codeleccion']
        df_paises.at[index,'descripcion'] = row['deseleccion']
    
    
    #df_paises['id_pais'] = row['codeleccio']
    #print(row['codeleccio'])
    df_paises = df_paises.drop_duplicates(subset ="id_pais")

    df_paises.to_csv ('proyect/static/files/formated_files/paises.csv', index = False, header=True)
    

def districtos(upload_directory):
    
    
    
    df= pandas.read_csv(f'{upload_directory}/mesas.csv')
    
    df_distritos = pandas.DataFrame(columns=['id_distrito','id_pais','descripcion'])

#voy por distritos el path de los distritos es pais.distrito - que viene dado por eleccion.departamento
    for index,row in df.iterrows():
        path_id = f"{row['codeleccion']}.{row['coddepartamento']}"
        id_pais = row['codeleccion']
    #print(path_id)
        df_distritos.at[index,'id_pais'] = row['codeleccion']
        df_distritos.at[index,'id_distrito'] = path_id
        df_distritos.at[index,'descripcion'] = row['desdepartamento'].replace("'", "’").replace("\n", " ")
    
    df_distritos = df_distritos.drop_duplicates(subset ="id_distrito")
    df_distritos.to_csv ('proyect/static/files/formated_files/distritos.csv', index = False, header=True)
    

def departamentos(upload_directory):
    
    
    
    df= pandas.read_csv(f'{upload_directory}/mesas.csv')
    
    df_departamentos = pandas.DataFrame(columns=['id_departamento','id_distrito','descripcion'])

    for index,row in df.iterrows():
        path_id = f"{row['codeleccion']}.{row['coddepartamento']}.{row['coddistrito']}"
        #id_departamento = row['coddistrit']
        df_departamentos.at[index,'id_departamento'] = path_id
        df_departamentos.at[index,'id_distrito'] = f"{row['codeleccion']}.{row['coddepartamento']}"
        df_departamentos.at[index,'descripcion'] = row['desdistrito'].replace("'", "’").replace("\n", " ")

    
    
    df_departamentos = df_departamentos.drop_duplicates(subset ="id_departamento")
    df_departamentos.to_csv ('proyect/static/files/formated_files/departamentos.csv', index = False, header=True)
    

def localidades(upload_directory):
    
    
    
    df= pandas.read_csv(f'{upload_directory}/mesas.csv')
        
    df_localidades = pandas.DataFrame(columns=['id_localidad','id_departamento','descripcion'])

    for index,row in df.iterrows():
        path_id = f"{row['codeleccion']}.{row['coddepartamento']}.{row['coddistrito']}.{row['codzona']}"
        df_localidades.at[index,'id_localidad'] = path_id
        df_localidades.at[index,'id_departamento'] = f"{row['codeleccion']}.{row['coddepartamento']}.{row['coddistrito']}"
        df_localidades.at[index,'descripcion'] = row['deszona'].replace("'", "’").replace("\n", " ")
    


    df_localidades = df_localidades.drop_duplicates(subset ="id_localidad")
    df_localidades.to_csv ('proyect/static/files/formated_files/localidades.csv', index = False, header=True)
    


def establecimientos(upload_directory):
    
    
    
    df= pandas.read_csv(f'{upload_directory}/mesas.csv')
        
    df_establecimientos = pandas.DataFrame(columns=['id_establecimiento','id_localidad','descripcion','nro_escuela','latitud','longitud','domicilio','telefono','nombre_directivo','ciudadanos_habilitados'])

    for index,row in df.iterrows():
        path_id = f"{row['codeleccion']}.{row['coddepartamento']}.{row['coddistrito']}.{row['codzona']}.{row['codlocal']}"
        df_establecimientos.at[index,'id_establecimiento'] = path_id
        df_establecimientos.at[index,'nro_escuela'] = row['codlocal']
        df_establecimientos.at[index,'ciudadanos_habilitados'] = 0 #row['electores']
        df_establecimientos.at[index,'id_localidad'] = f"{row['codeleccion']}.{row['coddepartamento']}.{row['coddistrito']}.{row['codzona']}"
        df_establecimientos.at[index,'descripcion'] = row['deslocal'].replace("'", "’").replace("\n", " ")
    
    df_establecimientos = df_establecimientos.drop_duplicates(subset ="id_establecimiento")

    df_establecimientos.to_csv ('proyect/static/files/formated_files/establecimientos.csv', index = False, header=True)
    
    

def mesas(upload_directory):
    
    
    
    df= pandas.read_csv(f'{upload_directory}/mesas.csv')
        
    df_mesas_output = pandas.DataFrame(columns=['id_mesa','id_establecimiento','nro_mesa','sexo','tipo','extranjera','ciudadanos_habilitados'])

    id_mesa = 0

    for index,row in df.iterrows():
        path_id = f"{row['codeleccion']}.{row['coddepartamento']}.{row['coddistrito']}.{row['codzona']}.{row['codlocal']}.{row['mesa']}"
        df_mesas_output.at[index,'nro_mesa'] = path_id
        df_mesas_output.at[index,'sexo'] = 'X'
        df_mesas_output.at[index,'tipo'] = 'Electronica'
        df_mesas_output.at[index,'extranjera'] = 'SI' if row['tipo'] == 'MAYORES' else 'NO'
        df_mesas_output.at[index,'ciudadanos_habilitados'] = 500
        df_mesas_output.at[index,'id_mesa'] = id_mesa
        df_mesas_output.at[index,'id_establecimiento'] =  f"{row['codeleccion']}.{row['coddepartamento']}.{row['coddistrito']}.{row['codzona']}.{row['codlocal']}"
        id_mesa += 1
    
    df_mesas_output = df_mesas_output.drop_duplicates(subset ="nro_mesa")
    df_mesas_output.to_csv('proyect/static/files/formated_files/mesas.csv', index = False, header=True)
    
    
def listas(upload_directory):
    
    df= pandas.read_csv(f'{upload_directory}/listas.csv',dtype=str).fillna('')
   

   

    # Paso los encabezados a minusculas 
    df.columns = [c.lower() for c in df.columns]
    
    
    df_listas_output = pandas.DataFrame(columns=['id_lista','id_partido','descripcion','texto_asistida','descripcion_corta','nro_lista','color','color_tipografia','color_api_resultados','nro_orden'])

    listas = []
    for index,row in df.iterrows():
        
        ##codlista esta compuesta por ints o str , strip no funciona con ints.
        ## cod_lista = row['codlista'].strip() 
        ## no entiendo bien que se buscaba aca, sacarle los espacios?
        cod_lista = row['codlista'].strip()
       
        if cod_lista not in df_listas_output['id_lista'].to_list():
            data = ''
            if 'presidente' in row and row['presidente'].strip() != '':
                data = json.dumps({
                    'presidente': quitar_comillas(row['presidente']),
                    'vice_1': quitar_comillas(row['vice_1']),
                    'vice_2': quitar_comillas(row['vice_2']),
                 })
        
            # Agrega el color si fueron establecidos lo 3 colores R,G y B
            color = None
            color_tipografia = ''
            if 'color_r' in row and 'color_g' in row and 'color_b' in row:
                try:
                    color = '#%02x%02x%02x' % (int(row['color_r']), int(row['color_g']), int(row['color_b']))
                
                    # Color de la tipografía en base al fondo, para que haya contraste
                    thresh = round(((int(row['color_r']) * 299) + (int(row['color_g']) * 587) + (int(row['color_b']) * 114)) /1000)                
                    if thresh <= 125:
                        color_tipografia = '#ffffff'
                    else:
                        color_tipografia = '#000000'
                    
                except:
                    #print('Alguno de los colores no fue establecido para la lista',row['codlista'])
                    color_tipografia = '#000000'
                    pass
            else:
                color_tipografia = '#000000'
            
            nueva_descripcion = quitar_comillas(row['descripcion'])
            if nueva_descripcion == '':
                print('La descripcion de la lista',row['codlista'],'esta vacía.')
            nueva_descripcion_corta = quitar_comillas(row['descripcion_corta'])
            if nueva_descripcion_corta == '':
                print('La descripcion corta de la lista',row['codlista'],'esta vacía.')
            new_row = {
                'id_lista': cod_lista,
                'id_partido': '',
                'descripcion': nueva_descripcion,
                'texto_asistida': row['numlista'] +' - '+ nueva_descripcion,
                'descripcion_corta': nueva_descripcion_corta,
                'nro_lista': row['numlista'],
                'color': color,
                'color_tipografia': color_tipografia,
                'color_api_resultados': '',
                'nro_orden': row['nro_orden'],
                'data': data
                }
        
            listas.append(new_row)
        
    df_listas_output = pandas.DataFrame.from_dict(listas)
    df_listas_output.to_csv('proyect/static/files/formated_files/listas.csv', index = False, header=True)
    #df_listas_output[df_listas_output.duplicated('id_lista', keep=False)].to_csv('/tmp/errores_listas_duplicadas.csv')
    #assert len(df_listas_output[df_listas_output.duplicated('id_lista', keep=False)]) == 0, 'Existen listas duplicadas, consultar /tmp/errores_listas_duplicadas.csv'
    
    

def candidatos(upload_directory, formated_directory):
    
    def get_ubicacion(nivel, nivel_para, dep, dis, zona, elec):
        if nivel == nivel_para:
            if nivel == 'NACIONAL':
                return str(elec)
            elif nivel == 'DEPARTAMENTO':
                return '.'.join([str(elec), dep])
            elif nivel == 'DISTRITO':
                return '.'.join([str(elec), dep, dis])
            elif nivel == 'ZONA':
                return '.'.join([str(elec), dep, dis, zona])
        return ''
        
        
    df_candidaturas = pandas.read_csv(f'{upload_directory}/candidaturas.csv', dtype=str).fillna('')
    candidaturas = {}
    for index,row in df_candidaturas.iterrows():
        candidaturas[row['codcandidatura']] = {
            'descripcion': row['descripcion'],
            'descripcion_corta': row['descripcion_corta'],
            'nivel': row['nivel'],
            'nro_orden': row['nro_orden'],
            'tipo': row['tipo']
        }
        
    df_candidatos = pandas.read_csv(f'{upload_directory}/candidatos.csv', dtype=str).fillna('')

    # Paso los encabezados a minusculas 
    df_candidatos.columns = [c.lower() for c in df_candidatos.columns]

    df_candidatos_output = pandas.DataFrame(columns=['id_candidato','id_lista','id_cargo','id_pais',
                                                    'id_distrito','id_departamento','id_localidad',
                                                    'nombre','nro_orden','sexo','dni','texto_asistida','titular'])

    log_errores_candidatos = open('/tmp/errores_candidatos.txt', mode='w', encoding='utf-8')

    nros_orden_candidatos = {}

    claves_existente = []
    candidatos = []
    
    df_paises=pandas.read_csv(f'{formated_directory}/paises.csv', dtype=str)
    lista_id_pais = df_paises['id_pais'].to_list()
    
    df_distritos=pandas.read_csv(f'{formated_directory}/distritos.csv', dtype=str)
    lista_id_distrito = df_distritos['id_distrito'].to_list()
    
    df_departamentos=pandas.read_csv(f'{formated_directory}/departamentos.csv', dtype=str)
    lista_id_departamento = df_departamentos['id_departamento'].to_list()
    
    df_localidades=pandas.read_csv(f'{formated_directory}/localidades.csv', dtype=str)
    lista_id_localidad = df_localidades['id_localidad'].to_list()

    for index,row in df_candidatos.iterrows():
        nivel = candidaturas[row['codcandidatura']]['nivel']
        id_pais = get_ubicacion(nivel, 'NACIONAL', row['coddepartamento'], row['coddistrito'], row['codzona'], row['codeleccion'])
        id_distrito = get_ubicacion(nivel, 'DEPARTAMENTO', row['coddepartamento'], row['coddistrito'], row['codzona'], row['codeleccion'])
        id_departamento = get_ubicacion(nivel, 'DISTRITO', row['coddepartamento'], row['coddistrito'], row['codzona'], row['codeleccion'])
        id_localidad = get_ubicacion(nivel, 'ZONA', row['coddepartamento'], row['coddistrito'], row['codzona'], row['codeleccion'])
        
        if id_pais != '' and id_pais not in lista_id_pais:
            msj = 'El id candidato '+ row['idcandidato']+' se encuentra asociado a una ELECCION '+id_pais+' que no existe en el archivo de mesas.'
            print(msj)
            log_errores_candidatos.write(msj+'\n')
            continue
        
        if id_distrito != '' and id_distrito not in lista_id_distrito:
            msj = 'El id candidato '+row['idcandidato']+' se encuentra asociado a un DEPARTAMENTO '+id_distrito+' que no existe en el archivo de mesas.'
            print(msj)
            log_errores_candidatos.write(msj+'\n')
            continue
        
        if id_departamento != '' and id_departamento not in lista_id_departamento:
            msj = 'El id candidato '+ row['idcandidato']+ ' se encuentra asociado a un DISTRITO '+ id_departamento+ ' que no existe en el archivo de mesas.'
            print(msj)
            log_errores_candidatos.write(msj+'\n')
            continue
        
        if id_localidad != '' and id_localidad not in lista_id_localidad:
            msj = 'El id candidato '+ row['idcandidato']+ ' se encuentra asociado a una ZONA '+ id_localidad+ ' que no existe en el archivo de mesas.'
            print(msj)
            log_errores_candidatos.write(msj+'\n')
            continue
        
        id_lista = row['codlista']
        candidatura = candidaturas[row['codcandidatura']]['descripcion']
        id_cargo = candidaturas[row['codcandidatura']]['descripcion_corta']
        clave_lista = (id_pais, id_distrito, id_departamento, id_localidad, id_lista, id_cargo)
            
        if row['orden'] == '0':
            print('El id candidato', row['idcandidato'], 'tiene orden 0')
            
        nro_orden = row['orden']
        
        clave_preferente = (id_pais, id_distrito, id_departamento, id_localidad, id_lista, id_cargo, nro_orden)
        if clave_preferente in claves_existente:
            ubicacion = None
            for c in clave_preferente[:4]:
                if c != '':
                    ubicacion = c
            msj = 'El candidato con id '+ row['idcandidato']+ ' pisa otro candidato para la Ubicacion '+ \
                        ubicacion+ ' Candidatura '+ candidatura+ ' Lista '+ id_lista+ ' Nro de orden' + nro_orden
            print(msj)
            log_errores_candidatos.write(msj+'\n')
            continue
        else:
            claves_existente.append(clave_preferente)
        
        # TODO Hay que corregir enrique tercero en asistida porque va a pisar el arreglo hecho para el juego v12
        #exit(0)
        nuevo_nombre = quitar_comillas(row['nombre'])
        
        # Capitaliza el nombre
        #nuevo_nombre = ' '.join([x.capitalize() for x in nuevo_nombre.split(' ')])
        #EL-7578 Candidatos con apodos en minúscula deben estar con Mayúsculas
        nuevo_nombre = ' '.join([x.capitalize() if "“" not in x else x for x in nuevo_nombre.split(' ')])

        
        new_row = {
            'id_candidato': index,
            'id_lista': id_lista,
            'id_cargo': id_cargo,
            'id_pais': id_pais,
            'id_distrito': id_distrito,
            'id_departamento': id_departamento,
            'id_localidad': id_localidad,
            'nombre': nuevo_nombre,
            'nro_orden': nro_orden,
            #'sexo': row['sexo'],
            'sexo': '',
            'dni': row['idcandidato'],
            'texto_asistida': nuevo_nombre,
            'titular': "SI"
        }        
        candidatos.append(new_row)
        
        
    df_candidatos_output = pandas.DataFrame.from_dict(candidatos)
    df_candidatos_output.to_csv (f'{formated_directory}/candidatos.csv', index = False, header=True)
    
    
    
def cargos(upload_directory):
    
    df_candidaturas = pandas.read_csv(f'{upload_directory}/candidaturas.csv', dtype=str).fillna('')
    candidaturas = {}
    for index,row in df_candidaturas.iterrows():
        candidaturas[row['codcandidatura']] = {
        'descripcion': row['descripcion'],
        'descripcion_corta': row['descripcion_corta'],
        'nivel': row['nivel'],
        'nro_orden': row['nro_orden'],
        'tipo': row['tipo']
    }
    
    
    
    
    
    df_cargos_msa = pandas.DataFrame(columns=['id_cargo',
                                            'id_cargo_descriptivo',
                                            'descripcion',
                                            'nro_orden',
                                            'descripcion_corta',
                                            'texto_asistida',
                                            'max_selecciones',
                                            'consulta_popular',
                                            'cargo_ejecutivo',
                                            'id_grupo',
                                            'preferente',
                                            'tachas',
                                            'max_tachas',
                                            'max_preferencias'])

    def get_des_corta(descr):
            res = ''
            partes = descr.split(' ')
            for p in partes:
                if len(p) > 2:
                    res += p[:2]+'. '
            res = res.strip()[:20]
            if len(res) > 20:
                raise Exception('Exc')
            return res
        
    # tipo 1 es lista cerrada (lo que nosotros llamamos ejecutivo)
    id_grupo = 1
    
    for _,cand in candidaturas.items():
        candidatura = cand['descripcion']
        tipo_candidatura = cand['tipo']
        id_cargo = cand['descripcion_corta']
        
        new_row = {
            'id_cargo': id_cargo,
            'id_cargo_descriptivo': id_cargo,
            'descripcion': candidatura.strip(),
            'nro_orden': id_grupo,
            'descripcion_corta': id_cargo,
            'texto_asistida': candidatura.strip(),
            'max_selecciones': '1',
            'consulta_popular': 'NO',
            'cargo_ejecutivo': 'SI' if tipo_candidatura == '1' else 'NO',
            'id_grupo': id_grupo,
            'preferente': 'NO' if tipo_candidatura == '1' else 'SI',
            'tachas': 'NO',
            'max_tachas':'',
            'max_preferencias': '' if tipo_candidatura == '1' else '1'
        }
        id_grupo += 1

        df_cargos_msa = df_cargos_msa.append(new_row, ignore_index=True)

    df_cargos_msa.to_csv('proyect/static/files/formated_files/cargos.csv', index = False, header=True)
   