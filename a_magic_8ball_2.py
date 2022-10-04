#d_8ball.py
"""
title: Magic 8 Ball 2! 
author: Michelle Jiang
date-created: 2022-10-044
"""

import random 

### VARIABLES ### 
ANSWERS = (
"⭐Certainly.⭐", 
"✨It is decidedly so.✨", 
"⭐Without a doubt.⭐", 
"✨Absolutely✨", 
"⭐Definitely⭐",
"✨You can count on it✨", 
"⭐Yes⭐", 
"✨Most likely✨", 
"✨Outlook good.✨", 
"⭐Signs point to yes.⭐",
"✨Cannot be determined.✨", 
"⭐Your mom⭐",
"⭐Try again⭐", 
"✨Ask again later✨",
"⭐Now is not a good time⭐", 
"✨ Sorry, but no. ✨", 
"~*Clear your mind*~ and ask again",
"⭐The stars do not align⭐",
"✨My sources say no✨",
"~*It is not fated*~"
)

### Intro ### 
print("Shake the magic 8 ball! Seek to find ~*the answer in mind*~")

# Input # 
VALUE = input("Think your question, think it twice. Then ENTER in the 8 ball. (Just press ENTER to shake the ball)")

# Processing # 
if VALUE == "":
    ANSWER = ANSWERS[random.randint(0, 19)]

# Output #
    print(ANSWER)