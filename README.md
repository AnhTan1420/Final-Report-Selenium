# Final-Report-Selenium
## OS: Mac/Linux

### Website : https://nhanvan.vn/

### Test Cases Manual : https://docs.google.com/spreadsheets/d/15JI9ma6HdpQmdbwhCUzVP3ujO8iiQbgd/edit?usp=sharing&ouid=100499490863982465973&rtpof=true&sd=true

### Project Report : https://docs.google.com/document/d/1LmMcX2ZmzTCnPe7JpjZZK8qasg_z_EOn/edit?usp=sharing&ouid=117418363728260771379&rtpof=true&sd=true



## Demo

<p align="center">
  <img width="700" align="center" src="https://github.com/AnhTan1420/Final-Report-Selenium/blob/main/Demo_Doan.gif" alt="demo"/>
</p>

## How to install 
### Install Project 

```
 git clone https://github.com/AnhTan1420/Final-Report-Selenium.git
```

### Activate .venv

```
 source .venv/bin/activate
```

### Install requirements.txt

```
 pip3 install -r requirements.txt 
```

## How to run
### Edit Data Excel
![image](https://user-images.githubusercontent.com/58280404/233262851-0948f480-c6d9-467e-b0b3-ff3b7e2b057e.png)

### Run Each Case
```
 pytest -sv src/tests/test_register.py
```

### Run Entire Case
```
 pytest -sv src/tests/test_*.py
```
