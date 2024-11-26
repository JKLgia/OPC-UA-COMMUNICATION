from opcua import Client, ua
import time

# OPC UA server URL
url = "opc.tcp://<PLC_IP>:<PORT>"

# Connect to the OPC UA server
client = Client(url)
client.set_user("<USERNAME>")
client.set_password("<PASSWORD>")

try:
    client.connect()
    print("Connected to OPC UA server")

    # Define the node IDs for reading and writing
    read_node_id = "ns=2;s=DB1,Real1"
    write_node_id = "ns=2;s=DB1,Real2"

    # Read value from PLC
    read_node = client.get_node(read_node_id)
    read_value = read_node.get_value()
    print(f"Read value: {read_value}")

    # Write value to PLC
    write_node = client.get_node(write_node_id)
    new_value = 123.45
    write_node.set_value(ua.DataValue(ua.Variant(new_value, ua.VariantType.Float)))
    print(f"Wrote value: {new_value}")

    # Keep the connection open for a while
    time.sleep(10)

finally:
    client.disconnect()
    print("Disconnected from OPC UA server")