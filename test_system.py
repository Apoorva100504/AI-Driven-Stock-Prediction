import requests
import time

def test_system():
    print("🧪 Testing stock prediction system...")
    
    # Wait a moment for server to start
    time.sleep(2)
    
    try:
        # Test the API
        response = requests.get('http://localhost:5000/api/analyze/GOLD', timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            print("✅ SYSTEM WORKING PERFECTLY!")
            print(f"📊 Symbol: {data['symbol']}")
            print(f"💰 Price: ${data['price']}")
            print(f"📈 Change: {data['price_change']}%")
            print(f"🎯 Recommendation: {data['recommendation']}")
            print(f"📊 RSI: {data['rsi']}")
            return True
        else:
            print(f"❌ API Error: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ System test failed: {e}")
        return False

if __name__ == '__main__':
    test_system()
