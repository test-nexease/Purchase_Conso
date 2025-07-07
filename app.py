import streamlit as st
import pandas as pd

# Replace file selection with Streamlit file uploader widgets
st.title("Upload Excel files for each dataset")

file_8235 = st.file_uploader("Upload Excel file for SAP-8235", type=["xlsx"])
file_8223 = st.file_uploader("Upload Excel file for M3-8223", type=["xlsx"])
file_8236 = st.file_uploader("Upload Excel file for M3-8236", type=["xlsx"])
file_8224_8225_8229 = st.file_uploader("Upload Excel file for SAP-8224_8225_8229", type=["xlsx"])
file_Aurora_8226_8297 = st.file_uploader("Upload Excel file for Aurora-8226-8297", type=["xlsx"])
file_BOE_8223 = st.file_uploader("Upload Excel file for BOE 8223", type=["xlsx"])
file_BOE_8226 = st.file_uploader("Upload Excel file for BOE 8226", type=["xlsx"])

# Proceed only if all files are uploaded
if all([file_8235, file_8223, file_8236, file_8224_8225_8229, file_Aurora_8226_8297, file_BOE_8223, file_BOE_8226]):
    # Read the uploaded Excel files
    df_8235 = pd.read_excel(file_8235, sheet_name='Sheet1')
    df_8223 = pd.read_excel(file_8223, sheet_name='Sheet1')
    df_8236 = pd.read_excel(file_8236, sheet_name='Sheet1')
    df_8224_8225_8229 = pd.read_excel(file_8224_8225_8229, sheet_name='Sheet1')
    df_Aurora_8226_8297 = pd.read_excel(file_Aurora_8226_8297, sheet_name='Sheet1')
    df_BOE_8223 = pd.read_excel(file_BOE_8223, sheet_name='Sheet1')
    df_BOE_8226 = pd.read_excel(file_BOE_8226, sheet_name='Sheet1')


    df_8223_8236 = pd.concat([df_8223, df_8236], ignore_index=True)
    df_BOE_8226['Document Type'] = 'Bill of Entry'
    df_BOE_8226['ERP'] = 'AURORA'
    df_BOE_8226['Entity Code'] = '8226'

    # %%
    df_8235['ERP'] = 'SAP UGD'

    df_8235['Document Type'] = df_8235['Document Type'].apply(lambda x: 'Credit Note' if x == 'KG' else 'Invoice')
    df_8235['Goods/Service'] = df_8235['Goods/Service'].apply(lambda x: 'Goods' if x == 'G' else 'Service')
    df_8235['Reverse Charge Flag'] = df_8235['Reverse Charge Flag'].apply(lambda x: 'Y' if x == 'X' else 'N')
    df_8235['Deductible/Non Deductible'] = df_8235['Deductible/Non Deductible'].apply(lambda x: 'Ineligible' if x == 'Non-Deductible' else 'Eligible')
    df_8235.loc[df_8235['Document Type'] == 'Credit Note', 'Doc.Base Value in LC'] *= -1
    df_8235.loc[df_8235['Document Type'] == 'Credit Note', 'CGST Amount'] *= -1
    df_8235.loc[df_8235['Document Type'] == 'Credit Note', 'SGST Amount'] *= -1
    df_8235.loc[df_8235['Document Type'] == 'Credit Note', 'IGST Amount'] *= -1
    df_8235.loc[df_8235['Document Type'] == 'Credit Note', 'TDS Amount'] *= -1
    df_8235.loc[df_8235['Document Type'] == 'Credit Note', 'TDS Amount for Goods'] *= -1
    df_8224_8225_8229['Entity Code'] = df_8224_8225_8229['Company Code']
    df_8224_8225_8229['GST Comments'] = df_8224_8225_8229['GST Remarks']
    df_8235['GST Comments'] = df_8235['GST Remarks']
    df_8235.loc[df_8235['Tax code description'].str.contains('Import', na=False), 'Document Type'] = 'Bill of Entry'



    # %%
    df_8224_8225_8229['ERP'] = 'SAP SMRT'
    df_8224_8225_8229['HSN/SAC'] = df_8224_8225_8229['HSN/SAC'].astype(str)
    df_8224_8225_8229['HSN/SAC'] = df_8224_8225_8229['HSN/SAC'].fillna('Na')
    df_8224_8225_8229['Document Type'] = df_8224_8225_8229['Document Type'].apply(lambda x: 'Credit Note' if x == 'KG' else 'Invoice')
    df_8224_8225_8229['Goods/Service'] = df_8224_8225_8229['Goods/Service'].apply(lambda x: 'Goods' if x == 'G' else 'Service')
    df_8224_8225_8229['Reverse Charge Flag'] = df_8224_8225_8229['Reverse Charge Flag'].apply(lambda x: 'Y' if x == 'X' else 'N')
    df_8224_8225_8229['Deductible/Non Deductible'] = df_8224_8225_8229['Deductible/Non Deductible'].apply(lambda x: 'Ineligible' if x == 'Non-Deductible' else 'Eligible')
    df_8224_8225_8229.loc[df_8224_8225_8229['Document Type'] == 'Credit Note', 'Doc.Base Value in LC'] *= -1
    df_8224_8225_8229.loc[df_8224_8225_8229['Document Type'] == 'Credit Note', 'CGST Amount'] *= -1
    df_8224_8225_8229.loc[df_8224_8225_8229['Document Type'] == 'Credit Note', 'SGST Amount'] *= -1
    df_8224_8225_8229.loc[df_8224_8225_8229['Document Type'] == 'Credit Note', 'IGST Amount'] *= -1
    df_8224_8225_8229.loc[df_8224_8225_8229['Document Type'] == 'Credit Note', 'TDS Amount'] *= -1
    df_8224_8225_8229.loc[df_8224_8225_8229['Document Type'] == 'Credit Note', 'TDS Amount for Goods'] *= -1
    df_8224_8225_8229.loc[df_8224_8225_8229['Tax code description'].str.contains('Import', na=False), 'Document Type'] = 'Bill of Entry'



    # %%
    df_8223_8236['ERP'] = 'M3'
    def reformat_date(date_str):
        # Ensure the string is zero-padded to 8 characters
        date_str = date_str.zfill(8)
        return f"{date_str[:4]}-{date_str[4:6]}-{date_str[6:]}" if len(date_str) == 8 else date_str
    date_columns = [
        'Invoice Date', 'GRN Date', 'Document Date', 'PO DATE',
        'Fin.Post/Process Dt.'
    ]
    for col in date_columns:
        df_8223_8236[col] = df_8223_8236[col].astype(str).apply(reformat_date)
    df_8223_8236['Document Type'] = df_8223_8236['Tax base amount'].apply(lambda x: 'Credit Note' if x < 0 else 'Invoice')
    df_8223_8236['Goods/Service'] = df_8224_8225_8229['Goods/Service'].apply(lambda x: 'Goods' if x == 'G' else 'Service')
    df_8223_8236['ITC Avail.Type'] = df_8223_8236['ITC Avail.Type'].apply(lambda x: 'Ineligible' if x == 'Ineligible Credit' else 'Eligible')
    df_8223_8236['Supplier category'] = df_8223_8236['Supplier category'].apply(lambda x: 'Import' if x == 'IMP' else 'Domestic')
    dict ={
        "AU" : "MILTON",
        "IN" : "INDIA",
        "FI" : "TAMPERE",
        "BT" : "GALING",
        "IE" : "IRELAND",
        "FR" : "FRANCE",
        "SE" : "SANDVIKEN",
        "GB" : "HALESOWEN",
        "AT" : "ZELTWEG",
        "IE" : "DUBLIN",
        "ZA" : "South Africa",
        "DE" : "Germany",
        "CN" : "China"
    }
    df_8223_8236['Country Code'] = df_8223_8236['Country Code'].replace(dict)
    df_8223_8236['Invoice Number'] = df_8223_8236['Invoice Number'].str.strip()
    df_8223_8236 = df_8223_8236.drop('GRN Number',axis=1)
    df_8223_8236['GST Comments'] = df_8223_8236['GST Remarks']


    # %%
    df_Aurora_8226_8297['ERP'] = 'AURORA'
    df_Aurora_8226_8297['HSN/SAC'] = df_Aurora_8226_8297['HSN/SAC'].astype(str)
    df_Aurora_8226_8297['Goods/Service'] = df_Aurora_8226_8297['Service Indicator'].apply(lambda x: 'Service' if x == 1 else 'Goods')
    df_Aurora_8226_8297['Company'] = df_Aurora_8226_8297['Company'].apply(lambda x: '8226' if x == 'IN' else '8297')
    df_Aurora_8226_8297['Transaction Type'] = df_Aurora_8226_8297['Transaction Type'].apply(lambda x: 'Invoice' if x == 'Invoice' else 'Credit Note')
    df_Aurora_8226_8297['Customer Bill Addr'] = df_Aurora_8226_8297[['Party Address1', 'Party Address 2', 'Party Address 4']].agg(
        lambda x: ' '.join(x.dropna().astype(str)), axis=1).str.strip()
    df_Aurora_8226_8297['Reverse Charge'] = df_Aurora_8226_8297['Reverse Charge'].apply(lambda x: 'N' if x == 'No' else 'Y')
    df_Aurora_8226_8297["Invoice ID"] = df_Aurora_8226_8297["Invoice ID"].astype(str)
    df_Aurora_8226_8297["POS"] = df_Aurora_8226_8297["Party State"]




    # %%
    mapping_8235 = {
        "SAP Key/ Invoice ID/ Voucher no." : "Document Number",
        "Entity Code": "Company Code",
        "Accounting Date": "Posting Date",
        "Invoice Number": "Invoice Number",
        "Invoice Date": "Invoice Date",
        "Supplier GSTIN": "Supplier GSTIN",
        "Supplier Name": "Supplier Name",
        "POS": "POS State",
        "Item ID": "Item Code",
        "Item Description": "Item Description",
        "Quantity": "ITEM Quantity",
        "Taxable Value": "Doc.Base Value in LC",
        "CGST Rate": "CGST RATE",
        "CGST Amount": "CGST Amount",
        "SGST Rate": "SGST RATE",
        "SGST Amount": "SGST Amount",
        "IGST Rate": "IGST RATE",
        "IGST Amount": "IGST Amount",
        "TDS Section": "TDS SECTION",
        "TDS RATE": "TDS RATE",
        "TDS Amount": "TDS Amount",
        "TDS Rate for Goods": "TDS Rate for Goods",
        "TDS Amount for Goods": "TDS Amount for Goods",
        "Eligible/Ineligible": "Deductible/Non Deductible",
        "Reverse Charge Flag": "Reverse Charge Flag",
        "GRN Number": "GRN Number",
        "GRN Date": "GRN Date",
        "Customer Bill Addr": "Supplier Address",
        "Customer Bill City": "Supplier City",
        "Customer State Code": "Supplier State Code",
        "Vendor PAN": "PAN",
        "SMRT GSTIN": "Recipient_GSTIN"
    }
    mapping_8224_8225_8229 = {
        "SAP Key/ Invoice ID/ Voucher no." : "Document Number",
        "Accounting Date": "Posting Date",
        "Supplier GSTIN": "Supplier GSTIN",
        "Supplier Name": "Supplier Name",
        "POS": "POS State",
        "Item Code": "Item ID",
        "Item Description": "Item Description",
        "ITEM Quantity": "Quantity",
        "Taxable Value": "Doc.Base Value in LC",
        "CGST Rate": "CGST RATE",
        "CGST Amount": "CGST Amount",
        "SGST Rate": "SGST RATE",
        "SGST Amount": "SGST Amount",
        "IGST Rate": "IGST RATE",
        "IGST Amount": "IGST Amount",
        "TDS Section": "TDS SECTION",
        "TDS RATE": "TDS RATE",
        "TDS Amount": "TDS Amount",
        "TDS Rate for Goods": "TDS Rate for Goods",
        "TDS Amount for Goods": "TDS Amount for Goods",
        "Eligible/Ineligible": "Deductible/Non Deductible",
        "Reverse Charge Flag": "Reverse Charge Flag",
        "Customer Bill Addr": "Supplier Address",
        "Customer Bill City": "Supplier Address",
        "Customer State Code": "Supplier City",
        "Vendor PAN": "PAN",
        "SMRT GSTIN": "Recipient_GSTIN"
    }
    df_8223_8236['POS.'] = df_8223_8236['POS']
    mapping_8223_8236 = {
        "SAP Key/ Invoice ID/ Voucher no." : "Document Number",
        "Entity Code": "Company Code",
        "Document Type": "Document Type",
        "Accounting Date": "Document Date",
        "Invoice Number": "Invoice Number",
        "Invoice Date": "Invoice Date",
        "Supplier GSTIN": "Supplier GSTIN",
        "Supplier Name": "Supplier Name",
        "Item ID": "Item Code",
        "Item Description": "Item Description",
        "Quantity": "Quantity",
        "Goods/Service": "Goods/Service",
        "HSN/SAC": "HSN/SAC",
        "Taxable Value": "Tax base amount",
        "CGST Rate": "CGST Rate",
        "CGST Amount": "CGST Amount",
        "SGST Rate": "SGST Rate",
        "SGST Amount": "SGST Amount",
        "IGST Rate": "IGST Rate",
        "IGST Amount": "IGST Amount",
        "TDS Section": "TDS Section",
        "TDS RATE": "TDS Rate",
        "TDS Amount": "TDS Amount",
        "TDS Rate for Goods": "TDS Rate for Goods",
        "TDS Amount for Goods": "TDS Amount for Goods",
        "Eligible/Ineligible": "ITC Avail.Type",
        "Reverse Charge Flag": "Reverse Charge Flag",
        "GRN Number": "Cost Center",
        "GRN Date": "GRN Date",
        "Customer Bill Addr": "Supplier Address",
        "Customer Bill City": "Country Code",
        "Party Country": "Country Code",
        "Vendor PAN": "PAN NUMBER.1",
        "SMRT GSTIN": "Recipient_GSTIN",
        "POS." : "Customer State Code",
        "PO Number" : "Purchase Order No.",
        "Stock ID" : "New-Stock ID"
    }
    mapping_Aurora = {
        "SAP Key/ Invoice ID/ Voucher no." : "Invoice ID",
        "Entity Code": "Company",
        "Document Type": "Transaction Type",
        "Accounting Date": "Accounting Date",
        "Invoice Number": "Supplier Invoice No",
        "Invoice Date": "Document Date",
        "Supplier GSTIN": "Party Tax ID",
        "Supplier Name": "Party Name",
        "Item ID": "Item ID",
        "Item Description": "Item Description",
        "Quantity": "Quantity",
        "Goods/Service": "Goods/Service",
        "HSN/SAC": "HSN/SAC",
        "Taxable Value": "Taxable Value",
        "CGST Amount": "CGST",
        "SGST Amount": "SGST",
        "IGST Amount": "IGST",
        "TDS Rate for Goods": "TCS Rate",
        "TDS Amount for Goods": "TCS Amount",
        "Eligible/Ineligible": "ITC Eligibility",
        "Reverse Charge Flag": "Reverse Charge",
        "GRN Number": "GRN Number",
        "GRN Date": "GRN Date",
        "Classification": "Classification",
        "Customer Bill City": "Party Address 4",
        "Customer State Code": "Party State",
        "Party Country": "Party Country",
        "Vendor PAN": "Party Country Tax ID",
        "SMRT GSTIN": "GSTIN",
        "GST Comments":"Input/ Input Service/ Capital Goods",
        "Supplier NO.":"Party ID",
        "PO Number" : "External Ref. No.",
        "Stock ID" : "Receiving Location",
        "CGST Rate" : "Tax Rate1",
        "SGST Rate" : "Tax Rate 2",
        "IGST Rate" : "Tax Rate 3"
    }
    mapping_8235_inverted = {v: k for k, v in mapping_8235.items()}
    mapping_8224_8225_8229_inverted = {v: k for k, v in mapping_8224_8225_8229.items()}
    mapping_8223_8236_inverted = {v: k for k, v in mapping_8223_8236.items()}
    mapping_Aurora_inverted = {v: k for k, v in mapping_Aurora.items()}
    df_8235.rename(columns=mapping_8235_inverted, inplace=True)
    df_8224_8225_8229.rename(columns=mapping_8224_8225_8229_inverted, inplace=True)
    df_8223_8236.rename(columns=mapping_8223_8236_inverted, inplace=True)
    df_Aurora_8226_8297.rename(columns=mapping_Aurora_inverted, inplace=True)
    required_columns = [
        "SAP Key/ Invoice ID/ Voucher no.",
        "ERP",
        "Entity Code",
        "Document Type",
        "Fiscal Period",
        "Fiscal Year",
        "Accounting Date",
        "Invoice Number",
        "Invoice Date",
        "Supplier GSTIN",
        "Supplier NO.",
        "Supplier Name",
        "POS",
        "Item ID",
        "Item Description",
        "Quantity",
        "Goods/Service",
        "HSN Goods/Service",
        "HSN/SAC",
        "Taxable Value",
        "CGST Rate",
        "CGST Amount",
        "SGST Rate",
        "SGST Amount",
        "IGST Rate",
        "IGST Amount",
        "Total Tax",
        "Invoice Total",
        "TDS Section",
        "TDS RATE",
        "TDS Amount",
        "TDS Rate for Goods",
        "TDS Amount for Goods",
        "TDS Code",
        "MSMED Number 1",
        "MSMED Number 2",
        "Tax code description",
        "Eligible/Ineligible",
        "Reverse Charge Flag",
        "Input/ Input Service/ Capital Goods",
        "PO Number",
        "GRN Number",
        "GRN Date",
        "Stock ID",
        "Classification",
        "Customer Bill Addr",
        "Customer Bill City",
        "Customer State Code",
        "Party Country",
        "Vendor PAN",
        "SMRT GSTIN",
        "BI No",
        "BOE Number",
        "BOE Date",
        "Stock Transfer",
        "Orignal Inv. Date",
        "Orignal Invoice No",
        "Orignal Supp. GSTIN",
        "GST Comments"
    ]
    dataframes = [df_8235, df_8223_8236, df_8224_8225_8229, df_Aurora_8226_8297]

    #Ensure all DataFrames have the same columns
    processed_dfs = []

    for df in dataframes:
        #Ensure columns match required_columns
        columns_to_drop = [col for col in df.columns if col not in required_columns]
        if columns_to_drop:
            df.drop(columns=columns_to_drop, inplace=True)
        
        missing_columns = [col for col in required_columns if col not in df.columns]
        if missing_columns:
            for col in missing_columns:
                df[col] = pd.NA  # Or another default value if preferred

        #Reorder columns to match required_columns order
        df = df[required_columns]
        
        # Append processed DataFrame to the list
        processed_dfs.append(df)
    df_8235 = processed_dfs[0]
    df_8223_8236 = processed_dfs[1]
    df_8224_8225_8229 = processed_dfs[2]
    df_Aurora_8226_8297 = processed_dfs[3]

    # %%
    df = pd.concat(dataframes,ignore_index=True)


    # %%
    df_BOE_8226['Document Type.'] = df_BOE_8226['Document Type']
    df_BOE_8223["Document Type"] = "Bill of Entry"
    df_BOE_8223['Entity Code'] = "8223"
    df_BOE_8223['ERP'] = "M3"
    df_BOE_8223['Document Type.'] = "Bill of Entry"
    df_BOE_8223['Classification'] = df_BOE_8223['Document Type']
    df_BOE_8226 = df_BOE_8226.drop('Supplier Name',axis=1)

    # %%
    mapping_BOE_8226 = {
        "DOCREF01": "SAP Key/ Invoice ID/ Voucher no.",
        "Invoice No": "Invoice Number",
        "Date": "Invoice Date",
        "IMPORTER NAME": "Supplier Name",
        "Item Code": "Item ID",
        "Fiscal Period": "Fiscal Period",
        "Fiscal Year": "Fiscal Year",
        "Description": "Item Description",
        "QUANTITY": "Quantity",
        "CTH": "HSN/SAC",
        "Assessable Value": "Taxable Value",
        "IGST - Amount": "IGST Amount",
        "GST TYPE": "Classification",
        "GSTIN/TYPE": "SMRT GSTIN",
        "BE No": "BOE Number",
        "BE Date": "BOE Date",
        "Document Type.": "Stock Transfer"
    }
    mapping_BOE_8223 = {
        "Voucher Number": "SAP Key/ Invoice ID/ Voucher no.",
        "ERP": "ERP",
        "Entity Code": "Entity Code",
        "Document Type": "Document Type",
        "Fiscal Period": "Fiscal Period",
        "Fiscal Year": "Fiscal Year",
        "Custom Duty": "Taxable Value",
        "IGST": "IGST Amount",
        "Document Type.": "Input/ Input Service/ Capital Goods",
        "GSTIN": "SMRT GSTIN",
        "BI No.": "BI No",
        "BOE No.": "BOE Number",
        "BOE Date": "BOE Date"
    }
    df_BOE_8226.rename(columns=mapping_BOE_8226,inplace=True)
    df_BOE_8223.rename(columns=mapping_BOE_8223,inplace=True)
    datarame = [df_BOE_8226,df_BOE_8223]
    processed_df = []

    for df1 in datarame:
        # Ensure columns match required_columns
        columns_to_drop = [col for col in df1.columns if col not in required_columns]
        if columns_to_drop:
            df1.drop(columns=columns_to_drop, inplace=True)
        
        missing_columns = [col for col in required_columns if col not in df1.columns]
        if missing_columns:
            for col in missing_columns:
                df1[col] = pd.NA  # Or another default value if preferred

        # Reorder columns to match required_columns order
        df1 = df1[required_columns]
        
        # Append processed DataFrame to the list
        processed_df.append(df1)


    # %%
    df_BOE_8226 = processed_df[0]
    df_BOE_8223 = processed_df[1]
    df1 = pd.concat(datarame,ignore_index=True)

    # %%
    df1 = df1[required_columns]
    result = pd.concat([df, df1], ignore_index=True)
    result = result[required_columns]

    # %%
    result['Accounting Date'] = pd.to_datetime(result['Accounting Date']).dt.strftime('%d-%m-%Y')
    result['Invoice Date'] = pd.to_datetime(result['Invoice Date']).dt.strftime('%d-%m-%Y')


    # %%
    result.loc[result['Fiscal Period'].isna() & result['Accounting Date'].notna(), 'Fiscal Period'] = result['Accounting Date'].str[3:5]
    result.loc[result['Fiscal Year'].isna() & result['Accounting Date'].notna(), 'Fiscal Year'] = result['Accounting Date'].str[6:10]
    #result["Fiscal Period"] = result["Fiscal Period"].astype(int)
    result['HSN Goods/Service'] = result['HSN/SAC'].apply(
        lambda x: 'Service' if isinstance(x, str) and x.startswith(('99', '1000')) else 'Goods'
    )


    # %%
    result.loc[result['Orignal Invoice No'].notna() & (result['Orignal Invoice No'] != ''), 'Document Type'] = 'Credit Note'
    credit_note_condition = result['Document Type'].str.contains('Credit Note', case=False, na=False)

    # List of columns that need to be modified
    columns_to_modify = ['Taxable Value', 'CGST Amount', 'SGST Amount', 'IGST Amount', 'Total Tax', 'Invoice Total']

    # Ensure that the columns are numeric (convert if necessary)
    for column in columns_to_modify:
        # Convert the column to numeric, forcing errors to NaN
        result[column] = pd.to_numeric(result[column], errors='coerce')
        
        # Apply the condition and replace positive values with negative ones in the specified columns
        result.loc[credit_note_condition, column] = result.loc[credit_note_condition, column].apply(lambda x: -x if pd.notna(x) and x > 0 else x)


    # %%
    # Convert relevant columns to numeric, coercing errors to NaN
    result['CGST Amount'] = pd.to_numeric(result['CGST Amount'], errors='coerce')
    result['SGST Amount'] = pd.to_numeric(result['SGST Amount'], errors='coerce')
    result['IGST Amount'] = pd.to_numeric(result['IGST Amount'], errors='coerce')
    result['Taxable Value'] = pd.to_numeric(result['Taxable Value'], errors='coerce')

    # # Calculate CGST Rate
    # result['CGST Rate'] = (result['CGST Amount'] / result['Taxable Value'].replace(0, np.nan)) * 100
    # result['CGST Rate'] = np.where(result['CGST Rate'] % 1 == 0, result['CGST Rate'].round(0), result['CGST Rate'].round(2))

    # # Calculate SGST Rate
    # result['SGST Rate'] = (result['SGST Amount'] / result['Taxable Value'].replace(0, np.nan)) * 100
    # result['SGST Rate'] = np.where(result['SGST Rate'] % 1 == 0, result['SGST Rate'].round(0), result['SGST Rate'].round(2))

    # # Calculate IGST Rate
    # result['IGST Rate'] = (result['IGST Amount'] / result['Taxable Value'].replace(0, np.nan)) * 100
    # result['IGST Rate'] = np.where(result['IGST Rate'] % 1 == 0, result['IGST Rate'].round(0), result['IGST Rate'].round(2))

    # Total Tax calculation
    result['Total Tax'] = result['CGST Amount'] + result['SGST Amount'] + result['IGST Amount']
    # Replace blank or missing values in 'HSN/SAC ' with 'Na'
    result['HSN/SAC'] = result['HSN/SAC'].fillna('Na')

    # Optionally, replace empty strings as well
    result['HSN/SAC'] = result['HSN/SAC'].replace('', 'Na')
    result['HSN/SAC'] = result['HSN/SAC'].replace('nan', 'Na')

    # If 'HSN/SAC ' is 'Na', replace 'HSN Goods/Service' with 'Na'
    result.loc[result['HSN/SAC'] == 'Na', 'HSN Goods/Service'] = 'Na'
    result.loc[result['HSN/SAC'] == 'nan', 'HSN Goods/Service'] = 'Na'



    import io

    buffer = io.BytesIO()
    with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
        result.to_excel(writer, index=False)
    buffer.seek(0)

    st.download_button(
        label="Download Excel File",
        data=buffer,
        file_name="cleaned_gst_data.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
