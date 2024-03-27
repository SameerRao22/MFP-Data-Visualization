# MFP-Data-Visualization
A simple website that accepts CSV exports from the MyFitnessPal app and renders nice visual representations using Grafana. 

# Solution

Takes the file as an input. Parses the file to create a simpler csv. Grafana dashboard is generated using the parsed csv file.

# Technologies Used

Django \
Grafana \
Pandas 

# Installation
**1.** Download the projects's zip file onto your local system \
**2.** Navigate into the main project directory:
```
cd [project name]
```
**3.** Install the necessary requirements:
```
pip install -r requirements.txt
```
**4.** Make the necessary Django migrations using this command:
```
python manage.py migrate
```
**4.** Run the webserver in the project's main directory using this command:
```
python manage.py runserver
```
**5.** Open the following url in your browser of choice:
```
http://127.0.0.1:8000/
```
**6.** Use the test data contained in the ```test-data/``` directory as inputs to the web page to ensure the format of the file is correct 
