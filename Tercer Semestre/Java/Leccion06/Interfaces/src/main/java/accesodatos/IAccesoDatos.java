package accesodatos;

public interface IAccesoDatos {
    int MAX_REGISTROS = 10;

    //Metodo insertar es asbtracto y sin cuerpo
    void insertar();

    void listar();

    void actualizar();

    void eliminar();
}