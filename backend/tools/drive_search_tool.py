from google.oauth2 import service_account
from googleapiclient.discovery import build

from langchain.tools import tool


SCOPES = ["https://www.googleapis.com/auth/drive"]

import os

import json
import os

service_account_info = json.loads(
    os.getenv("SERVICE_ACCOUNT_JSON")
)

credentials = service_account.Credentials.from_service_account_info(
    service_account_info,
    scopes=SCOPES
)

service = build("drive", "v3", credentials=credentials)


@tool
def search_drive(query: str) -> str:
    """
    Search Google Drive files using Google Drive API q parameter syntax.

    You must generate valid Google Drive API queries.

    Examples:

    Search by partial name:
    - name contains 'report'

    Search PDFs:
    - mimeType='application/pdf'

    Search images:
    - mimeType contains 'image/'

    Search text content inside files:
    - fullText contains 'invoice'

    Search by modified date:
    - modifiedTime > '2025-05-01T00:00:00'

    Combined query:
    - name contains 'financial'
    and mimeType='application/pdf'

    Combined content search:
    - fullText contains 'salary'
    and mimeType='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'

    IMPORTANT:
    Always generate VALID Google Drive API q syntax only.
    """

    try:

        results = service.files().list(
            q=query,
            pageSize=10,
            fields="files(id, name, mimeType, webViewLink)"
        ).execute()

        files = results.get("files", [])

        if not files:
            return "No files found."

        output = []

        for file in files:
            output.append(
                f"""
            📄 File: {file['name']}
            📁 Type: {file['mimeType']}
            🔗 Link: {file['webViewLink']}
            """
            )

        return "Matching files:\n" + "\n".join(output)

    except Exception as e:
        return f"Error while searching Google Drive: {str(e)}"