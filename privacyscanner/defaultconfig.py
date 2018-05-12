QUEUE_DB_DSN = 'dbname=privacyscore user=privacyscore password=privacyscore host=localhost'
MAX_EXECUTION_TIMES = {None: None}
SCAN_MODULE_OPTIONS = {}
SCAN_MODULES = [
    'privacyscanner.scanmodules.network',
    'privacyscanner.scanmodules.openwpm',
    'privacyscanner.scanmodules.serverleaks',
    'privacyscanner.scanmodules.testssl.https',
]
NUM_WORKERS = 2
MAX_EXECUTIONS = 100
