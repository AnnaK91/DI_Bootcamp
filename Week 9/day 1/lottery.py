# Lottery ticket cost 1 dollar and it can make you rich !

# Create a class called "LotteryTicket"
# it has only one attribute: "golden" (boolean)

# Use a class attribute to count how many tickets were bought
# Every fifth ticket is a golden ticket (just set "golden" to True)
# """
# Dunder methods:

class LotteryTicket:

    bought_tickets = 0
    golden_counter = 0

    def __init__(self):

        LotteryTicket.bought_tickets += 1
        LotteryTicket.golden_counter += 1

        self.golden = False
        self.ticket_number = LotteryTicket.bought_tickets

        if LotteryTicket.golden_counter == 5:
            self.golden = True
            LotteryTicket.golden_counter = 0

    def __str__(self): #Overriding Object.__str__
        return f"<Ticket No {self.ticket_number}>"

    def __repr__(self):
        if self.golden:
            return f"Golden Ticket No {self.ticket_number}>"
        return f"<Ticket No {self.ticket_number}>"

# class Object --> Mother class of every class in python
tickets = []
i = 0
while i < 50:
    ticket = LotteryTicket()
    tickets.append(ticket)
    i += 1

print(tickets[25])
print(tickets)