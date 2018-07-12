__counter__

counter is a REST API based word count.

This app should work on OS X, Linux, and Windows. You should have the latest
version of either Python 2.7 or Python 3 installed.

#### Installation

Clone the repository or download the files ```counter.py```.

Install he dependency library - ```flask``` using pip

    $ pip install flask

#### Launch

Launch the application or deploy this in a web server to serve on default port or friendly URI.

```
$ python counter.py <urlMap.pkl>
```

This will start a webserver on port 5000.

##### Usage

To consume the REST endpoint, Simply hit the URL on the browser.

```
http://<hostname>:5000/api/<word>
```

Provided ```word``` in the endpoint is recorded and a numeric 3 digit number is returned with a value of how many times the ```word``` is provided in the URL.


