from google.oauth2 import service_account
from googleapiclient.discovery import build

from langchain.tools import tool


SCOPES = ["https://www.googleapis.com/auth/drive"]

SERVICE_ACCOUNT_FILE = "credentials/service_account.json"

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE,
    scopes=SCOPES
)

service = build("drive", "v3", credentials=credentials)


@tool
def search_drive(query: str) -> str:
    """
    Search Google Drive files using Google Drive API query syntax.

    Examples:
    - name contains 'Report'
    - mimeType='application/pdf'
    - name contains 'employee' and mimeType='application/pdf'

    Use:
    - name contains 'keyword'
    - mimeType='application/pdf' for PDFs
    - mimeType contains 'image/' for images

    IMPORTANT:
    Use valid Google Drive API q parameter syntax only.
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
            File: {file['name']}
            Type: {file['mimeType']}
            Link: {file['webViewLink']}
            """
            )

        return "Matching files:\n" + "\n".join(output)

    except Exception as e:
        return f"Error while searching Google Drive: {str(e)}"