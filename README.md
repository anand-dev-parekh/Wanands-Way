# Wanands Way

This is a simple pygame mini game similiar to that of crossy road. Just not as visually appealing...


---
## Play Locally

1) Clone repo
```
git clone https://github.com/anand-dev-parekh/Wanands-Way.git
```
2) Install dependencies
```
cd Wanands-Way
pip3 install -r requirements.txt
```
3) Run the game and Enjoy! 
```
cd src
python3 main.py
```

---

## Updates
I created this game a while ago, so of course, there are many areas to improve in this game. I don't plan to work on this game anymore, however, if you would like, make a pull request and I'll update it! Anyways heres a list of things that should be done to this game.

1) Hash and Salt user passwords
2) Make a prettier design for the game
3) IF app gets bigger, create a simple api to update+read database

---

## Create Leaderboard
Before you configure the leaderboard please read these warnings.

#### Warnings
The game connects to a MongoDB Cluster. The original intent of the app was to make a little game my friends and I could play during school, so I made it serverless and placed the MongoDB authentication on the client side (bad practice). This means anyone who were to use your leaderboard would have full access to your MongoDB cluster making the game VERY insecure. So, unless you are also just making a little leaderboard for your friends, I would not recommend configuring the database/leaderboard.


Instructions for Configuring Leaderboard
1) Fork the repository 
