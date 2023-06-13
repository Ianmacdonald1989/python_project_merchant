from models.spending import Spending
from models.merchant import Merchant

import repositories.spending_repository as spending_repository 
import repositories.merchant_repository as merchant_repository 

#SUPPLIER/STORE

merchant1 = Merchant("Pizza Planet")
merchant_repository.save(merchant1)

merchant2 = Merchant("Poultry Palace")
merchant_repository.save(merchant2)

merchant_repository.select_all()

#TRANSACTIONS 

spending1 = Spending("pizza")
spending_repository.save(spending1)

spending2 = Spending("Poultry Burger")
spending_repository.save(spending2)


spending_repository.select_all()
