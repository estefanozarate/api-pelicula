import boto3
import uuid
import os

def lambda_handler(event, context):
    print(event)
    tenant_id = event['body']['tenant_id']
    pelicula_datos = event['body']['pelicula_datos']
    nombre_tabla = os.environ["TABLE_NAME"]
    uuidv4 = str(uuid.uuid4())
    pelicula = {
        'tenant_id': tenant_id,
        'uuid': uuidv4,
        'pelicula_datos': pelicula_datos
    }
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(nombre_tabla)
    response = table.put_item(Item=pelicula)
    print(pelicula) 
    return {
        'statusCode': 200,
        'pelicula': pelicula,
        'response': response
    }