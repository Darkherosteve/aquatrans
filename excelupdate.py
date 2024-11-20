import os
import openpyxl

def update_excel(file_path, sheet_name, updates):
    try:
        # Open the Excel file and select the sheet
        workbook = openpyxl.load_workbook(file_path)
        sheet = workbook[sheet_name]
        
        # Update specified cells with values
        for cell, value in updates.items():
            sheet[cell].value = value
        
        # Save the workbook after updates
        workbook.save(file_path)
        print("Success", "Details successfully saved to Excel.")
    except Exception as e:
        print("Error", f"Failed to update Excel: {str(e)}")