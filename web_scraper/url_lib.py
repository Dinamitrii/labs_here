import urllib.request

# URL of the web page to fetch
url = 'https://127.0.0.1/'

try:
    response = urllib.request.urlopen(url)
    data = response.read()

    # Decode the data (if it's in bytes) to a string
    html_content = data.decode('utf-8')

    # Print the HTML content of the web page
    print(html_content)

except Exception as e:
    print("Error fetching URL:", e)
