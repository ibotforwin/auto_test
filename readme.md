This is an early prototype of an automatic type tester for Python functions.

The intended purpose is for the tester to automatically find all the functions in a given Python file, check the hinted types and pass test values to ensure that the correct types are returned.

This current version is able to work within a single file but is not importable as a function into a foreign file. The auto_test.py file is the main application file and the tester.py is a test use-case which is still not functioning correctly at time.
