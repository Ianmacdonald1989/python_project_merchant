from db.run_sql import run_sql

from models.spending import Spending 
from models.merchant import Merchant
import repositories.merchant_repository as merchant_repository 

#save
def save(spendings):
    sql = "INSERT INTO spendings (amount, tag, merchant_id) VALUES (%s, %s, %s) RETURNING *"
    values = [spendings.amount_spent, spendings.tag, spendings.merchant.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    spendings.id = id
    return spendings

#select
def select_all():
    spendings = []

    sql = "SELECT * FROM spendings"
    results = run_sql(sql)

    if results is not None: 
        merchant = merchant_repository.select(results['merchant_id'])
        spendings = Spending(results['amount_spent'], results['tag'], merchant, results['id'])
    return spendings 

#delete
def delete_all():
    sql ="DELETE FROM spendings"
    run_sql(sql)

#delete all 
def delete(id):
    sql ="DELETE FROM  spendings WHERE id = %s"
    values = [id]
    run_sql(sql, values)


#update 
def update(spending):
    sql = "UPDATE spendings SET (amount_spent. tag, merchant) = (%s, %s, %s) WHERE id = %s"
    values = [spending.amount_spent, spending.tag, spending.merchant, spending.id]
    run_sql(sql, values)

