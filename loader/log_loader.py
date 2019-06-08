import json
import hashlib
import time
from data_managers.writers.elasticsearch_writer import ElasticsearchWriter


def get_log_id(log):
    # Generate a unique id for the provided log
    hasher = hashlib.blake2b(digest_size=20)
    hasher.update(log)
    return hasher.hexdigest()

def get_bulk_prepped_log(data_id, log, base_index='accesslogs', log_type='accesslog'):
        # Format the log to get it ready for bulk insert
        index_name = "{}".format(base_index)
        # Some cleaning
        log['_index'] = index_name
        log['_type'] = log_type
        log['_id'] = data_id
        return log

def parse_log(es_writer, file_path='data/access_exercise.json', initialize=True):
    # Loads the local log file, does geo enchancement and then puts it into ES
    print('Starting parse log process')
    print('Opening log file and reading')
    log_file = open(file_path).read()
    logs = json.loads(log_file)
    processed_logs = []
    print('Loading logs into ES')
    for log in logs:
        #print(log)
        processed_logs.append(
            get_bulk_prepped_log(
                get_log_id(json.dumps(log).encode('utf-8')),
                log
            )
        )
    es_writer.bulk_insert(processed_logs)
    print('Done')

if __name__ == "__main__":
    es_connected = False
    es_writer = None
    # Dirty hack to deal with this container not starting first 
    # And if the ES connection doesn't work
    while not es_connected:
        try:
            es_writer = ElasticsearchWriter(initialize=True)
            es_connected = True
        except Exception as ex:
            print('Failed to connect sleeping for 5 -> {0}'.format(ex))
            time.sleep(5)
            continue
    parse_log(es_writer)
