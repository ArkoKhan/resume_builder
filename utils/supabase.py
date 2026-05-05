import requests
import os
import uuid
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

def upload_file(file):
    filename = f"{uuid.uuid4()}_{file.name}"
    
    url = f"{SUPABASE_URL}/storage/v1/object/media/{filename}"
    
    headers = {
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {SUPABASE_KEY}",
        "Content-Type": file.content_type
    }
    
    response = requests.post(url, headers=headers, data=file.read())
    
    if response.status_code not in [200, 201]:
        raise Exception(f"Upload failed: {response.text}")
    
    public_url = f"{SUPABASE_URL}/storage/v1/object/public/media/{filename}"
    
    return public_url


def delete_file(file_url):
    SUPABASE_URL = os.getenv("SUPABASE_URL")
    SUPABASE_KEY = os.getenv("SUPABASE_KEY")
    
    # Extract filename from URL
    filename = file_url.split("/")[-1]
    
    url = f"{SUPABASE_URL}/storage/v1/object/media/{filename}"
    
    headers = {
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {SUPABASE_KEY}",
    }
    
    response = requests.delete(url, headers=headers)
    
    return response.status_code