import os
from flask import Flask, render_template, request, send_file
# from excelupdate import update_excel
# from exceltopdf import excel_to_pdf

app = Flask(__name__)

# Home route to render the home page
@app.route("/")
def home():
    return render_template('home.html')

# Form submission route
@app.route('/submit', methods=['POST'])
def submit():
    # Get Form Data and convert to uppercase
    vehicle_no = request.form.get('vehicle_no').upper()
    date = request.form.get('date')
    consignment_no = request.form.get('consignment_no').upper()
    from_location = request.form.get('from_location').upper()
    to_location = request.form.get('to_location').upper()
    consignor = request.form.get('consignor').upper()
    consignee = request.form.get('consignee').upper()
    cargo_description = request.form.get('cargo_description').upper()
    quantity = request.form.get('quantity').upper()
    gross_weight = request.form.get('gross_weight').upper()
    tare_weight = request.form.get('tare_weight').upper()
    net_weight = request.form.get('net_weight').upper()
    invoice_no = request.form.get('invoice_no').upper()
    eway_bill_no = request.form.get('eway_bill_no').upper()
    # container_no = request.form.get('container_no').upper()
    arrival_time = request.form.get('arrival_time').upper()
    departure_time = request.form.get('departure_time').upper()
    remark = request.form.get('remark').upper()
    booking_no = request.form.get('booking_no').upper()

    # Debug print
    print(f"Received vehicle number: {vehicle_no}")
    print(f"Received vehicle number: {date}")
    print(f"Received vehicle number: {consignment_no}")
    print(f"Received vehicle number: {from_location}")

    # Excel file location (do not change)
    Excel_file = r"C:\Users\steve\Desktop\Aqua trans Web\ExcelSheets\LR.xlsx" 
    pdf_save = r"C:\Users\steve\Desktop\Aqua trans Web\pdf" 
    sheet = "Sheet1"

    # Updates for the Excel file
    updates = {
        "C8": vehicle_no,
        "E8": date,
        "I8": consignment_no,  # Use the new consignment number
        "B9": from_location,
        "F9": to_location,
        "A11": consignor,
        "E11": consignee,
        "A15": cargo_description,
        "D15": quantity,
        "F15": gross_weight,
        "F16": tare_weight,
        "F17": net_weight,
        "H17": invoice_no,
        "H18": eway_bill_no,
        # "B19": container_no, 
        # "B20": seal_no,
        "B21": arrival_time,
        "B23": departure_time,
        "H19": remark,
        "H16": booking_no

    }

    try:
        # Update Excel and convert to PDF
        # update_excel(Excel_file, sheet, updates)
        # excel_to_pdf(Excel_file, pdf_save)
        last_converted_file = os.path.join(pdf_save, "converted_file.pdf")
        
    except Exception as e:
        print(f"Error during Excel to PDF conversion: {e}")
        return "An error occurred during file processing!", 500

    return render_template('pdfdownload.html', last_converted_file=last_converted_file)

# File download route
@app.route("/download")
def download():
    global last_converted_file  # Access the global variable

    if last_converted_file and os.path.exists(last_converted_file):
        return send_file(last_converted_file, as_attachment=True)
    else:
        return "File not found or not generated yet!", 404

if __name__ == "__main__":
    app.run(debug=True)
