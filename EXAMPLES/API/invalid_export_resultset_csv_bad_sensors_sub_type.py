
"""
Export a ResultSet from asking a question using a bad sensors
"""

import os
import sys
sys.dont_write_bytecode = True

# Determine our script name, script dir
my_file = os.path.abspath(sys.argv[0])
my_dir = os.path.dirname(my_file)

# determine the pytan lib dir and add it to the path
parent_dir = os.path.dirname(my_dir)
pytan_root_dir = os.path.dirname(parent_dir)
lib_dir = os.path.join(pytan_root_dir, 'lib')
path_adds = [lib_dir]

for aa in path_adds:
    if aa not in sys.path:
        sys.path.append(aa)


# connection info for Tanium Server
USERNAME = "Tanium User"
PASSWORD = "T@n!um"
HOST = "172.16.31.128"
PORT = "443"

# Logging conrols
LOGLEVEL = 2
DEBUGFORMAT = False

import tempfile

import pytan
handler = pytan.Handler(
    username=USERNAME,
    password=PASSWORD,
    host=HOST,
    port=PORT,
    loglevel=LOGLEVEL,
    debugformat=DEBUGFORMAT,
)

print handler

# setup the export_obj kwargs for later
export_kwargs = {}
export_kwargs["export_format"] = u'csv'
export_kwargs["sensors"] = [[]]
export_kwargs["header_add_sensor"] = True

# ask the question that will provide the resultset that we want to use
ask_kwargs = {
    'qtype': 'manual',
    'sensors': [
        "Computer Name"
    ],
}
response = handler.ask(**ask_kwargs)
export_kwargs['obj'] = response['question_results']

# export the object to a string
# this should throw an exception: pytan.exceptions.HandlerError
import traceback

try:
    handler.export_obj(**export_kwargs)
except Exception as e:
    traceback.print_exc(file=sys.stdout)



'''Output from running this:
Handler for Session to 172.16.31.128:443, Authenticated: True, Version: Not yet determined!
2015-08-07 19:57:02,479 DEBUG    pytan.handler.QuestionPoller: ID 1326: id resolved to 1326
2015-08-07 19:57:02,479 DEBUG    pytan.handler.QuestionPoller: ID 1326: expiration resolved to 2015-08-07T20:07:02
2015-08-07 19:57:02,479 DEBUG    pytan.handler.QuestionPoller: ID 1326: query_text resolved to Get Computer Name from all machines
2015-08-07 19:57:02,479 DEBUG    pytan.handler.QuestionPoller: ID 1326: id resolved to 1326
2015-08-07 19:57:02,479 DEBUG    pytan.handler.QuestionPoller: ID 1326: Object Info resolved to Question ID: 1326, Query: Get Computer Name from all machines
2015-08-07 19:57:02,482 DEBUG    pytan.handler.QuestionPoller: ID 1326: Progress: Tested: 0, Passed: 0, MR Tested: 0, MR Passed: 0, Est Total: 2, Row Count: 0
2015-08-07 19:57:02,483 DEBUG    pytan.handler.QuestionPoller: ID 1326: Timing: Started: 2015-08-07 19:57:02.479683, Expiration: 2015-08-07 20:07:02, Override Timeout: None, Elapsed Time: 0:00:00.003347, Left till expiry: 0:09:59.516972, Loop Count: 1
2015-08-07 19:57:02,483 INFO     pytan.handler.QuestionPoller: ID 1326: Progress Changed 0% (0 of 2)
2015-08-07 19:57:07,486 DEBUG    pytan.handler.QuestionPoller: ID 1326: Progress: Tested: 0, Passed: 0, MR Tested: 0, MR Passed: 0, Est Total: 2, Row Count: 0
2015-08-07 19:57:07,486 DEBUG    pytan.handler.QuestionPoller: ID 1326: Timing: Started: 2015-08-07 19:57:02.479683, Expiration: 2015-08-07 20:07:02, Override Timeout: None, Elapsed Time: 0:00:05.007137, Left till expiry: 0:09:54.513185, Loop Count: 2
2015-08-07 19:57:12,490 DEBUG    pytan.handler.QuestionPoller: ID 1326: Progress: Tested: 2, Passed: 2, MR Tested: 2, MR Passed: 2, Est Total: 2, Row Count: 2
2015-08-07 19:57:12,490 DEBUG    pytan.handler.QuestionPoller: ID 1326: Timing: Started: 2015-08-07 19:57:02.479683, Expiration: 2015-08-07 20:07:02, Override Timeout: None, Elapsed Time: 0:00:10.010671, Left till expiry: 0:09:49.509649, Loop Count: 3
2015-08-07 19:57:12,490 INFO     pytan.handler.QuestionPoller: ID 1326: Progress Changed 100% (2 of 2)
2015-08-07 19:57:12,490 INFO     pytan.handler.QuestionPoller: ID 1326: Reached Threshold of 99% (2 of 2)
Traceback (most recent call last):
  File "<string>", line 66, in <module>
  File "/Users/jolsen/gh/pytan/lib/pytan/utils.py", line 2699, in wrap
    ret = f(*args, **kwargs)
  File "/Users/jolsen/gh/pytan/lib/pytan/handler.py", line 1084, in export_obj
    pytan.utils.check_dictkey(**check_args)
  File "/Users/jolsen/gh/pytan/lib/pytan/utils.py", line 2692, in check_dictkey
    raise pytan.exceptions.HandlerError(err(key, valid_list_types, list_types))
HandlerError: 'sensors' must be a list of [<class 'taniumpy.object_types.sensor.Sensor'>], you supplied [<type 'list'>]!

'''