
#### 1) Atributos:
#- `marca` (String): marca de la radio.
#- `frecuenciaActual` (float): frecuencia actual en MHz (por ejemplo, 101.5).
#- `volumen` (int): nivel de volumen entre 0 y 100.
#- `encendida` (boolean): indica si la radio está encendida.
#- `modoFM` (boolean): indica si está en modo FM (True) o AM (False).
#- `frecuenciaAnterior` (float): guarda la última frecuencia antes del cambio.

#### 2) Métodos de consulta:
#- Obtener el valor de cada atributo mediante métodos `get`.

#### 3) Métodos de modificación:
#- Permitir cambiar la marca, el modo (FM/AM), y la frecuencia actual mediante métodos `set`.

#### 4) Métodos funcionales:
#- `subirVolumen()`: incrementa el volumen en 1 unidad (máximo 100).
#- `bajarVolumen()`: disminuye el volumen en 1 unidad (mínimo 0).
#- `cambiarFrecuencia(nuevaFrecuencia)`: cambia la frecuencia y guarda la anterior.
#- `frecuenciaAnterior()`: vuelve a la frecuencia anterior.
#- `silenciar()`: pone el volumen en 0.
#- `encender()`: enciende la radio.
#- `apagar()`: apaga la radio.

#### 5) Diagrama UML:
#- Representar los atributos y métodos en un diagrama UML de clase.

#### 6) Desafío adicional:
#- Proponer una mejora que permita guardar un conjunto de frecuencias favoritas (por ejemplo, en una lista) y crear métodos para:
#  - Agregar una frecuencia a favoritos.
#  - Mostrar todas las frecuencias favoritas.
#  - Sintonizar directamente una frecuencia favorita.
