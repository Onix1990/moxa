import logging

from pymodbus.client.sync import ModbusTcpClient as ModbusClient

logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)

client = ModbusClient('192.168.127.254', 4001)

client.connect()

request = client.read_input_registers(40012, 1)
print(request)

client.close()
