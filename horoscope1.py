#application to check daily horoscope
print('WELCOME.....')
next= True #to use for while loop
#begin of while
while next==True:
#content
  print('Get to know your todays Horoscope...')
  print('''
    1) Aries
    2) Tauras
    3) Gemini
    4) Cancer
    5) Leo
    6) Virgo
    7) Libra
    8) Scorpio
    9) Sagitarius
    10) Capricorn
    11) Aquarius
    12) Pisces
  ''')
    #taking input from user
  n=int(input("Pick your zodiac sign number..."))
  #begin of first if-elif-else
  if n==1:
    print('''
      ARIES:
      Feeling useful will suddenly be extremely important to you. 
      Right now you're feeling that it doesn't really matter whether you get what you want today when you see so many others who don't have anything at all. 
      If you can be of service to someone today, you will make yourself feel valuable, like you're able to do just about anything. 
      You are a positive force in people's lives, even the people who don't know you very well yet.
    ''')
  elif n==2:
    print('''
    TAURAS:
    Your feelings are just under the surface today, which you could choose to see as a good thing or a bad thing. 
    If you're looking for the courage to say something tough to someone who needs to hear it, your trigger temper could help you say it once and for all. 
    But if you're going to be around sensitive folks you need to impress today, said temper could lead to problems.
    A sudden emotional reaction won't go over well, so watch your tongue and be ready to hold it.
    ''')
  elif n==3:
    print('''
    GEMINI:
    One of those charming (if a bit eccentric) characters currently in your life is getting a bit too nosy right now. 
    Your business is yours. If you want to spare yourself some future exasperation, tell this busybody to mind their own business. 
    Be polite, but prepare to repeat yourself because they aren't likely to get the hint right off the bat.
    Your life is going to be much more fascinating to other people than it is to you right now, believe it or not.
    ''')
  elif n==4:
    print('''
    CANCER:
    Don't flinch if someone delivers you some disappointing news today.
    Deep down, you probably knew it was coming.And if you weren't prepared enough to handle this news with ease, don't worry about how things will turn out. 
    Instead, focus on the smaller issues that you can do something about. There are actions you can take to ease the sting of this news.
    Don't let yourself get drawn into the drama. Pick yourself up, dust yourself off, and carry on.
    ''')
  elif n==5:
    print('''
    LEO:
    Much to your surprise, your finances seem to be slowly falling into place. 
    This is good news, but it doesn't mean you should go back to your old ways of shopping and (not) tracking your costs. 
    Now that you have everything under control, don't give up! You're used to living life with a tighter belt, and there is still a lot you can learn about how to trim the fat. 
    Keep going and you'll be very proud of what you can save in just a few months.
    ''')
  elif n==6:
    print('''
    VIRGO:
    A group effort is the best effort today. If you want results, you need to get the help of the people who can make it happen. 
    Align yourself with the people who know what they're doing even if they aren't your favorite people on earth. 
    This isn't about making friends; it's about making progress on one of your life goals.
    These others will be able to provide all the details that make a big impression in the end. Trust their judgment.
    ''')
  elif n==7:
    print('''
    LIBRA:
    A recent spat might have left a bad taste in your mouth, but as far as everyone else is concerned, your name has no black mark on it.
     There have been no grudges held, so you need to do yourself a favor and forget about the unpleasantness that occurred. 
    Focus on the future and put your best foot forward. 
    They've already forgotten all about it, so how about you doing the same thing? Guilt won't get you where you need to go.
    ''')
  elif n==8:
    print('''
    SCORPIO:
    Today should be a good day, especially if you plan to follow up on someone's progress. 
    They're much further along than you expected, and it will warm your heart to see how they're thriving. 
    However, details regarding a project might escape you right now if you aren't paying careful attention. 
    You should ask someone else to double-check your work.
    It will give them the opportunity to feel useful, and it will help you know what to look out for next time.
    ''')
  elif n==9:
    print('''
    SAGITARIUS:
    What you've been waiting for is about to come your way, but the catch is you shouldn't let others see just how deliriously happy you are about it! 
    Play it coy and play it cool. Make sure you don't rush ahead of everyone else to snatch this opportunity from their hands! 
    Being too eager will put you at a disadvantage.
    Follow the lead of other people, and you will find yourself in a very advantageous position. Your patience will pay off big time.
    ''')
  elif n==10:
    print('''
    CAPRICORN:
    You need to step up to bat today, because your friends or co-workers are in desperate need of a leader like you! 
    Right now your brain is sharp, your convivial energy is strong, and you have a fantastic ability to find out what the real facts are that underlie any current intrigue. 
    He said/she said conflicts won't last long when you're team captain. 
    People need you! Volunteer to take over. Everyone, including you, will be glad you did.
    ''')
  elif n==11:
    print('''
    AQUARIUS:
    One of your partners—either in romance, life, or work—may have a different agenda than you do right now.
     This is totally fine and won't cause any conflict, but it is something you should be aware of. 
    A joint decision needs to be made soon, and they're leaning in the direction opposite yours. 
    They won't understand your point of view unless you explain it to them, so speak up in a calm way. Luckily, you're good at communicating what you need.
    ''')
  elif n==12:
    print('''
    PISCES:
    Being more analytical about your emotions might sound counterintuitive, but it's the perfect approach right now, especially since your brain is humming along much more efficiently than your slightly confused heart.
    Examine any problems you're dealing with now. Think about them objectively. Put yourself in the position of a judge overseeing the details of a case.
    Once you remove your own bias from the situation, you will quickly see an easy answer
    ''')
  else:
    print("Check the number you entered. Enter within the specified range (1-12)")
#end of if-elif-else

#begin of second if-else loop
  next = True if input("Do you want to check again? Enter 'Y' as yes or 'N' as no ")=="Y" else False 
  print('Thanks for using our service. Bye!') 
#end of if-else

#end of while