Tanium Sensor Analysis Tool Readme
===========================

---------------------------
<a name='toc'>Table of contents:</a>

  * [Tanium Sensor Analysis Tool Help](#user-content-tanium-sensor-analysis-tool-help)

---------------------------

# Tanium Sensor Analysis Tool Help

  * Asks a question for every sensor and saves the results as CSV reports

```bash
Tanium_Sensor_Analysis_Tool.py -h
```

```
usage: Tanium_Sensor_Analysis_Tool.py [-h] [-u USERNAME] [-p PASSWORD]
                                      [--host HOST] [--port PORT]
                                      [-l LOGLEVEL] [--debugformat]
                                      [--platform PLATFORMS]
                                      [--category CATEGORIES]
                                      [--output_dir REPORT_DIR]
                                      [--sleep SLEEP]
                                      [--pct PCT_COMPLETE_THRESHOLD]
                                      [--timeout TIMEOUT]
                                      [-f QUESTION_FILTERS]
                                      [-o QUESTION_OPTIONS] [--sensors-help]
                                      [--filters-help] [--options-help]

Asks a question for every sensor and saves the results as CSV reports

optional arguments:
  -h, --help            show this help message and exit

Tanium Authentication:
  -u USERNAME, --username USERNAME
                        Name of user (default: None)
  -p PASSWORD, --password PASSWORD
                        Password of user (default: None)
  --host HOST           Hostname/ip of SOAP Server (default: None)
  --port PORT           Port to use when connecting to SOAP Server (default:
                        444)

Handler Options:
  -l LOGLEVEL, --loglevel LOGLEVEL
                        Logging level to use, increase for more verbosity
                        (default: 1)
  --debugformat         Log with debug level to console and files (default:
                        False)

TSAT Options:
  --platform PLATFORMS  Only ask questions for sensors on a given platform
                        (default: [])
  --category CATEGORIES
                        Only ask questions for sensors in a given category
                        (default: [])
  --output_dir REPORT_DIR
                        Directory to save output to (default: /Users/jolsen/gh
                        /pytan/BUILD/TSAT_OUTPUT/2015_08_07-15_34_35-EDT)
  --sleep SLEEP         Number of seconds to wait between asking questions
                        (default: 1)
  --pct PCT_COMPLETE_THRESHOLD
                        Percent to consider questions complete (default: 99.0)
  --timeout TIMEOUT     How many seconds to wait before a question times out
                        (default: 300)
  -f QUESTION_FILTERS, --filter QUESTION_FILTERS
                        Whole question filter; pass --filters-help to get a
                        full description (default: [])
  -o QUESTION_OPTIONS, --option QUESTION_OPTIONS
                        Whole question option; pass --options-help to get a
                        full description (default: [])
  --sensors-help        Get the full help for sensor strings (default: False)
  --filters-help        Get the full help for filters strings (default: False)
  --options-help        Get the full help for options strings (default: False)
```

  * Validation Test: exitcode
    * Valid: **True**
    * Messages: Exit Code is 0



[TOC](#user-content-toc)


###### generated by: `build_bin_doc v1.4.5`, date: Fri Aug  7 15:34:35 2015 EDT, Contact info: **Jim Olsen <jim.olsen@tanium.com>**