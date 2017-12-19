from datetime import datetime
from datetime import timedelta
import subprocess
date_init = datetime.strptime('2017-10-05','%Y-%m-%d')
while date_init<=datetime(2017,12,18,0,0,0):
     subprocess.check_call(['bq', 'query', '--use_legacy_sql=false', '--allow_large_results' ,'--replace','--noflatten_results', '--destination_table', 'Energy_Consumption.REFCONS_TEST$'+''.join(str(date_init).split( )[0].split('-')), "select * from `gbl-im-ve-energyefficiency.Energy_Consumption.REFCONS` where date(date_update) ='"+str(date_init).split()[0]+"'" ])
     date_init = date_init + timedelta(days = 1)
