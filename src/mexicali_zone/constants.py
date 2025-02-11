BOUNDS_FILE = "bounds.fgb"
CSV_DENUE = 'temp_data/conjunto_de_datos/denue_inegi_{0}_.csv'
DENUE = 'https://www.inegi.org.mx/contenidos/masiva/denue/denue_{0}_csv.zip'
ESTABLISHMENTS_FILE = "establishments.fgb"
REGEX_PPL = r'([0-9]+) a ([0-9]+) personas'
SECTORS_MAP = [
    {"range": [(11, 11)], "sector": "primario"},
    {"range": [(21, 33)], "sector": "industria"},
    {"range": [(43, 46)], "sector": "comercio"},
    {"range": [(51, 56)], "sector": "oficina"},
    {"range": [(48, 49), (81, 81)], "sector": "servicios"},
    {"range": [(62, 62)], "sector": "salud"},
    {"range": [(61, 61)], "sector": "educacion"},
    {"range": [(72, 72)], "sector": "comercio"},
    {"range": [(73, 100)], "sector": "gubernamental"},
]