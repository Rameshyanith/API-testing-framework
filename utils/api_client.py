import requests # type: ignore

class APIClient:

    def __init__(self,base_url):
        self.base_url=base_url

    def get(self,endpoint,params=None):
        """
        Sends a GET request to the API.

        Args:
            endpoint (str): API endpoint (e.g., '/users').
            params (dict, optional): Query parameters for the request.

        Returns:
            dict: Parsed JSON response.
        """
        response = requests.get(f"{self.base_url}{endpoint}", params=params)
        response.raise_for_status()  # Raises HTTPError for bad responses (4xx, 5xx)
        return response.json()
    
    def post(self,endpoint,data=None):
        """
        Sends a POST request to the API.

        Args:
          endpoint (str): API endpoint.
          data (dict, optional): Payload for the POST request.

        Returns:
          dict: Parsed JSON response.
         """
        response = requests.post(f"{self.base_url}{endpoint}", json=data)
        response.raise_for_status()
        return response.json()
    
    def put(self,endpoint,data=None):
        """
        Sends a PUT request to the API to update data.

        Args:
            endpoint (str): API endpoint.
            data (dict, optional): Payload for the PUT request.

        Returns:
            dict: Parsed JSON response.
        """
        response=requests.put(f"{self.base_url}{endpoint}",data=None)
        response.raise_for_status()
        return response.json()
    
    def delete(self,endpoint):
        """
        Sends a DELETE request to the API.

        Args:
            endpoint (str): API endpoint.

        Returns:
            int: HTTP status code.
        """
        response = requests.delete(f"{self.base_url}{endpoint}")
        response.raise_for_status()
        return response.status_code()
    
     
    
        

