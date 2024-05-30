// Definición de la clase ProductoElectronico
class ProductoElectronico {
    // Atributos
    String nombre;
    double precio;
    String marca;

    // Constructor
    public ProductoElectronico(String nombre, double precio, String marca) {
        this.nombre = nombre;
        this.precio = precio;
        this.marca = marca;
    }

    // Método para mostrar la información del producto
    public void mostrarInformacion() {
        System.out.println("Nombre: " + nombre);
        System.out.println("Marca: " + marca);
        System.out.println("Precio: $" + precio);
    }
}