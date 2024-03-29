import requests

class Http_calls:
    def check_status(link:str):
        """
        Function to check link status

        Args:
        link: Link as string

        Returns:
        status_code: Link status code 
        """
        status = requests.get(link).status_code
        return status

    def fetch_data(link:str):
        """
        Function to fetch data

        Args:
        link: Link as string

        Returns:
        fetched link data.
        """
        return requests.get(link).content

def http_handler(link:str):
    print(f"Link status: {Http_calls.check_status(link)}")
    print(f"Data:\n {Http_calls.fetch_data(link)}")

if __name__ == "__main__":
    http_handler("https://example.com")