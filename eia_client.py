import requests
from decorators import log_step

class EIAClient:
    @log_step
    def fetch(self, states):
        all_data = []
        url = (
            "https://api.eia.gov/v2/electricity/state-electricity-profiles/"
            "capability/data/"
        )

        for state in states:
            params = {
                "api_key": "TdZEOO34JNlLtLmePpdjGECwba3Aj3ceGFGwD7SU",
                "frequency": "annual",
                "start": "2021",
                "end": "2023",
                "facets[stateId][]": state,
                "data[0]": "capability",
                "sort[0][column]": "period",
                "sort[0][direction]": "desc",
                "offset": 0,
                "length": 5000,
            }

            response = requests.get(url, params=params)
            print(f"Status for state {state}: {response.status_code}")

            if response.status_code == 200:
                data = response.json()
                all_data.append((state, data))
            else:
                print(f"Failed to fetch data for state {state}: {response.text}")

        return all_data