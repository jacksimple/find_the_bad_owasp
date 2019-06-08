from elasticsearch import Elasticsearch, helpers

class ElasticsearchWriter():
    def __init__(self, host='elasticsearch', base_index='accesslogs', initialize=True):
        # First create the db
        self.conn = Elasticsearch(host)
        self.base_index = base_index
        if initialize:
            self.delete_indexes()
            self.conn.indices.create(index=self.base_index)

    def delete_indexes(self):
        delete_index_wildcard = '{0}*'.format(self.base_index)
        self.conn.indices.delete(index=delete_index_wildcard, ignore=[400, 404])

    def insert_log(self, index, doc_id, doc, doc_type='accesslog'):
        self.conn.index(
            index=index,
            doc_type=doc_type,
            body=doc,
            id=doc_id
        )

    def bulk_insert(self, docs):
        helpers.bulk(self.conn, docs)
