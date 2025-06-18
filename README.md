
# 💬 CryptoSage – Smart Cryptocurrency Advisor Chatbot

CryptoSage is a simple rule-based chatbot that helps users explore and understand key insights about popular cryptocurrencies, including trends, sustainability, energy usage, market capitalization, and risk levels. Built with Python and JavaScript, this chatbot interacts with a lightweight backend to provide responses based on a structured dataset.

---

## 🚀 Features

- 📈 Get the **price trend** of top cryptocurrencies.
- 🌱 Check the **sustainability score** of eco-friendly coins.
- ⚡ Learn about **energy consumption** of different crypto assets.
- 💼 Explore each coin’s **market capitalization**.
- ⚠️ Assess **risk levels** to inform better decisions.
- 🤖 Simple question-based interaction using natural keywords.
- 🎴 Recommended coins displayed with visual cards in the frontend.

---

## 🧠 Sample Questions Supported

Here are some example queries the chatbot understands:

1. What is Bitcoin price trend?
2. Tell me the sustainability score of Cardano.
3. How much energy does Ethereum use?
4. What's the market cap of Ripple?
5. What's Solana's risk level?
6. Recommend a sustainable cryptocurrency.
7. Which cryptos are trending?
8. Is there a low-risk cryptocurrency?
9. Which crypto has high energy usage?
10. What coin has the highest sustainability?

---

## 🛠️ Tech Stack

- **Frontend**: HTML, CSS, JavaScript (vanilla)
- **Backend**: Python (Flask or any minimal backend server)
- **Data**: Static `crypto_db` dictionary (can be extended to use a database or API)
- **Visualization**: Chart.js (for trends and sustainability charts)

---

## 📂 Project Structure

```
/CryptoSage/
├── static/
│   └── css
|         └──styles.css   # Style sheet
|   └── js
|        └── app.js       # Frontend interaction logic
├── templates/
│   └── index.html        # UI layout
├── app.py                # Backend server (Flask recommended)
├── crypto_db.json        # Crypto dataset (or embedded in app)
├── README.md             # Project documentation
```

---

## 🧪 How to Run

1. **Install dependencies** (for Flask backend):

   ```bash
   pip install flask
   ```

2. **Run the backend**:

   ```bash
   python app.py
   ```

3. **Open your browser** and navigate to:

   ```
   http://localhost:5000
   ```

4. **Ask your questions!** Start chatting with CryptoSage.

---

## 📊 Dataset

Sample crypto data (can be found in `crypto_data.py` or directly in your backend):

```python
crypto_db = {
  "bitcoin": { "price_trend": "rising", "sustainability_score": 0.7, "market_cap": "1.3T", "energy_use": "high", "risk_level": "medium" },
  "ethereum": { "price_trend": "rising", "sustainability_score": 0.6, "market_cap": "400B", "energy_use": "medium", "risk_level": "medium" },
  "cardano": { "price_trend": "stable", "sustainability_score": 0.9, "market_cap": "15B", "energy_use": "low", "risk_level": "low" },
  "solana": { "price_trend": "rising", "sustainability_score": 0.8, "market_cap": "60B", "energy_use": "low", "risk_level": "medium" },
  "ripple": { "price_trend": "stable", "sustainability_score": 0.5, "market_cap": "25B", "energy_use": "high", "risk_level": "high" }
}
```

---

## 📌 Notes

- This is a **rule-based bot**, not an AI/NLP model.
- You can expand it to support more dynamic queries, integrate Dialogflow, or connect to live APIs for real-time data.
- Sustainability scores are scaled from 0.0–1.0 and multiplied by 10 for display.

---

## 👨‍💻 Author

Built by Charles Mori– feel free to reach out or contribute!

---

## 📃 License

MIT License – feel free to use and modify.
