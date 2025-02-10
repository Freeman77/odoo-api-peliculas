# Módulo de Gestión de Películas en Odoo

## Descripción

Módulos de Gestión de Películas en Odoo (16.0)

- movie_management: Permite gestionar películas, incluyendo su nombre y ranking.

- movie_sync: Obtiene información de películas desde el servicio externo [Random Data API - Películas](https://random-data-api.com/api/v3/projects/a2bebcc5-69e3-4b4e-b8c0-4a2f4306f0da), cada 1 minuto (requiere API key).

- movie_api: Expone un endpoint REST (/api/top-movies) que entrega un Top 10 de películas, basado en el módulo [Base Rest](https://github.com/OCA/rest-framework/tree/16.0/base_rest) de la OCA.

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

- Una vez iniciado, Odoo estará disponible en la URL: http://localhost:8069
- Para el primer inicio, se debe crear una nueva base de datos.
- Luego iniciamos sesión como admin.
- En el menú 'Aplicaciones', buscar e instalar los módulos 'movie_management', 'movie_sync' y 'movie_api'.
- Ingresar en modo desarrollador a Ajustes > Técnico > Parámetros del sistema, buscar la llave 'movie_sync.api_key' e ingresar su key.
- Ingresar en modo desarrollador a Ajustes > Técnico > Acciones planificadas y activar la acción 'Sincronizar películas desde Random Data API'.
- Una vez configurado, el endpoint GET http://localhost:8069/api/top_movies comenzará a responder con el top 10 de películas.

## Cómo ejecutar Pruebas

...
