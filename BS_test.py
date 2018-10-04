from bs4 import BeautifulSoup

with open("bbaheri.pythonanywhere.com") as fp:
    soup = BeautifulSoup(fp)

soup = BeautifulSoup("<html>data</html>")