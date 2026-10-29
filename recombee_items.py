import pandas as pd
from recombee_api_client.api_client import RecombeeClient, Region
from recombee_api_client.api_requests import SetItemValues, Batch
from recombee_api_client.exceptions import APIException

# TODO 1: Configurare credentiale Recombee
DB_NAME = 'mockorg-dev'
PRIVATE_TOKEN = 'K8cabquIlOKPCwZii6xjpishNuiY8sPtk7O8xhqc1lhC8x5f2XQUFcrMJlJeNaqO'

client = RecombeeClient(DB_NAME, PRIVATE_TOKEN, region=Region.EU_WEST)

# TODO 2: Incarcarea dataset-ului
PATH_DATASET = 'imdb_top_1000.csv'

def send_items():
    """Functie care citeste dataset-ul si trimite item-urile in Recombee"""
    try:
        df = pd.read_csv(PATH_DATASET)
    except FileNotFoundError:
        print(f"Eroare: Fisierul '{PATH_DATASET}' nu a fost gasit!")
        return

    # Umplem valorile lipsa (NaN) pentru a evita erori
    df = df.fillna({
        'Genre': 'Unknown',
        'Released_Year': 0,
        'IMDB_Rating': 0.0,
        'Director': 'Unknown',
        'Overview': ''
    })

    print(f"Se trimit {len(df)} item-uri in Recombee...")
    
    requests = []
    
    for index, row in df.iterrows():
        # Curatam item_id si inlocuim slash-urile care strica URL-ul REST
        item_id = str(row['Series_Title']).replace('/', '_').replace('\\', '_').strip()
        
        # Validare si conversie an lansare
        try:
            released_year = int(row['Released_Year'])
        except (ValueError, TypeError):
            released_year = 0

        # Maparea proprietatilor cu cele definite la Lab 02
        properties = {
            "genre": str(row['Genre']),
            "released_year": released_year,
            "imdb_rating": float(row['IMDB_Rating']),
            "director": str(row['Director']),
            "overview": str(row['Overview'])
        }
        
        # Adaugam request-ul de setare a valorilor pentru item
        requests.append(SetItemValues(item_id, properties, cascade_create=True))
        
        # Trimitem in loturi (batch) de cate 100 pentru eficienta
        if len(requests) == 100:
            client.send(Batch(requests))
            requests = []
            print("S-a trimis un lot de 100 item-uri...")
            
    # Trimitem si restul ramanase
    if requests:
        client.send(Batch(requests))
        print("S-a trimis ultimul lot de item-uri.")
        
    print("Toate item-urile au fost trimise cu succes!")

if __name__ == "__main__":
    send_items()