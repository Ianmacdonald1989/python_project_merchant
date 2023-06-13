from db.run_sql import run_sql

from models.spending import Spending 
from models.merchant import Merchant
import repositories.merchant_repository as merchant_repository 

#save
def save(spending):
    sql = "INSERT INTO spendings (amount, tag, merchant_id) VALUES (%s, %s, %s) RETURNING *"
    values = [spending.amount_spent, spending.tag, spending.merchant.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    spending.id = id
    return spending

#select
def select_all():
    spendings = []

    sql = "SELECT * FROM spendings"
    results = run_sql(sql)

    for row in results: 
        merchant = merchant_repository.select(row['merchant_id'])
        spending = Spending(row['amount'], row['tag'], merchant, row['id'])
        spendings.append(spending)
    return spendings 

def select(id):
    spending = None
    sql = "SELECT * FROM spendings WhERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        merchant = merchant_repository.select(result['merchant_id'])
        spending = Spending(result['amount'], ['tag'], merchant, result['id'])
    return spending
    

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

