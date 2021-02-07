# Subir y descargar archivos a S3

Para el script que vamos a usar, necesitamos tener [Python, PIP y Boto3](http://https://cloudaffaire.com/how-to-install-python-boto3-sdk-for-aws/ "Python y PIP") descargados. (En el link podemos ver como descargarlo según nuestro sistema operativo).

Tambien es necesario que tengamos instalado [AWS CLI.](http://https://aws.amazon.com/es/cli/ "AWS CLI")

Una vez instalado todo, vamos a configurar la consola de nuestra computadora ingresando: 

`aws configure`

Luego vamos a poner las credenciales: 

`AWS Access Key ID [ ]: `

`AWS Secret Access Key [ ]: `

`Default region name [ ]: `

`Default output format [None]:`

En el ultimo campo no hace falta poner nada.

### Script para subir archivos

Primero, importamos el package que vamos a usar:

    import boto3
Especificamos que vamos a estar usando en S3 y ponemos el nombre del bucket a donde vamos a querer subir nuestros archivos:

    s3 = boto3.resource("s3")
    BUCKET = "ml-worksample"
Despues, en el primer parametro, ponemos el nombre del archivo que queremos subir, en este caso **"Testworksample.py".** 
En el segundo parametro, vamos a poner el nombre de la carpeta a la que queremos subir el archivo y seguido del **"/"** ponemos el nombre con el que vamos a querer roconocer a nuestro archivo dentro del bucket. En este caso le dejamos el mismo nombre, pero podes cambiarlo.

    s3.Bucket(BUCKET).upload_file("Testworksample.py", "Archivos utilitarios/Testworksample.py")

### Script para descargar archivos

Para descargar, seguimos los mismos primeros pasos que en el script anterior:

    import boto3
    s3 = boto3.resource("s3")
    BUCKET = "ml-worksample"

En la ultima parte, en el primer parametro, vamos a poner el nombre de la carpeta en el bucket y seguido del **"/"** ponemos el nombre del archivo que queremos descargar. 
En el segundo parametro, ponemos como vamos a querer llamar al archivo, puede ser un nombre nuevo o el mismo. En este caso yo le puse uno nuevo **"Testworksamplecopy.py"**. 

    s3.Bucket(BUCKET).download_file( "Archivos Utilitarios/Testworksample.py", "Testworksamplecopy.py",)

### Consideraciones extra:

**Seguridad:** 
- Conocer las IP publicas (de los que necesitan usar el bucket), estando conectado a la VPN de Mercado Libre y habilitar en la politica del bucket solo esas IP. De esta forma, se accede por internet, pero solo aquellos que cumplen con estos requisitos pueden acceder y modificar el bucket.
- Tambien se puede usar el dar permisos a los grupos que correspondan y los usuarios se distribuyen en esos grupos.
- Tambien estan los PrivateLink, que nos dan una IP de nuestra VPC en AWS y todo el trafico que queremos manejar para ahi, lo rutea por adentro. 

**Funcionalidades**: 
- Esto de usar un script es mucho mas util para eventos en schedule. Por ejemplo, subimos un archivo a un bucket s3, dentro de ese bucket tenemos un evento que dispara una funcion lamdda, que con pyhton levanta el archivo del bucket s3 y se lo pasa el EC2. De ahi el EC2, lo procesa. 

- Los servicios de AWS Athena y AWS Redshift Spectrum, son buenos para consultar grandes cantidades de datos sin tener la necesidad de estar descargandolos. 
