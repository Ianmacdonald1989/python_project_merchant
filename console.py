from models.spending import Spending
from models.merchant import Merchant

import repositories.spending_repository as spending_repository 
import repositories.merchant_repository as merchant_repository 


merchant1 = Merchant("Pizza Planet")
merchant_repository.save(merchant1)

merchant_repository.select_all()
