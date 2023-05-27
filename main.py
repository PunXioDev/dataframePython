from data.apartamentos import apartamento1,apartamento2

from helpers.crearTablasHTML import crearTabla

import pandas as pd 

#1.CREAR DATAFRAME

tabla1=pd.DataFrame(apartamento1,columns=['edades'])
tabla2=pd.DataFrame(apartamento2,columns=['edades'])
tabla3=pd.read_csv('./data/empleados.csv')


#efectuando filtro con python

#1. definir un condicion logica.

    # empleadosJovenesAnalistas1=tabla3.query("edad<28 and cargo=='analista1'")

    # empleadosSalarioBajo=tabla3.query("salario<5000000 and cargo=='analista2'")

    # empleadosADespedir=tabla3.query("edad>=50")

#2. creamos la tabla de html con el dataframe

    # crearTabla(empleadosJovenesAnalistas1, "tablaJovenes")

    # crearTabla(empleadosSalarioBajo, "tablaSalarioBajo")

    # crearTabla(empleadosADespedir, "tablaVacacionesIndefinidas")