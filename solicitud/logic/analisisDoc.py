import pika
from datetime import datetime

rabbit_host = '10.128.0.6'
rabbit_user = 'monitoring_user'
rabbit_password = 'isis2503'

connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=rabbit_host, 
        credentials=pika.PlainCredentials(rabbit_user, rabbit_password)))

channel = connection.channel()

channel.queue_declare(queue='creditos')
doc1 = 'Mario Castillo;2100000;1000612379;Apple;35;01/01/2022'
doc2 = 'Laura Torres;5400000;1000185263;Facebook;31;02/09/2021'
infoDocumentos=[doc1,doc2]

print('Mandando información de los documentos de los clientes. To exit press CTRL+C')

for i in infoDocumentos:
    channel.basic_publish(exchange='', routing_key='creditos', body=i)
    print("Se ha enviado la información de los documentos "+ i)

connection.close()
