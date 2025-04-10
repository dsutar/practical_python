import requests
from requests.adapters import HTTPAdapter, Retry

class WeatherAPIClient:
    def __init__(self, base_url, api_key, timeout=5, retries=3):
        self.base_url = base_url
        self.api_key = api_key
        self.timeout = timeout
        self.retries = retries
        
         # Set up session with retry logic
        self.session = requests.Session()
        retry_strategy = Retry(
            total=retries,
            backoff_factor=0.5,
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=["GET"]
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("http://", adapter)
        self.session.mount("https://", adapter)
        
        
    def get_current_weather(self, city):
        url = f"{self.base_url}/weather"
        
        params = {"q": city, "appid": self.api_key}
        
        try:
            response = self.session.get(url, params=params, timeout=self.timeout)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.Timeout  :
            print("Request timed out")
        except requests.exceptions.HTTPError as err:
            print(f"HTTP error: {err}")
        except requests.exceptions.RequestException as err:
            print(f"Error during request: {err}")
        return None    
    
    
if __name__ == "__main__":
    client = WeatherAPIClient(
        base_url="https://api.mockweather.com",
        api_key="demo123",
        timeout=3,
        retries=2
    )

    data = client.get_current_weather("San Francisco")
    print(data)    