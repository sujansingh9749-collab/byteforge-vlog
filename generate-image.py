import requests
import sys
import base64
from pathlib import Path

def generate_image(prompt, output_path):
    # ZSky AI public endpoint
    url = "https://zsky.ai/api/public/generate"
    
    # আপনার আর্টিকেলের টাইটেল অনুযায়ী প্রম্পট তৈরি
    payload = {
        "prompt": prompt,
        "aspect_ratio": "16:9",  # ব্লগ কাভারের জন্য ভালো
        "style": "photographic"   # style: photographic, cinematic, artistic
    }
    
    try:
        response = requests.post(url, json=payload, timeout=60)
        response.raise_for_status()
        
        data = response.json()
        image_b64 = data.get("image_base64")
        
        if image_b64:
            # Base64 ডিকোড করে ইমেজ সেভ করুন
            image_data = base64.b64decode(image_b64)
            with open(output_path, 'wb') as f:
                f.write(image_data)
            print(f"✅ Image saved: {output_path}")
            return True
        else:
            print(f"❌ No image in response for prompt: {prompt}")
            return False
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python generate-image.py 'prompt' output.jpg")
        sys.exit(1)
    
    prompt = sys.argv[1]
    output_path = sys.argv[2]
    generate_image(prompt, output_path)
