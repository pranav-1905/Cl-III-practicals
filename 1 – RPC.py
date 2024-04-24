# 1 – RPC 
# SERVER

import xmlrpc.server
from xmlrpc.server import SimpleXMLRPCRequestHandler
class FactorialServer:
    def calculate_factorial(self, n):
       if n < 0:
          raise ValueError("Input must be a non-negative integer.")
       result = 1
       for i in range(1, n + 1):
          result *= i
       return result
# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
 rpc_paths = ('/RPC2',)
# Create server
with xmlrpc.server.SimpleXMLRPCServer(('localhost', 8000),
         requestHandler=RequestHandler) as server:
     server.register_introspection_functions()
     # Register the FactorialServer class
     server.register_instance(FactorialServer())
     print("FactorialServer is ready to accept requests.")
     # Run the server's main loop
     server.serve_forever()


CLIENT
import xmlrpc.client
# Create an XML-RPC client
with xmlrpc.client.ServerProxy("http://localhost:8000/RPC2") as proxy:
    try:
        # Replace 5 with the desired integer value
        input_value = 5
        result = proxy.calculate_factorial(input_value)
        print(f"Factorial of {input_value} is: {result}")
    except Exception as e:
        print(f"Error: {e}")