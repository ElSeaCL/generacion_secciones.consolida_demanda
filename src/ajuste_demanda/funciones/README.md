# Modulo de funciones

Este package contiene las distintas funciones utilizadas en el proceso de ajuste de demandas.

Se dividen en funciones de evaluación, encargadas de determinar si la demanda requiere de un ajuse; funciones de filtro, encargadas de filtrar las demandas que cumplen con la condición de ajuste y funciones de valores, encargadas de obtener el valor a modificar.

Para cumplir con la definición de una función nueva los requerimientos son:

- Su nombre debe empezar con *fn*
- Sebe registrarse un nombre informal. Este se utiliza para asociar a la función en el archivo de configuración. Para registrar este nombre se hace uso del decorador `@registro` almacenado en la carpeta utils.
