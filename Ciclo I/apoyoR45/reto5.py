import json
import pandas as pd
import numpy as np

def preProcesado (DF):
    # Funcion que prepara las categorias en un DF para ser codificadas en la matriz
    # Devuelve tambien las categorias en una lista
    categoriesDF = DF['categories']. apply (pd. Series )
    categoriesDF ['title'] = DF['title']
    categoriesDF = categoriesDF . drop_duplicates ([ 'title'])
    categoriesDF . set_index ('title', inplace = True )
    categories = [ categoriesDF [ categorie ]. unique () for categorie in categoriesDF .
    columns ]
    categories = [ categorie for lista in categories for categorie in lista if all
    ([ pd. isnull ( categorie ) == False , categorie != ' ', categorie != '', len (
    str ( categorie )) > 1]) ]
    categories = list ( set ( categories ))
    return categoriesDF , categories

def codificaMatriz (DF , categories : list , producto : list ):
    # Funcion que inserta unos en la matriz
    # Su codigo aqui
    mCategories = pd.DataFrame(
        np.zeros((len(categories), len(producto))),
        index=categories,
        columns=list(producto)
    )

    for book in DF.index:
        for index in DF:
            categorie = DF[index][book]
            if categorie in categories:
                mCategories[book][categorie] = 1

    return mCategories# Debe retornar un DF como el de la Tabla 1.

def recomiendaLibro ( url_puntuacion :str , url_perfil :str , url_recomendacion : str )->json :
    
    librosPuntuacion = pd.read_csv(url_puntuacion, sep=';', names=['titulo','puntuacion'], index_col=['titulo'])

    dataPerfil = pd.read_json(url_perfil)
    dataPerfil, categoriesPuntuacion = preProcesado(dataPerfil)

    librosPuntuacion = dataPerfil.index

    mCategories = codificaMatriz(dataPerfil, categoriesPuntuacion, librosPuntuacion)

    for book in mCategories.columns:
        if book in librosPuntuacion.index:
            mCategories[book] = mCategories[book].apply(lambda punto: float(punto * librosPuntuacion['puntuacion'][book]))
    
    mCategories['perfilUsuario'] = [mCategories.loc[categorie,:].sum() for categorie in mCategories.index]
    mCategories['perfilUsuario'] = mCategories['perfilUsuario'].apply(lambda punto: punto / mCategories['perfilUsuario'].sum())
    print(mCategories)

    #------------

    return json.dumps(solucion, indent=4)

recomiendaLibro('https://raw.githubusercontent.com/iam3mer/defioC1MTIC2022/main/reto5/pointBook_1.csv', 'https://git.io/JZrOh', 'https://git.io/JZr32')
