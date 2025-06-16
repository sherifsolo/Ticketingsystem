import time
import math

#Ticket System	Log, assign, track, and close support issues with status tags


#implimet CRUD operations
    #Create a ticket
    #Read(get) a ticket
          #open if in progress/ waiting on user/ escalated
          #closed  if resolved
    #Update a ticket
       #@admin
          #prority
          #agent
          #category
       #@officer
          #ticket status ----- in progress/ waiting user / resolved / escalated
    #Delete a ticket

#impliment logging capabilities just incase
#tracking capabilities

#email / sms notification for any major update and to submitter if ticket resolved

class TICKET:
       Title = ""
       Description = ""
       Category = ""
       PriorityLevel = ""
       Uploads = "" #this should contain links to the resources but rendered dynamically on the UI
       Status = ""
       Agent = ""
       Id = 0
       def __init__(self, title: str, description: str, category: str, prioritylevel: str = "Low", uploads = None, status: str = "Open", agent: str = None):
              self.Title = title
              self.Description = description
              self.Category = category
              self.PriorityLevel = prioritylevel
              self.Uploads = uploads
              self.Status = status
              self.Agent = agent
              self.Id = self.setTicketId()
       def getTicketInfo(self):
              return [ self.Id, self.Title, self.Description, self.Category, self.PriorityLevel, self.Uploads, self.Status, self.Agent]
    
       def setTicketStatus(self, status: str):
              self.Status = status
       def setTicketPriorityLevel(self, level: str):
              self.PriorityLevel = level
       def setTicketAgent(self, agent: str):
              self.Agent = agent

#what if two tickets are submitted at the same time?
       def setTicketId(self) -> str:
              try:
                     import time
                     import math
              except ImportError as e:
                     print(f"failed to import the time module with error {e}\n please make sure its installed")
              except Exception as e:
                     print("An unexpected error occured...this tickets id has been set to 0, set it manually to avoid collision")
                     self.Id = 0
              currentTime = time.time()
              timeString = time.ctime()
              checkSum = 0
              for char in self.Title:
                     checkSum += ord(char) #gets the ascii value of ech digit and adds it to our checksum.
              #print(f"current time {currentTime} on {timeString}\n ")
              #print(f"Current time plus checksum = {currentTime + checkSum}")
              iD = currentTime + checkSum
              iD = math.ceil((iD % 365))
              #Tue Jun  3 08:38:01 2025
              #123456789012

              id = f"{timeString[0]}{timeString[4]}{timeString[9]}{str(iD)}"
              self.Id = id
              return self.Id
               

class TICKTINGSYSTEM():
      tickets = []

      def __init__(self):
         pass

      #CREATE
      def createTicket(self,title: str, description: str, category: str, priorityLevel: str, uploads, status: str = "Open", agent: str = None ) -> list:
         ticket = TICKET(title, description, category, priorityLevel, uploads, status, agent)
         self.tickets.append(ticket)
         print("Created new ticket")
         return ticket.getTicketInfo()
      

      # READ 
      #returns a list populated with the actual instances of the TICKET object in memory
      def getTickets(self) -> list:
         return self.tickets
      
      def getTicketsInfo(self) -> list:
         info = []
         for ticket in self.tickets:
            intel = ticket.getTicketInfo()
            info.append(intel)
         return info
      #returns a TICKET object gotten by id

      def getTicketById(self, id: str) -> TICKET:
         for ticket in self.tickets:
            if ticket.Id == id:
               return ticket
         return None
      
      # UPDATE
      # ticket status, uploads, agent, prioritylevel
      def updateTicketStatus(self, id: str, status: str):
         ticket = self.getTicketById(id)
         print(f"Changing ticket {ticket.Id} status from {ticket.Status} to {status}")
         ticket.setTicketStatus(status)
         print(f"ticket {ticket.Id} changed status to {status}  \n")
         return


      def updateTicketAgent(self, id: str, agent:str):
         ticket = self.getTicketById(id)
         print(f"Changing ticket {ticket.Id} agent from {ticket.Agent} to {agent}")
         ticket.setTicketAgent(agent)
         print(f"ticket {ticket.Id} changed agent to {agent} \n")
         return
      def updatePriorityLevel(self, id: str, level: str):
         ticket = self.getTicketById(id)
         print(f"Changing ticket {ticket.Id} priority level from {ticket.PriorityLevel} to {level}")
         ticket.setTicketPriorityLevel(level)
         print(f"ticket {ticket.Id} changed priority level to {level} \n")
         return
      # DELETE
      def deleteTicket(self, id: str):
         ticket = self.getTicketById(id)
         try:
            print(f"removing ticket with id {id}...this action can not be undone \n")
            self.tickets.remove(ticket)
         except ValueError:
            print(f"Could not delete ticket with id {id}")

         return

