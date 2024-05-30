public class Biblioteca {

    public static void main(String[] args) {
        // Creación de objetos de la clase Libro
        Libro libro1 = new Libro(
                "El Principito", "Antoine de Saint-Exupéry",
                1943);
        Libro libro2 = new Libro(
                "Cien años de soledad", "Gabriel García Márquez",
                1967);

        // Mostrando la información de los libros
        System.out.println("Información del primer libro:");
        libro1.mostrarInformacion();

        System.out.println("\nInformación del segundo libro:");
        libro2.mostrarInformacion();
    }
    
}
