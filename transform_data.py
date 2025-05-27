import json
from datetime import datetime

def transform_data(element):
    try:
        record = json.loads(element.replace("'", "\""))

        record['row_key'] = record.get('row_key', '')
        record['name'] = record.get('name', '').title()
        record['email'] = record.get('email', '').lower()
        record['is_active'] = bool(record.get('is_active', False))

        record['loyalty_status'] = 'Platinum' if record.get('loyalty_points', 0) > 500 else 'Standard'

        inserted_at = record.get('inserted_at')
        updated_at = record.get('updated_at')

        try:
            record['inserted_at'] = datetime.strptime(inserted_at, '%Y-%m-%d %H:%M:%S').isoformat()
        except:
            record['inserted_at'] = datetime.utcnow().isoformat()

        try:
            record['updated_at'] = datetime.strptime(updated_at, '%Y-%m-%d %H:%M:%S').isoformat() if updated_at else '1970-01-01T00:00:00'
        except:
            record['updated_at'] = '1970-01-01T00:00:00'

        join_date = record.get('join_date')
        try:
            join_date_obj = datetime.strptime(join_date, '%Y-%m-%d')
            record['account_age_days'] = (datetime.utcnow() - join_date_obj).days
        except:
            record['account_age_days'] = 0

        record['age'] = record.get('age', 0)
        record['account_balance'] = record.get('account_balance', 0.0)
        record['loyalty_points'] = record.get('loyalty_points', 0)
        record['last_login'] = record.get('last_login', '1970-01-01T00:00:00')

        return json.dumps(record)
    except Exception as e:
        print("Transformation Error:", e)
        return None
