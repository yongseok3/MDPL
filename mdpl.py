from astroquery.cosmosim import CosmoSim
import pandas as pd

class MDPL():
    CS = CosmoSim()

def test1():
    CS = CosmoSim()
    CS.login(username="kerex", password="sodwjd0279")
    ##CS.explore_db(db='MDPL2', table='FOF')
    sql_query = "SELECT 0.26*(0.5+FLOOR(LOG10(mass)/0.25)) AS log_mass, COUNT(*) AS num FROM MDR1.FOF WHERE snapnum=85 GROUP BY FLOOR(LOG10(mass)/0.25) ORDER BY log_mas"
    a=CS.run_sql_query(query_string=sql_query)
    CS.check_job_status(a)
    db = CS.download(a, filename="test.csv", format="csv")
    import numpy as np
    db = np.array(db)
    print(db)
    CS.check_all_jobs()
    #CS.delete_all_jobs()
    CS.logout()

def redshift():
    CS = CosmoSim()
    CS.login(username="kerex", password="sodwjd0279")
    ##CS.explore_db(db='MDPL2', table='FOF')
    sql_query = "SELECT DISTINCT * FROM MDR2.Redshifts ORDER BY snapnum DESC"
    a=CS.run_sql_query(query_string=sql_query)
    print(CS.check_job_status(a))

    db = CS.download(a, filename="test.csv", format="csv")
    import numpy as np
    db = np.array(db)
    print(db)
    CS.check_all_jobs()
    CS.logout()

    
if __name__ == "__main__":
    redshift()
