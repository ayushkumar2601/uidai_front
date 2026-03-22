#!/usr/bin/env python3
"""
Test CORS configuration for the backend API
"""

import requests
import json

def test_cors():
    """Test CORS configuration"""
    base_url = "https://aadhaar-ml-api.onrender.com"
    
    print("Testing CORS configuration...")
    
    # Test 1: Health check
    print("\n1. Testing health endpoint...")
    try:
        response = requests.get(f"{base_url}/health", timeout=30)
        print(f"Status: {response.status_code}")
        print(f"Headers: {dict(response.headers)}")
        if response.status_code == 200:
            print("✅ Health check passed")
        else:
            print("❌ Health check failed")
    except Exception as e:
        print(f"❌ Health check error: {e}")
    
    # Test 2: States endpoint
    print("\n2. Testing states endpoint...")
    try:
        response = requests.get(f"{base_url}/api/states", timeout=30)
        print(f"Status: {response.status_code}")
        print(f"CORS Headers: {response.headers.get('Access-Control-Allow-Origin', 'Not found')}")
        if response.status_code == 200:
            data = response.json()
            print(f"✅ States endpoint passed - {len(data.get('states', []))} states found")
        else:
            print("❌ States endpoint failed")
    except Exception as e:
        print(f"❌ States endpoint error: {e}")
    
    # Test 3: OPTIONS preflight request
    print("\n3. Testing OPTIONS preflight...")
    try:
        headers = {
            'Origin': 'https://uidai-front-x2od-f8qni2gvf.vercel.app',
            'Access-Control-Request-Method': 'POST',
            'Access-Control-Request-Headers': 'Content-Type'
        }
        response = requests.options(f"{base_url}/api/predict", headers=headers, timeout=30)
        print(f"Status: {response.status_code}")
        print(f"CORS Headers: {dict(response.headers)}")
        if response.status_code in [200, 204]:
            print("✅ OPTIONS preflight passed")
        else:
            print("❌ OPTIONS preflight failed")
    except Exception as e:
        print(f"❌ OPTIONS preflight error: {e}")

if __name__ == "__main__":
    test_cors()