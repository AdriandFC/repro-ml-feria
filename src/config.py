"""Configuración del proyecto. Es el ÚNICO archivo que deben adaptar a su dataset."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Zonas del data lake
RAW = ROOT / "data" / "raw" / "DadosV3.csv"
PROCESSED = ROOT / "data" / "processed" / "dataset.csv"
RESULTS = ROOT / "results" / "results_summary.csv"

TARGET = "Dropout"
TAREA = "clasificacion"

COLS_NUM = []  # Pendiente: definir variables numéricas del modelo
COLS_CAT = []  # Pendiente: definir variables categóricas del modelo
CODIGOS_FALTANTES = []

MODELO = "CAMBIAR"  # Falta confirmar el algoritmo asignado

SEMILLA_PARTICION = 42
SEMILLAS = [0, 1, 2, 3, 42]
