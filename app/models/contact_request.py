class ContactRequest:
    name = ""
    email = ""
    category = ""
    priority = ""
    message = ""

    def __str__(self):
        return f"name:{self.name} email:{self.email} category:{self.category} priority:{self.priority}" \
               f"message:{self.message}"

    def Save(self):
        pass
