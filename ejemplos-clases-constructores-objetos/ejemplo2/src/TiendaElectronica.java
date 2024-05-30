// Clase principal que contiene el método main
public class TiendaElectronica {
    public static void main(String[] args) {
        // Creación de objetos de la clase ProductoElectronico
        ProductoElectronico producto1 = new ProductoElectronico(
                "Smartphone", 599.99, "Samsung");
        ProductoElectronico producto2 = new ProductoElectronico(
                "Tablet", 349.99, "Apple");

        // Mostrando la información de los productos
        System.out.println("Información del primer producto:");
        producto1.mostrarInformacion();

        System.out.println("\nInformación del segundo producto:");
        producto2.mostrarInformacion();
    }
}