from ticket_manager import TicketManager

manager = TicketManager()

manager.add_user("Mehmet", "mehmet@it-destek.com", "IT Staff")
manager.add_user("Elif", "elif@it-destek.com", "IT Staff")
manager.add_user("Ahmet", "ahmet@it-destek.com", "IT Staff")
manager.add_user("Gökçe", "gokce@it-destek.com", "IT Staff")
manager.add_user("Hasan Abi", "hasan@it-destek.com", "Senior IT Staff")

print("Ekip başarıyla veritabanına eklendi!")