public class Main {
    public static void main(String[] args) {

        Biblioteca biblioteca1 = new Biblioteca("Biblioteca Central");
        Biblioteca biblioteca2 = new Biblioteca("Biblioteca Municipal");

        Libro libro1 = new Libro("Cien años de soledad", "Gabriel García Márquez", 1967);
        Libro libro2 = new Libro("Don Quijote de la Mancha", "Miguel de Cervantes", 1605);
        Libro libro3 = new Libro("El principito", "Antoine de Saint-Exupéry", 1943);
        Libro libro4 = new Libro("1984", "George Orwell", 1949);
        Libro libro5 = new Libro("La sombra del viento", "Carlos Ruiz Zafón", 2001);

        biblioteca1.agregarLibro(libro1);
        biblioteca1.agregarLibro(libro2);
        biblioteca1.agregarLibro(libro5);

        biblioteca2.agregarLibro(libro3);
        biblioteca2.agregarLibro(libro4);

        biblioteca1.mostrarLibros();
        biblioteca2.mostrarLibros();

        System.out.println("\n=== BUSCAR LIBRO ===");
        String libroBuscado = "El principito";
        Libro encontrado = biblioteca2.buscarLibroPorNombre(libroBuscado);
        if (encontrado != null) {
            System.out.println("¡Libro encontrado en la biblioteca '" + biblioteca2.getNombre() + "'!");
            encontrado.mostrarInfo();
        } else {
            System.out.println("El libro '" + libroBuscado + "' NO se encuentra en la biblioteca '" + biblioteca2.getNombre() + "'");
        }

        System.out.println("\n=== BIBLIOTECA CON MÁS LIBROS ===");
        Biblioteca[] bibliotecas = {biblioteca1, biblioteca2};
        
        int maxLibros = -1;

        for (Biblioteca b : bibliotecas) {
            if (b.getCantLibros() > maxLibros) {
                maxLibros = b.getCantLibros();
            }
        }
        
        System.out.println("Máxima cantidad de libros: " + maxLibros);
        for (Biblioteca b : bibliotecas) {
            if (b.getCantLibros() == maxLibros) {
                System.out.println("  - " + b.getNombre() + " (" + b.getCantLibros() + " libros)");
            }
        }
    }
}