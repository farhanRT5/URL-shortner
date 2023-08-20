import pyshorteners

url = input("Enter the URL :\n")

print("URL after shortening :", pyshorteners.Shortener().tinyurl.short(url))