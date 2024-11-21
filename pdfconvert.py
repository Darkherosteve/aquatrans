import win32com.client as win32
import os
import pythoncom

def excel_to_pdf(excel_file_path, pdf_file_path):
    try:
        pythoncom.CoInitialize()  # Initialize COM
        
        if not os.path.exists(excel_file_path):
            print("Error:", f"Excel file not found: {excel_file_path}")
            return
        
        excel = win32.DispatchEx('Excel.Application')
        wb = excel.Workbooks.Open(excel_file_path)
        
        # Export workbook as PDF
        wb.ExportAsFixedFormat(0, pdf_file_path)
        print("Success:", f"PDF saved successfully as: {os.path.basename(pdf_file_path)}")
    
    except Exception as e:
        print("Error:", f"Failed to save PDF: {str(e)}")
    
    finally:
        try:
            wb.Close(False)
        except Exception as e:
            print(f"Error closing workbook: {e}")
        try:
            excel.Quit()
        except Exception as e:
            print(f"Error quitting Excel: {e}")
        pythoncom.CoUninitialize()  # Uninitialize COM