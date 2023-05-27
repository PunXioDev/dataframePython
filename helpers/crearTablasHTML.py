def crearTabla(dataFrame, nombreTabla):
    archivoHTML = dataFrame.to_html()  # dataFrame a HTML
    # tengo un archivo HTML vacio
    archivo = open(f"./tablas/{nombreTabla}.html", "w", encoding="UTF-8")
    archivo.write(''' 
                  <!DOCTYPE html>
                  <html>
                  <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1">
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
                    <title>Tabla</title>
                  </head>
                  <body>
                  <main class="container-fluid">
                  ''')
    archivo.write(archivoHTML)
    archivo.write(''' 
                  </main>
                  </body>
                  </html>
                  ''')
    archivo.close()
