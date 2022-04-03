a = "Hello|World!| game"
text= "Date|Amnt|Desc;\
Apr2022|10.20|Walmart;\
Apr2022|10.20|Costco;\
Apr2022|10.20|Walmart;\
Apr2022|10.20|Nofrill"

b = text.split(";")
print(b)
#Print only items that have Walmart in above
for item in b:
	if "Walmart" in item :
	    print(item)

