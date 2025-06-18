# app.py
from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Loading the crypto database from a JSON file
with open('crypto_db.json') as f:
    crypto_db = json.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_query = request.form.get('query')
    result = handle_query(user_query)
    return jsonify(result)

def handle_query(user_query):
    """Process a user query and return a single appropriate response."""
    user_query = user_query.lower()

    for coin, data in crypto_db.items():
        coin_lower = coin.lower()

        # 1. Price Trend
        if f"{coin_lower} price trend" in user_query or f"trend of {coin_lower}" in user_query:
            return {"message": f"The price trend of {coin} is {data['price_trend']}."}

        # 2. Sustainability Score
        if f"{coin_lower} sustainability" in user_query or f"{coin_lower} sustainable" in user_query:
            score = data['sustainability_score'] * 10
            return {"message": f"The sustainability score of {coin} is {score}/10."}

        # 3. Market Cap
        if f"{coin_lower} market cap" in user_query or f"{coin_lower} capitalization" in user_query:
            return {"message": f"The market capitalization of {coin} is {data['market_cap']}."}

        # 4. Energy Use
        if f"{coin_lower} energy use" in user_query or f"{coin_lower} power" in user_query:
            return {"message": f"{coin} uses {data['energy_use']} energy."}

        # 5. Risk Level
        if f"{coin_lower} risk" in user_query or f"{coin_lower} safe" in user_query:
            return {"message": f"The risk level of {coin} is {data['risk_level']}."}

    # 6. Recommend sustainable coin
    if "most sustainable" in user_query or "eco friendly" in user_query:
        best = max(crypto_db.items(), key=lambda x: x[1]["sustainability_score"])
        return {
            "message": f"{best[0]} is the most sustainable coin with a score of {best[1]['sustainability_score']*10}/10.",
            "coinData": {
                "name": best[0],
                "price_trend": best[1]["price_trend"],
                "sustainability_score": best[1]["sustainability_score"] * 10,
                "market_cap": best[1]["market_cap"],
                "energy_use": best[1]["energy_use"],
                "recommended": True
            }
        }

    # 7. List trending coins
    if "trending" in user_query or "rising coins" in user_query:
        trending = [coin for coin, data in crypto_db.items() if data['price_trend'] == 'rising']
        return {"message": "Trending coins: " + ", ".join(trending)}

    # 8. Recommend low-risk coin
    if "low risk" in user_query or "safe investment" in user_query:
        safe_coins = [coin for coin, data in crypto_db.items() if data["risk_level"] == "low"]
        if safe_coins:
            return {"message": f"Low-risk coins include: {', '.join(safe_coins)}"}
        else:
            return {"message": "Currently, no coins are rated as low-risk."}

    # 9. Most efficient energy use
    if "least energy" in user_query or "energy efficient" in user_query:
        best = min(crypto_db.items(), key=lambda x: x[1]['energy_use'])
        return {"message": f"{best[0]} is the most energy-efficient coin with {best[1]['energy_use']} energy use."}

    # 10. General help
    if "help" in user_query or "what can you do" in user_query:
        return {
            "message": "I can help you with:\n"
                       "- Coin price trends\n"
                       "- Sustainability ratings\n"
                       "- Market caps\n"
                       "- Energy consumption\n"
                       "- Risk levels\n"
                       "- Recommending the best coins based on your priorities"
        }

    # Fallback
    return {
        "message": "I'm not sure how to help with that. Try asking about a coin's trend, risk level, sustainability, or market cap."
    }

@app.route('/api/crypto-data')
def get_crypto_data():
    """API to return all crypto data."""
    return jsonify(crypto_db)

@app.route('/api/recommendation')
def get_recommendation():
    """API to return a recommended coin based on criteria."""
    criteria = request.args.get('criteria', 'sustainability')

    if criteria == 'sustainability':
        coin = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])

    elif criteria == 'growth':
        rising_coins = [c for c in crypto_db if crypto_db[c]["price_trend"] == "rising"]
        if rising_coins:
            coin = max(rising_coins, key=lambda x: crypto_db[x]["sustainability_score"])
        else:
            coin = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])

    else:
        coin = min(crypto_db, key=lambda x: 9 if crypto_db[x]["risk_level"] == "high" else 3)

    return jsonify({"coin": coin, "data": crypto_db[coin], "recommended": True})

if __name__ == '__main__':
    app.run(debug=True)
