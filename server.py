import logging

from pymodbus.datastore import ModbusSequentialDataBlock
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext
from pymodbus.device import ModbusDeviceIdentification
from pymodbus.server.sync import StartTcpServer
from twisted.internet.task import LoopingCall


def updating(a):
    print(a)


logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)

objects = 25
registers_per_object = 3
total_registers = objects * registers_per_object

store = ModbusSlaveContext(
    di=ModbusSequentialDataBlock(0, [17] * total_registers),
    co=ModbusSequentialDataBlock(0, [17] * total_registers),
    hr=ModbusSequentialDataBlock(0, [17] * total_registers),
    ir=ModbusSequentialDataBlock(0, [17] * total_registers)
)
context = ModbusServerContext(slaves=store, single=True)

identity = ModbusDeviceIdentification()
identity.VendorName = 'pymodbus'

loop = LoopingCall(f=updating, a=context)

loop.start(5, now=True)

StartTcpServer(context, identity=identity, address=("", 502))
