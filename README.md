# Pipeline de ML reproducible · NOMBRE DEL PROYECTO

Machine Learning I · Proyecto Integrador · Entregable individual
Alumno(a): NOMBRE · Grupo: N · Algoritmo asignado: MODELO

**Resumen:** QUÉ predice el modelo, con QUÉ dataset peruano (fuente) y cuántas filas.

## Cómo reproducir
Probado con **Python X.Y.Z** en SISTEMA OPERATIVO.

macOS / Linux:
```bash
git clone URL_DEL_REPOSITORIO repro && cd repro
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
PYTHONHASHSEED=0 python -m src.prepare_data
PYTHONHASHSEED=0 python -m src.train --seed 42
PYTHONHASHSEED=0 python -m src.run_seeds
```
Windows (PowerShell):
```powershell
git clone URL_DEL_REPOSITORIO repro; cd repro
python -m venv .venv; .venv\Scripts\Activate.ps1
pip install -r requirements.txt
$env:PYTHONHASHSEED=0
python -m src.prepare_data
python -m src.train --seed 42
python -m src.run_seeds
```

## Resultado esperado
Una corrida (`--seed 42`):
{"seed": 42, "modelo": "rf", "data_md5": "7f668c20ebe1f8c985985f86c7546db8", "accuracy_mean": 0.92379, "accuracy_sd": 0.00703, "f1_macro_mean": 0.87079, "f1_macro_sd": 0.01246, "recall_macro_mean": 0.84438, "recall_macro_sd": 0.01428}

Cinco semillas (results/results_summary.csv):
Cinco semillas (`results/results_summary.csv`):

| Semilla | Modelo | Accuracy media | Accuracy DE | F1 macro media | F1 macro DE | Recall macro media | Recall macro DE |
|---:|---|---:|---:|---:|---:|---:|---:|
| 0 | baseline | 0.80097 | 0.00016 | 0.44474 | 0.00005 | 0.50000 | 0.00000 |
| 1 | baseline | 0.80097 | 0.00016 | 0.44474 | 0.00005 | 0.50000 | 0.00000 |
| 2 | baseline | 0.80097 | 0.00016 | 0.44474 | 0.00005 | 0.50000 | 0.00000 |
| 3 | baseline | 0.80097 | 0.00016 | 0.44474 | 0.00005 | 0.50000 | 0.00000 |
| 42 | baseline | 0.80097 | 0.00016 | 0.44474 | 0.00005 | 0.50000 | 0.00000 |
| 0 | rf | 0.92496 | 0.00645 | 0.87351 | 0.01115 | 0.84860 | 0.01165 |
| 1 | rf | 0.92278 | 0.00484 | 0.86940 | 0.00817 | 0.84360 | 0.00758 |
| 2 | rf | 0.92496 | 0.00381 | 0.87302 | 0.00789 | 0.84717 | 0.01211 |
| 3 | rf | 0.92404 | 0.00677 | 0.87172 | 0.01207 | 0.84645 | 0.01324 |
| 42 | rf | 0.92379 | 0.00703 | 0.87079 | 0.01246 | 0.84438 | 0.01428 |

**Resultado reportado:** Accuracy de Random Forest = **0.9241 ± 0.0009** (media ± desviación estándar muestral entre 5 semillas). Baseline = 0.8010 ± 0.0000.

**Resultado reportado:** Accuracy = 0.92379 ± 0.00703, F1 macro = 0.87079 ± 0.01246 y Recall macro = 0.84438 ± 0.01428 (validación cruzada de 5 particiones, semilla 42).

![Corridas en MLflow](docs/mlflow.png)

## Estructura de datos (data lake)
| Zona | Carpeta | Contenido | Regla |
|---|---|---|---|
| raw (bronze) | `data/raw/` | Archivo original | Nunca se edita |
| processed (silver) | `data/processed/` | Datos limpios | Se regenera con `src.prepare_data` |
| results (gold) | `results/` | Métricas | Se regenera con `src.run_seeds` |

Ver `data/MANIFIESTO.md`.

## Qué lo hace reproducible
| Requisito | Cómo se cumple |
|---|---|
| ≥ 6 commits | |
| Sin fuga de datos | |
| Aleatoriedad fija | |
| 5 semillas en MLflow, media ± DE | |
| Mismos datos para todos | |
| Entorno exacto | |

## Prueba del extraño
Quién la hizo (nombre y grupo), enlace al Issue y resultado.

## Limitaciones

## Respuestas
1. …
2. …
3. …
4. …
5. …
6. …

## Declaración de uso de IA
Qué herramienta de IA se usó, para qué y qué revisó o ejecutó el autor. Si no se usó, indicarlo.
