from supabase import create_client

SUPABASE_URL = "https://qadfjxzauvrjrfqahbbm.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InFhZGZqeHphdXZyanJmcWFoYmJtIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTcxOTE0MDU0NiwiZXhwIjoyMDM0NzE2NTQ2fQ.kbDbfeuQp7LvVRJsaQ4K7MoE-qkxd0p4n3HA3GH-Db8"
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)


def get_user_data(user_id):
    response = supabase.table("users").select("*").eq("id", user_id).execute()
    return response.data

def save_dilemma(data):
    response = supabase.table("ethical_dilemmas").insert(data).execute()
    return response.data

# Additional database functions as needed
