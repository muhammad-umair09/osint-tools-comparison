import io
import pandas as pd

def generate_csv_report(df):
    """Generates a downloadable CSV bytes stream."""
    return df.to_csv(index=False).encode('utf-8')

def generate_excel_report(df):
    """Generates a downloadable Excel bytes stream with formatting sheets."""
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='OSINT Tool Metrics Summary')
    return output.getvalue()