# 
# Example file for retrieving data from the internet
# LinkedIn Learning Python course by Joe Marini
#
import urllib.request
def main():
    webbrowser=urllib.request.urlopen("https://www.google.com")
    print("result code: ", webbrowser.getcode())
    data=webbrowser.read()
    print(data)

if __name__ == "__main__":
    main()
