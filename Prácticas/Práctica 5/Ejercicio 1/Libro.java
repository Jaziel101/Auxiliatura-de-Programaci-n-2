public class Libro {
    private String nombre;
    private String autor;
    private int año;

    // Constructor
    public Libro(String nombre, String autor, int año) {
        this.nombre = nombre;
        this.autor = autor;
        this.año = año;
    }

    // Getters
    public String getNombre() {
        return nombre;
    }

    public String getAutor() {
        return autor;
    }

    public int getAño() {
        return año;
    }

    public void mostrarInfo() {
        System.out.println("  - " + nombre + " | Autor: " + autor + " | Año: " + año);
    }
}