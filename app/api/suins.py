from requests import request

def get_suins_username(domain):
    suins_url = "https://suins-be-prod.herokuapp.com/domain/search"
    domain_replaced = domain.replace(".sui", "")
    suins_payload = {
        "name": domain_replaced,
    }
    
    response = request("POST", suins_url, json=suins_payload)

    results = response.json()['results']

    if (len(results) > 0 and results[0] and results[0]['domain'] == 'sui' and results[0]['owner_address']):
        return results[0]['owner_address']

    if (len(results) > 1 and results[1] and results[1]['domain'] == 'sui' and results[1]['owner_address']):
        return results[1]['owner_address']

    return False