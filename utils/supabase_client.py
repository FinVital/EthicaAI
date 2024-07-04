from supabase import create_client, Client

url: str = "https://xksqzhnwlhtikmglxojk.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inhrc3F6aG53bGh0aWttZ2x4b2prIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjAwMDM2NDMsImV4cCI6MjAzNTU3OTY0M30.71210B6-yDeAWy08DZ8zTmO6ssfWWTYEyW6SCxVKdUE"
supabase: Client = create_client(url, key)
