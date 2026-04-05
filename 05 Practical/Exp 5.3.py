#Shreyas Rajendra Shigwan, Roll no. 90, CSE(AIML)
# Exp 5.3: Logging for Debugging
import logging
logging.basicConfig(level=logging.INFO)

try: 
    x = int(input("Enter a number : "))
    y = int(input("Enter another number : "))
    logging.debug("Performing Division")
    print(x/y)
except Exception as e:
    logging.error("Error occured")