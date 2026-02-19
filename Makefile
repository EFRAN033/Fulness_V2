# Makefile para un proyecto Vue.js

# Regla para construir la aplicación
build:
	npm run build

# Regla para desplegar la aplicación a S3
deploy: build
	aws s3 cp --recursive dist/ s3://fulness-prueba4

# Regla para limpiar el directorio de construcción
clean:
	rm -rf dist/