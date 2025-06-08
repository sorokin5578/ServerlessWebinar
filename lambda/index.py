import json
import uuid
import boto3
import os
from datetime import datetime, timezone

# Initialize DynamoDB resource
dynamodb = boto3.resource('dynamodb')
table_name = os.environ.get('TABLE_NAME', 'Notes')
table = dynamodb.Table(table_name)

def handler(event, context):
    http_method = event.get('httpMethod')
    resource_path = event.get('resource')  # e.g., /notes or /notes/{id}

    # Create a new note
    if http_method == 'POST' and resource_path == '/notes':
        body = json.loads(event.get('body', '{}'))
        note_id = str(uuid.uuid4())
        item = {
            'id': note_id,
            'text': body.get('text', ''),
            'createdAt': datetime.now(timezone.utc).isoformat()
        }
        table.put_item(Item=item)
        return {
            'statusCode': 201,
            'body': json.dumps({'message': 'Note created', 'id': note_id})
        }

    # Get all notes
    elif http_method == 'GET' and resource_path == '/notes':
        response = table.scan()
        return {
            'statusCode': 200,
            'body': json.dumps(response.get('Items', []))
        }

    # Delete a specific note using path parameter: /notes/{id}
    elif http_method == 'DELETE' and resource_path == '/notes/{id}':
        path_params = event.get('pathParameters') or {}
        note_id = path_params.get('id')

        if not note_id:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'Note ID is required in the path'})
            }

        table.delete_item(Key={'id': note_id})
        return {
            'statusCode': 200,
            'body': json.dumps({'message': f'Note {note_id} deleted'})
        }

    # Unsupported HTTP method or path
    return {
        'statusCode': 400,
        'body': json.dumps({'error': 'Unsupported method or path'})
    }