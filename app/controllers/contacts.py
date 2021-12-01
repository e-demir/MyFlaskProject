from ..models import ContactRequest

def GetContactList():
    return [
        ["Emrullah DEMİR", "Üretim", "Yüksek"],
        ["Ayça TUNCAY", "Satış", "Orta"],
        ["Zehra Sultan DEMİR", "İnsan Kaynakları", "Yüksek"],
        ["Ali Veli", "Nakliye", "Orta"]
    ]

def SaveContactRequest(name, email, category, priority, message):
    contact_request = ContactRequest()
    contact_request.name = name
    contact_request.email = email
    contact_request.category = category
    contact_request.priority = priority
    contact_request.message = message
    contact_request.Save()
    print(contact_request)