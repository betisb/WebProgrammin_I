import requests
from bs4 import BeautifulSoup

def test_assignment_0_hello(student_id,url):
    response = requests.get(url+"/index")
    assert response.status_code == 200
    assert "h1" in response.text.lower()
    #assert student_id in response.text
    print("Pass")

def test_assignment_0_login(student_id,url):
    response = requests.get(url+"/login")
    assert response.status_code == 200
    assert "<form" in response.text
    assert "submit" in response.text.lower()
    assert "username" in response.text.lower()
    assert "password" in response.text.lower()
    html = BeautifulSoup(response.text,'html.parser')
    print(html.prettify())
    form_tag = html.find_all("form")
    assert (len(form_tag)>0)
    input_tag = html.find_all("input")
    assert (len(input_tag)>2)
    print(html.find_all('form'))
    print("pass")

if __name__ == "__main__":
    name='bbaheri'
    url="http://bbaheri.pythonanywhere.com"
    url= "localhost:5000"
    for test in [
        test_assignment_0_hello,
        test_assignment_0_login
        ]:
        test(name,url)