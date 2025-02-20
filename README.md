🍜 Food Chatbot
A chatbot that integrates the Line ChatBot API and web crawling to help users find Taiwanese food.

✨ Features
✔️ Search for food recommendations via Line chatbot
✔️ Scrape real-time food information (ratings, prices, menus, etc.)
✔️ Automatically respond to user input and suggest suitable restaurants or street food
✔️ Deploy on Heroku for continuous operation

🚀 Project Structure
1️⃣ API Integration
Uses Line Messaging API to receive and respond to user messages
Parses user input to determine search queries
2️⃣ Web Crawling
Scrapes real-time food data from various online sources
Extracts restaurant ratings, menus, and user reviews
3️⃣ Deployment & Hosting
Hosted on Heroku for seamless and continuous operation
Uses a database (e.g., PostgreSQL) to store frequently searched results
📌 How to Use
1️⃣ Add the official Line chatbot account
2️⃣ Send a message with the food or restaurant you’re looking for
3️⃣ Receive instant recommendations with relevant details

🛠️ Tech Stack
Python (Flask, Requests, BeautifulSoup)
Line Messaging API
Web Scraping (BeautifulSoup, Selenium)
Heroku (Deployment & Hosting)
