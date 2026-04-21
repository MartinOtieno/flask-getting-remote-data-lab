from get_requester import GetRequester

url = "https://jsonplaceholder.typicode.com/users"

requester = GetRequester(url)

print(requester.get_response_body())
print(requester.load_json())