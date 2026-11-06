# Manifiesto de datos

| Campo | Valor |
|---|---|
| Nombre del archivo en `data/raw/` | DadosV3.csv |
| Fuente (institución) | Pendiente de confirmar |
| URL exacta de descarga | Pendiente de confirmar |
| Fecha de descarga | Pendiente de confirmar |
| Licencia o condiciones de uso | Pendiente de confirmar |
| ¿Se permite redistribuir? | Pendiente de confirmar |
| Filas × columnas (raw) | 14942 × 47 |
| MD5 del archivo raw | 7651033e85d057d52b27b1cfa4a67755 |
| MD5 del archivo processed | 7f668c20ebe1f8c985985f86c7546db8 |

## Diccionario de las variables usadas

| Variable | Tipo | Descripción | Unidad / categorías |
|---|---|---|---|
| Dropout | Objetivo | Variable que se busca predecir | 0 y 1 |

## Transformaciones de raw a processed

1. Se quitaron espacios en los nombres de columnas.
2. Se eliminaron filas duplicadas.
3. No se identificaron códigos especiales de valores faltantes.
4. Se eliminaron las filas sin valor en la variable objetivo (Dropout).
5. No se agregaron transformaciones propias del grupo.
