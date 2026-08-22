grand_total=0
my_list=[]
def list():
  my_cosmatic={"lakme":500,
             "maybelline":650,
             "nykaa":700,
             "m.a.c":1500,
             "huda beauty":1800,
             "colorbar":600,
             "sugar cosmatics":550,
             "plum":450,
             "mamaearth":400}
  def function():
   global grand_total
   try:
     units=int(input("Enter quantity:"))
     if units>0: 
       total=units*price
       grand_total=grand_total+total
       item.append(units)
       item.append(total)
     else:
       print("please enter a valid number")  
   except Exception as e:
        print("erorr:",e)
        function() 
  user=input("Enter The Stock Name:").lower()
  stock=user.lower()
  item=[]
  if stock in my_cosmatic.keys():
      price=my_cosmatic.get(stock)
      item.append(user)
      item.append(price)
      function()
      my_list.append(item)
      again=input("do you add another item (y/n)")
      if again in ["yes","y"]:
           list() 
      elif again in["n","no"]:  
        print("---------PORTFOLIO SUMMARY----------") 
        for each in my_list:
          
          print("BRAND:",each[0])
          print("PRICE:",each[1])
          print("QUANTITNY:",each[2])
          print("TOTAL:",each[3]) 
          print("                  ")
        print("-----------------------------------------------")
        print("grand total=",grand_total)
        print("===============================================")
         
  else:
      print("Sorry this brand is not avaliable in our list")
       
      again=input("do you add another item (y/n)").lower()
      if again in["n","no"]:
         print("---------PORTFOLIO SUMMARY----------")  
         for each in my_list:
             
           print("BRAND:",each[0])
           print("PRICE:",each[1])               
           print("QUANTITY:",each[2])
           print("TOTAL:",each[3]) 
           print("                  ")
           print("-----------------------------------------------")
           print("grand tootal  =          ",grand_total)
           print("===============================================")
list()            
         
with open("portfolio.txt","w") as file:
   file.write("----------portofolio summary-----------")    
   for each in my_list:
      file.write("\nBRAND :"+str(each[0]))     
      file.write("\nPRICE :"+str(each[1]))
      file.write("\nQUANTITY :"+str(each[2]))
      file.write("\nTOTAL :"+str(each[3]))
      file.write("\n                  ")    
      file.write("\n--------------------------------------") 
   file.write("\nGRAND TOTAL :"+str(grand_total))
   file.write("\n===========================================")
with open("portfolio.txt","r")as file:
    content=file.read()    
    print(content)