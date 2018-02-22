# A Diep.io self playing bot developed by Shravan Bhat

#REQUIREMENTS
Please use something like pip and install the following dependencies-
* pyautogui
* numpy
* PIL
* OpenCv2

Also a size formatter such Sizer(Windows) can be used to help change sizes and debug any code

#CODE
This bot works by initially classifying the quadrant where the food is located and moviing mouse and the player to it. 

##Instructions-

**INITIALLY PLEASE SET THE MODE TO AUTO_FIRE BY PRESSING E IN THE BROWSER**

###TEST MODES-
* For test mode, set the variable TEST_MODE = True, this makes an opencv window open on the right to view what the bot is seeing. Also note that firefox **MUST** be sized to 776 x 721 size for optimum results

* For non test modes,set TEST_MODE= False and make the browser to full screen mode

###DETECTING TEAM
* This bot currently functions best in Sandbox mode, 2 Player and FFA modes very well.
* It does have functionality to detect enemy team color but if it dosen't please set the enemy=red_team or enemy=blue_team before the *getBox()* function

###WORKING
After this configuration, this is how bot works-
1) Detects all squares, polygons and triangles.
2) Finds the closest food source and starts moving slowly towards it.
3) At the same time,it points the mouse to the food source and launches bullets through auto_fire.
4) While moving if it comes too close to food source, it stops and waits till source is eaten to prevent health loss through collision impacts.
5) If no food is found, it moves towards the quadrant where the food was last found. If no food is found even after 5 seconds, it chooses a random quadrant and moves to it.
6) If any enemy is found, it starts shooting towards where enemy is last seen and starts running away immediately towards the opposite direction.
7) It detects borders by calculating pixel density of the border and moves away if pixel density of border increases beyond a certain value. Sometimes the bot may get stuck in a corner being unable to move requiring manual intervention.

#UPGRADING
Currently the player needs to manually upgrade to sniper or twin etc once level is reached since automatic functions are not finished yet.
>It currently works best in any sniper or twin with high fire rates and distance or high precision.

#TODO
[] Make bot detect enemy players properly by their scope rifles.
[] Auto upgrading
[] Food priority