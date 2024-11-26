from opcua import Client, ua

# OPC-UA server URL
url = "opc.tcp://192.168.0.1:4840"

# Create a client instance
client = Client(url)

try:
    # Connect to the OPC-UA server
    client.connect()
    print("Connected to OPC-UA server")

    # Read a variable from the PLC
    node = client.get_node("ns=3;s=\"DB137\".\"DATA_1\"")  # Replace with the correct node ID
    value = node.get_value()
    print(f"Value from PLC: {value}")

    # Write a value to the PLC
    new_value = value - 5  # Replace with the value you want to write
    node.set_value(ua.DataValue(ua.Variant(new_value, ua.VariantType.Int16)))
    print(f"New value written to PLC: {new_value}")

finally:
    # Disconnect from the OPC-UA server
    client.disconnect()
    print("Disconnected from OPC-UA server")