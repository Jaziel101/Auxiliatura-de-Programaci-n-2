public class Biblioteca {
    private String nombre;
    private int cantLibros;
    private Libro[] libros;
    private static final int MAX_LIBROS = 100;

    // Constructor
    public Biblioteca(String nombre) {
        this.nombre = nombre;
        this.cantLibros = 0;
        this.libros = new Libro[MAX_LIBROS];
    }

    public boolean agregarLibro(Libro libro) {
        if (cantLibros < MAX_LIBROS) {
            libros[cantLibros] = libro;
            cantLibros++;
            System.out.println("Libro '" + libro.getNombre() + "' agregado a la biblioteca '" + nombre + "'");
            return true;
        } else {
            System.out.println("No hay espacio para más libros en la biblioteca '" + nombre + "'");
            return false;
        }
    }

    public Libro buscarLibroPorNombre(String nombreBuscado) {
        for (int i = 0; i < cantLibros; i++) {
            if (libros[i].getNombre().equalsIgnoreCase(nombreBuscado)) {
                return libros[i];
            }
        }
        return null;
    }

    public void mostrarLibros() {
        System.out.println("\n=== BIBLIOTECA: " + nombre.toUpperCase() + " ===");
        if (cantLibros == 0) {
            System.out.println("  No hay libros registrados.");
        } else {
            for (int i = 0; i < cantLibros; i++) {
                libros[i].mostrarInfo();
            }
        }
        System.out.println("Total de libros: " + cantLibros);
    }

    // Getters
    public String getNombre() {
        return nombre;
    }

    public int getCantLibros() {
        return cantLibros;
    }
}