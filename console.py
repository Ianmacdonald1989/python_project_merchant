import pdb
from models.spending import Spending
from models.merchant import Merchant

import repositories.spending_repository as spending_repository 
import repositories.merchant_repository as merchant_repository 

spending_repository.delete_all()
merchant_repository.delete_all() 


#SUPPLIER/STORE

merchant1 = Merchant("Pizza Planet")
print(merchant1.id)
merchant_repository.save(merchant1)
print(merchant1.id)
merchant2 = Merchant("Poultry Palace")
merchant_repository.save(merchant2)

merchant_repository.select_all()

#TRANSACTIONS 

spending1 = Spending(15, "Italian", merchant1)
spending_repository.save(spending1)

spending2 = Spending(10, "nashville", merchant2)
spending_repository.save(spending2)




# pdb.set_trace()
