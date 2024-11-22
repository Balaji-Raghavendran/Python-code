class CreateLibraryId:
    def __init__(self,customer_name,library_Id):
        self._customer_name = customer_name
        self._library_Id = library_Id

    def customer_Identification_Card(self):
        print("Customer's name is:",self._customer_name)
        print("Customer's Library Id:",self._library_Id)

class Booklending(CreateLibraryId):
    def __init__(self,customer_name,library_Id,):
        super().__init__(customer_name,library_Id)
        self._book_lending = ["1.Hacking: The Art of Exploitation by Jon Erickson",
                              "2.Metasploit: The Penetration Tester's Guide",
                              "3.The Web Application Hacker's Handbook",
                              "4.The 7 Habits of Highly Effective People",
                              "5.Deep Work: Rules for Focused Success in a Distracted World",
                              "6.How to Win Friends and Influence People",
                              "7.Whispers of the Eternal Flame",
                              "8.Echoes of the Forgotten Realm",
                              "9.Stormcallers of the Celestial Tide",
                              "10.Ashes of the Blood Moon",
                              "11.Turning Setbacks into Comebacks",
                              "12.My Brain is 90% Sarcasm",
                              "13.Aliens Ate My Homework (And Other Excuses)",
                              "14.The Subtle Art of Not Giving a Duck",
                              "15.When Life Gives You Lemons, Ask for Tequila"] #creating a book list
        
        self._lending_days = {1: 25, 2: 19, 3: 30, 4: 20, 5: 18, 6: 29, 7: 21, 8: 17, 9: 14, 10: 16, 11: 14, 12: 17,
                              13: 16, 14: 18, 15: 18} #creating a dictionary to select a particular book number and their due dates
        
        self._lent_book = None
        
    def lending_book(self,lend_book):
            if 1 < lend_book <= len(self._book_lending): #lend book value must be greater than 0 and lesser than equal to the length of self._book_lending
                 book_name = self._book_lending[lend_book-1]  #using index positioning selecting a particular book
                 lending_days = self._lending_days.get(lend_book,"Unknown") #self._lending_days and lend_book will fetch the values if the values are not found then unknown will be displayed
                 self._lent_book = (book_name,lending_days)
                 print("The book you lend",book_name,"and the lending days is",lending_days)
            else:
                 print("Invalid book number!")

    def Customer_bill(self):
         if self._lent_book: #if the values are in the self._lent_book
              print("========Customer's Bill=========")
              print("Customer's name:",self._customer_name)
              print("Customer's Library Id:",self._library_Id)
              print("The book Customer lent is:",self._lent_book[0])
              print("The due day for the book is:",self._lent_book[1])
              print("**********Thank You Visit Again**********")
         else:
              print("Invalid Book Registration or Renew Library Id")

customer = Booklending("John","BC123")
customer.lending_book(15)
customer.Customer_bill()

                 
        
        
 