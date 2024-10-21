"""
Trigger a DAG in a Cloud Composer 2 environment in response to an event,
using Cloud Function.
"""

import os
from typing import Any, Dict

import composer2_airflow_rest_api
from dateutil.parser import parse
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Email

# Constants
WEB_SERVER_URL = ""
"""The WEB_SERVER_URL is a constant that represents the URL of the Airflow web server 
in your Cloud Composer environment. It's used to interact with the 
Airflow API to trigger DAGs (Directed Acyclic Graphs) remotely."""

DAG_ID = 'hive_load_airflow_dag'

def trigger_dag_gcf(data: Dict[str, Any], context: Any = None) -> None:
    """
    Trigger a DAG and pass event data.

    Args:
      data: A dictionary containing the data for the event. Its format depends
      on the event.
      context: The context object for the event.
    """
    file_name = data['name']
    file_parts = file_name.split('/')[-1].split('.')
    
    if len(file_parts) != 2 or file_parts[1] != 'csv':
        send_error_email(f"Invalid file format: {file_name}")
        return

    date_str = file_parts[0].replace('logistics_', '')
    
    try:
        parse(date_str, yearfirst=True)
    except ValueError:
        send_error_email(f"Invalid date format in file name: {file_name}")
        return

    composer2_airflow_rest_api.trigger_dag(WEB_SERVER_URL, DAG_ID, data)

def send_error_email(error_message: str) -> None:
    """ Send an error email using SendGrid.
    Access the sendgrid API key stored in cloud run function's environment varibales """
    sg = SendGridAPIClient(os.environ['key-gcp-mail'])

    message = Mail(
        to_emails=["xxx@gmail.com"],
        from_email=Email('xxx@gmail.com', "Ray"),
        subject="Error in Cloud Function",
        html_content=f"<p>{error_message}</p>"
    )
    
    try:
        response = sg.send(message)
        print(f"Email sent successfully. Status code: {response.status_code}")
    except Exception as e:
        print(f'Failed to send email: {str(e)}')
