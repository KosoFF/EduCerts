from pytz import utc
import requests
import json
import codecs
import dateutil.parser
from configuration import config as cf
from database import loadSession
from database import models
import sys
from apscheduler.schedulers.background import BackgroundScheduler, BlockingScheduler
from apscheduler.jobstores.redis import RedisJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor

from datetime import datetime

jobstores = {
    'redis': RedisJobStore(host='tarpon.redistogo.com', password='4d34a8694cdf73faaf16b29b81f0da11',
                           port=11400, db=0),

}
startblock=1
endblock=10000000

executors = {
    'default': ThreadPoolExecutor(1)

}
job_defaults = {
    'coalesce': False,
    'max_instances': 10
}
scheduler = BlockingScheduler(jobstores=jobstores, executors=executors, job_defaults=job_defaults, timezone=utc)

@scheduler.scheduled_job('interval', seconds=5)
def timed_job():
    payload = {
        'module': 'account',
        'action': 'txlist',
        'address': cf.ACCOUNT_ADDRESS,
        'startblock':startblock,
        'sort': 'asc',
        'apikey': cf.ETHERSCAN_API_KEY
    }
    r = requests.get('http://ropsten.etherscan.io/api', params=payload)
    lastBlock = 0
    json_data = json.loads(r.text)
    try:
        session = loadSession()
        for result in json_data['result']:
            block_number = result['blockNumber']
            timestamp = result['timeStamp']
            tx_hash = result['hash']
            block_hash = result['blockHash']
            org = result['from']
            cert = json.loads(codecs.decode(result['input'][2:], "hex").decode('utf-8'))
            certificate = models.Certificate(block_number=block_number, tx_timestamp=datetime.fromtimestamp(int(timestamp)),
                                             block_hash=block_hash, tx_hash=tx_hash, organisation_ethereum_wallet=org,
                                             personal_document_type_code=cert['personal_document_type_code'],
                                             personal_document_id=cert['personal_document_id'],
                                             certificate_type_code=cert['certificate_type_code'],
                                             certificate_id=cert['certificate_id'],
                                             course_name=cert['course_name'],
                                             certificate_date=dateutil.parser.parse(cert['certificate_date']),
                                             course_length=int(cert['course_length']),
                                             average_grade=int(cert['average_grade']),
                                             course_start_date=dateutil.parser.parse(cert['course_start_date']),
                                             course_end_date=dateutil.parser.parse(cert['course_end_date'])
                                             )
            if(session.query(models.Certificate.tx_hash).filter_by(tx_hash=certificate.tx_hash).scalar() is None):
                session.add(certificate)
                session.flush()
                session.commit()
    except AttributeError:
        print( "Unexpected error:", sys.exc_info()[0])
        return #expected behavior, some jsons will be rubbish

    except Exception:
        raise








# @scheduler.scheduled_job('interval', seconds=20)
# def timed_job():
#     print('I will sleep for 10 secs')
#     time.sleep(120)



scheduler.start()