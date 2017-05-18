from retrying import retry
import logging
import time

log = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

g_i = 0

@retry(wait_fixed=1000, stop_max_delay=10000)
def f1():
	try:
		global g_i
 		log.info("iteration %d, time: %d ", g_i, time.time())	
		g_i += 1
		assert g_i == 5 
	except:


	return g_i


f1()
