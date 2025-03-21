import websocket
import ssl
import json

def open(ws):
    print("open")

    #Channel
    json_subscribe ="""
    {
    "event": "bts:subscribe",
    "data": {
        "channel": "live_trades_btcusd"
    }
}
"""
    #To send the channel to connection 
    ws.send(json_subscribe)

def error(ws, error):
    print(error) 

def message(ws, message):
    message = json.loads(message)
    price = message['data']['price_str']
    print(price)   

def close(ws):
    print("fechar")

if __name__== "__main__":
    ws = websocket.WebSocketApp("wss://ws.bitstamp.net.",
                                on_open=open,
                                on_close=close,
                                on_message=message,
                                on_error=error)
    
    print(ws) 
    ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})
