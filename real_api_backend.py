from flask import Flask, jsonify, send_file
import random
from datetime import datetime

app = Flask(__name__)

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

# Test data with guaranteed extreme conditions
STOCK_DATA = {
    'BTC': 65200, 'ETH': 3500, 'AAPL': 178, 'TSLA': 252, 
    'MSFT': 331, 'GOOGL': 139, 'GOLD': 1985, 'SILVER': 23
}

@app.route('/')
def home():
    return send_file('index.html')

@app.route('/api/analyze/<symbol>')
def analyze_stock(symbol):
    try:
        symbol = symbol.upper().strip()
        print(f"🔍 Analyzing: {symbol}")
        
        # GUARANTEE extreme conditions for testing
        test_cases = [
            # Case 1: STRONG BUY (Low RSI)
            {'rsi': 25, 'change': -2, 'rec': 'STRONG BUY', 'score': 0.85, 'conf': 'Very High'},
            # Case 2: BUY (Medium RSI + Positive change)
            {'rsi': 35, 'change': 5, 'rec': 'BUY', 'score': 0.75, 'conf': 'High'},
            # Case 3: STRONG SELL (High RSI)
            {'rsi': 75, 'change': 1, 'rec': 'STRONG SELL', 'score': 0.15, 'conf': 'Very High'},
            # Case 4: SELL (Medium-High RSI + Negative change)
            {'rsi': 65, 'change': -4, 'rec': 'SELL', 'score': 0.25, 'conf': 'High'},
            # Case 5: BUY (Positive momentum)
            {'rsi': 50, 'change': 6, 'rec': 'BUY', 'score': 0.65, 'conf': 'Medium'},
            # Case 6: SELL (Negative momentum)
            {'rsi': 50, 'change': -7, 'rec': 'SELL', 'score': 0.35, 'conf': 'Medium'},
            # Case 7: HOLD (Neutral)
            {'rsi': 45, 'change': 1, 'rec': 'HOLD', 'score': 0.5, 'conf': 'Medium'}
        ]
        
        # Pick a random test case for variety
        case = random.choice(test_cases)
        
        if symbol in STOCK_DATA:
            base_price = STOCK_DATA[symbol]
        else:
            base_price = random.uniform(50, 500)
        
        current_price = base_price * (1 + case['change']/100)
        
        result = {
            'symbol': symbol,
            'price': round(current_price, 2),
            'price_change': round(case['change'], 2),
            'rsi': round(case['rsi'], 1),
            'prediction_score': case['score'],
            'recommendation': case['rec'],
            'confidence': case['conf'],
            'data_source': 'Test Data',
            'timestamp': datetime.now().isoformat(),
            'reasoning': 'Test mode: Guaranteed recommendation variety'
        }
        
        print(f"✅ TEST MODE: {symbol} - {case['rec']} (RSI: {case['rsi']}, Change: {case['change']}%)")
        return jsonify(result)
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return jsonify({'error': 'Analysis failed. Please try again.'}), 500

@app.route('/api/test')
def test_api():
    return jsonify({'status': 'TEST MODE ACTIVE - Guaranteed BUY/SELL recommendations!'})

if __name__ == '__main__':
    print("🚀 STOCK PREDICTOR TEST MODE")
    print("🎯 GUARANTEED to show BUY/SELL/STRONG BUY/STRONG SELL recommendations!")
    app.run(debug=True, port=5000, host='0.0.0.0')
