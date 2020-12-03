from zeep import Client

client = Client(wsdl='http://www.dneonline.com/calculator.asmx?wsdl')
# print(client.service.Multiply(10,3))