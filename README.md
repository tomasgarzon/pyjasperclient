Introduction
============

A simple python module to run and get generated reports deployed on a JasperServer. Module works by consuming the SOAP web service provided by the JasperServer. It is ideal for python projects that uses JasperServer for reporting and needs a way to access/publish these reports to their users easily. However, this project is not a management interface for JasperServer, you should use its web interface and/or iReport for that.

Requirements
------------

* re # included in standard distribution
* email # included in standard distribution
* xml # included in standard distribution

* suds-py3

NOTE: module has been tested on python v3.5 only.

Usage
=====

For the impatient
-----------------

```python
from pyjasperclient import JasperClient

url = 'http://localhost:8080/jasperserver/services/repository?wsdl'
jc = JasperClient()
js.login(url, 'jlogin', 'jpass')
report = js.run('/Reports/reporting_to_the_explanatory_note/Report30', 'XLS', {'Year': u'2011'}, {'onePagePerSheet': 'true'})
report_file = file('report.xls','wb')
f.write(report[1]['data'])
f.close()
```

JasperClient object
-------------------
Create your Jasper object with JasperServer wsdl url and JasperServer credentials.

    j = JasperClient( 'http://localhost:8080/jasperserver/services/repository?wsdl', 'joeuser', 'joeuser')

There are only three methods that can be used.

    JasperClient.list(dir="")

Returns a list of strings that are report URIs of the JasperServer. Optional dir param may be used to define the directory to look for. It should start with / and end with directory name. (No / at the end)

    JasperClient.get(uri)

Returns a dict with report (uri) parametrs:
report:
* name
* id (uriString)
* label
* description
* controls [list]:
    * id (inputControl uri)
    * name
    * type
    * label
    * description
* parameters [list]:
    * name
    * class
    * default (default value)

<!-- endlist -->
    Jasper.run(uri, output="PDF", params={}, args={})

This will run the report for the URI given in uri and generate a dict containing 'content-type' and 'data'. 'content-type' can be used to send as an HTTP response header. params is a simple dict to pass directly to the running report. Uri should be report URI on JasperServer. Output may be PDF, JRPRINT, HTML, XLS, XML, CSV and RTF; default PDF

Check the source for more info
