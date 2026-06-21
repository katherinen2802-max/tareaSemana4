from modelos.cliente import Cliente
from modelos.producto import Producto
from servicios.restaurante import Restaurante

cliente = Cliente (
    "Juan Perez", 
    "juanPerez@gmail.com"
    )

producto = Producto (
    "Pizza",
    "Coca-Cola"
)

restaurante = Restaurante()

restaurante.agregar_cliente(cliente)
restaurante.agregar_producto(producto)

print("=== CLIENTES INGRESADOS ===")
restaurante.mostrar_clientes()

print("=== PRODUCTOS VENDIDOS ===")
restaurante.mostrar_productos()