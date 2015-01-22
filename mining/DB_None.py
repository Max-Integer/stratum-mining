import time
import hashlib
import lib.settings as settings
import lib.logger
from twisted.enterprise import adbapi
from twisted.internet import defer

log = lib.logger.get_logger('DB_None')

class DB_None():
    def __init__(self):
        log.debug("Connecting to DB")
        self.connect()
        
    def connect(self):
	log.debug('Not Connecting to Empty DB')

    @defer.inlineCallbacks
    def fetchone_nb(self, query, args=None):
	defer.returnValue(True)

    def fetchall_nb(self, query, args=None):
	defer.returnValue(None)

    def execute_nb(self, query, args=None):
	defer.returnValue(None)

    def _executemany(self, txn, query, args):
        defer.returnValue(None)

    def executemany(self, query, args=None):
	defer.returnValue(None)

    def import_shares(self, data):
	defer.returnValue(None)

    @defer.inlineCallbacks
    def found_block(self, res, data):
        log.debug("############ found_block #############")
	defer.returnValue(None)

    def get_user_nb(self, id_or_username):
        log.debug("Finding nb user with id or username of %s", id_or_username)
        defer.returnValue(None)

    def get_user(self, id_or_username):
        log.debug("Finding user with id or username of %s", id_or_username)
	defer.returnValue(None)

    @defer.inlineCallbacks
    def get_uid(self, id_or_username):
	defer.returnValue(None)

    def insert_worker(self, account_id, username, password):
        log.debug("Adding new worker %s", username)
        return str(username)
        

    def delete_user(self, id_or_username):
        log.debug("Deleting user with id or username of %s", id_or_username)
	return

    def insert_user(self, username, password):
        log.debug("Adding new user %s", username)
        return str(username)

    def update_user(self, id_or_username, password):
        log.debug("Updating password for user %s", id_or_username);
	return None

    @defer.inlineCallbacks
    def check_password(self, username, password):
        log.debug("Checking username/password for %s", username)
        defer.returnValue(False)

    def update_worker_diff(self, username, diff):
        log.debug("Setting difficulty for %s to %s", username, diff)
	return None

    def clear_worker_diff(self):
        log.debug("Resetting difficulty for all workers")
	return None

    @defer.inlineCallbacks
    def get_workers_stats(self):
        result = yield self.fetchall_nb(
        defer.returnValue(None)

    def close(self):
	return None

    @defer.inlineCallbacks
    def check_tables(self):
        log.debug("Checking Database")
	return(True)
