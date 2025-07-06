Tarea 3 - Intercepción, Inyección y Modificación de Tráfico FTP con Scapy

Taller de Redes y Servicios  
 
---

Este proyecto consiste en analizar el comportamiento de un servicio de red al interceptar, modificar e inyectar tráfico no esperado entre un cliente y un servidor FTP utilizando la herramienta Scapy dentro de un contenedor Docker.

Se realizaron inyecciones usando fuzzing, modificaciones a campos del protocolo FTP y análisis de las repercusiones generadas en el cliente o servidor.

---

## Estructura del Proyecto

.
├── client-ftp/ # Contenedor cliente FTP
│ └── Dockerfile
├── server-ftp/ # Contenedor servidor ProFTPD
│ ├── Dockerfile
│ ├── proftpd.conf
│ └── mensaje.txt
├── scapy/ # Contenedor con scripts Scapy
│ ├── Dockerfile
│ ├── cambio_user.py
│ ├── fuzzing.py
│ ├── modificaciones.py
│ ├── modificar_flags.py
│ └── ver_trafico.py
├── Taller_Redes_y_Servicios_Tarea3.pdf # Informe 
├── Taller_Redes_y_Servicios_Tarea2.pdf # Entrega anterior (base)


---

## Requisitos

- Docker instalado
- Linux (recomendado para captura de red sin restricciones)
- Acceso a red local para ejecución de múltiples contenedores

---

## Instrucciones para Reproducir

### 1. Crear contenedores Docker

```bash
docker build -t server-ftp ./server-ftp

docker build -t client-ftp ./client-ftp

docker build -t scapy-container ./scapy

## 2. Ejecutar contenedores

```bash
docker run -dit --name server --network red-tarea3 server-ftp

docker run -dit --name client --network red-tarea3 client-ftp

docker run -it --name scapy --network red-tarea3 --cap-add=NET_ADMIN scapy-container
 **El contenedor Scapy requiere la opción --cap-add=NET_ADMIN para modificar tráfico.**

## 3. Ejecucion de scripts en Scapy

| Script               | Descripción                                                |
| -------------------- | ---------------------------------------------------------- |
| `ver_trafico.py`     | Captura y muestra el tráfico FTP entre cliente y servidor. |
| `cambio_user.py`     | Modifica el comando USER para probar credenciales falsas.  |
| `fuzzing.py`         | Inyecta tráfico malformado usando técnicas de fuzzing.     |
| `modificaciones.py`  | Realiza múltiples pruebas de modificación de comandos.     |
| `modificar_flags.py` | Cambia flags TCP para observar efectos no estándar.        |

**Ejemplo: python3 cambio_user.py**