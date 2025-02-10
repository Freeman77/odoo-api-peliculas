# Módulo de Gestión de Películas en Odoo

## Descripción

Módulos de Gestión de Películas en Odoo (16.0)

- movie_management: Permite gestionar películas, incluyendo su nombre y ranking.

- movie_sync: Obtiene información de películas desde el servicio externo [Random Data API - Películas](https://random-data-api.com/api/v3/projects/a2bebcc5-69e3-4b4e-b8c0-4a2f4306f0da), cada 1 minuto (requiere API key).

- movie_api: Expone un endpoint REST (/api/top_movies) que entrega un Top 10 de películas, basado en el módulo [Base Rest](https://github.com/OCA/rest-framework/tree/16.0/base_rest) de la OCA.

## Para iniciar el proyecto en modo producción

1. Es requisito tener instalado [Docker](https://www.docker.com/)

2. Construir contenedor de Odoo 16 con paquetes python adicionales

    ```console
    docker compose build
    ```

3. Iniciar contenedores en modo desacoplado

    ```console
    docker compose up -d
    ```

## Instalación y Configuración

1. Una vez iniciado, Odoo estará disponible en la URL: [http://localhost:8069]

2. Para el primer inicio, se debe crear una nueva base de datos.

3. Luego iniciamos sesión como admin.

4. En el menú 'Aplicaciones', buscar e instalar los módulos:
    - movie_management
    - movie_sync
    - movie_api

5. Ingresar en modo desarrollador al menú "Ajustes > Técnico > Parámetros del sistema", buscar la llave 'movie_sync.api_key' e ingresar su key.

6. Ingresar en modo desarrollador al menú "Ajustes > Técnico > Acciones planificadas" y activar la acción 'Obtener Películas desde Random-Data-API'.

7. Una vez configurado, el endpoint [http://localhost:8069/api/top_movies] comenzará a responder con el top 10 de películas.

## Cómo ejecutar Pruebas

### Para probar la funcionalidad del cron

- Posterior a la instalación del módulo 'movie_sync' se debe activar la acción planificada (cron) con nombre "Obtener Películas desde Random-Data-API", ya sea manualmente o marcando el toggle a "Activo".

- Ejecutar el siguiente comando para revisar los logs que muestran el flujo de creación de películas en la base de Odoo.

    ```console
    docker compose logs odoo -f
    ```

### Para probar el endpoint 

- Posterior a la instalación del módulo 'movie_api' será posible realizar solicitudes GET al endpoint
[http://localhost:8069/api/top_movies]

- Es posible acceder al endpoint simplemente con un navegador web (Chrome/Firefox), Postman o curl.

```console
    curl -X GET http://localhost:8069/api/top_movies
    ```

- Al acceder deberiamos obtener el listado en formato json del top 10 de películas.
