from pathlib import Path


ROOT_DIR = Path.cwd()
''' / '''

ENV_FILE = ROOT_DIR / '.env'
''' /.env '''

STORAGE_DIR = ROOT_DIR / 'storage/'
''' /storage/ '''

DATABASE_FILE = STORAGE_DIR / 'database.sqlite3'
''' /storage/database.sqlite3 '''

CONVERSATIONS_DIR = STORAGE_DIR / 'conversations/'
''' /storage/conversations/ '''
