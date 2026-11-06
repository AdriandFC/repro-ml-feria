"""Configuración del proyecto. Es el ÚNICO archivo que deben adaptar a su dataset."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Zonas del data lake
RAW = ROOT / "data" / "raw" / "DadosV3.csv"
PROCESSED = ROOT / "data" / "processed" / "dataset.csv"
RESULTS = ROOT / "results" / "results_summary.csv"

TARGET = "Dropout"
TAREA = "clasificacion"

COLS_NUM = [
    "Age",
    "EnrollmentDuration",
    "DaysWithoutFrequency",
    "LifetimeValue",
    "AverageFrequency",
    "UseByTime",
    "AthleticsActivities",
    "WaterActivities",
    "FitnessActivities",
    "DanceActivities",
    "TeamActivities",
    "RacketActivities",
    "CombatActivities",
    "NatureActivities",
    "SpecialActivities",
    "OtherActivities",
    "NumberOfActivities",
    "NumberOfFrequencies",
    "AttendedClasses",
    "AttendedClassesAverage",
    "AllowedWeeklyVisitsBySLA",
    "AllowedNumberOfVisitsBySLA",
    "RealNumberOfVisits",
    "Ratio",
    "NumberOfRenewals",
    "HasReferences",
    "NumberOfReferences"
]
COLS_CAT = [
    "AgeClass",
    "Gender",
    "EnrollmentDurationClass2",
    "DaysWithoutFrequencyClass2",
    "AverageFrequencyClass2",
    "RatioClass2"
]
CODIGOS_FALTANTES = []

MODELO = "rf"

SEMILLA_PARTICION = 42
SEMILLAS = [0, 1, 2, 3, 42]
