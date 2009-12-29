d51.django.apps.tagging
=======================
Simple, small tagging application for Django

Why yet another tagging app?
----------------------------
Yes, yes, I know.  There a dozen tagging apps out there for Django, but a quick
look at any of them should send you running away screaming in terror.


Testing
-------

The tests in `d51.django.apps.tagging` are complete self-contained.  You can
run the tests from within any Django project by executing the standard test
command:

    python manage.py test tagging

You can also test directly within the repository using [virtualenv][] and
[pip][].  The rest of this section assumes you're interested in testing in
isolation, outside of a full project.

### Initializing the test environment
First, you must initialize a virtual environment:

    virtualenv .

Next, you need to install Django (if you don't have it installed already),
which is listed in the `requirements.txt` file.  You can install the necessary
version directly into the virtual environment using the `-E .` parameter:

    pip install -E . -r requirements.txt

### Initializing with Fabric
These steps can be run for you with [fabric][].  The `fabfile.py` included with
this repository has been tested with 1.0a and may not be backwards compatible.
To initialize using Fabric, you can run:

    fab init

### Activating test environment
You must activate the virtual environment if it contains your only copy of Django.
You can do this by running:

    source ./bin/activate

Your prompt should change to not that you are now running inside the virtual
environment.  Now you're ready to run the tests.

### Running the tests
There are two ways to run the tests.  The most straight forward with the output
you've come to expect from a Django test runner is the `run_tests.py` file.
Simply run:

    python run_tests.py

You can also run the tests using Fabric, though the output is much more
subdued.

    fab test

### Cleaning the test environment
A complete copy of Django, along with the tools necessary for virtualenv are
installed using this method.  Once you are finished testing, you can remove all
of the generated files with Fabric by running the following command:

    fab clean

*Warning*: You must re-run the initialization steps if in order to run the
tests again if you run the `clean` task.

[virtualenv]: http://virtualenv.openplans.org/
[pip]: http://pip.openplans.org/
[fabric]: http://docs.fabfile.org/

