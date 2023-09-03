import pyshorteners

def shorten_url(long_url):
    s = pyshorteners.Shortener()

    shortened_url = s.tinyurl.short(long_url)  

    return shortened_url

def main():
    print("Welcome to the URL Shortener!")

    while True:
        long_url = input("Enter the URL you want to shorten (or 'quit' to exit): ")

        if long_url.lower() == 'quit':
            break

        shortened_url = shorten_url(long_url)

        print(f"Shortened URL: {shortened_url}\n")

    print("Thank you for using the URL Shortener!")

if __name__ == "__main__":
    main()