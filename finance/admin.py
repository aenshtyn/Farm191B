from django.contrib import admin
from .models import AccountYear,AccountType,Ledger,Transaction,TransactionDetails,JournalEntry
# Register your models here.

admin.site.register(AccountYear )   
admin.site.register(AccountType)  
admin.site.register(Ledger)  
admin.site.register(Transaction)  
admin.site.register(JournalEntry)
# admin.site.register()
# admin.site.register()
# admin.site.register()
# admin.site.register()