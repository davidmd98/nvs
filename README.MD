# Goal: crear un projecte from scratch

## Step 1

- Crear workspace: doc <https://code.visualstudio.com/docs/editor/workspaces>
- Crear la carpeta del .devcontainer
- Crear el .devcontainer.json <https://code.visualstudio.com/docs/devcontainers/create-dev-container>
- Un Dockerfile que faci un Docker pull de Python 3.13
image-repo <https://hub.docker.com/_/python/>
image-names <https://medium.com/@faruk13/alpine-slim-bullseye-bookworm-noble-differences-in-docker-images-explained-d9aa6efa23ec>

Al Dockerfile hi ha d'haver:

- apt update
- apt install build-essentials

- Instal.lar poetry i pip
- Crear un fitxer poetry from scratch <https://python-poetry.org/>
- Mirar la documentació oficial de poetry
- Afegir-hi els els següents paquets: pandas, scikit-learn
- Afegir-hi els següents paquets de desenvolupament: ruff
- Implementar algun exemple de scikit de ML que faci servir moltes dates i que trigui molt a entrenar
- Dos scripts: fit i predict
- Tot dins d'un entry point: demo
- demo train
- demo predict

## Step 2

- Farem un segon Dockerfile dins fora de la carpeta de .devcontainer
- Semblant al del .devcontainer
- En aquest sí que farem un poetry install de tots els paquets
- Docker build d'aquest Dockerfile
    docker build -f Dockerfile DemoImage
- Crear container i executar exemple
    docker run -it --rm DemoImage bash
    docker run -it --rm DemoImage demo train
    docker run -it --rm DemoImage demo predict

## Step 3

- Executar el codi dins del container però estressant el container