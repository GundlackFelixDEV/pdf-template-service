PROFILE = {
    "reciepientsFullName": "Max Mustermann",
    "lastName": "Mustermann",
    "title": "Mr.",
    "reciepientsAddress": "Musterstraße 11",
    "zipCode": "123456",
    "city": "Musterhausen",
    "IBAN": "DE07123412341234123412"
}
NF_FORM = {
        "proc_agency": "USAG Grafenwoehr,<br>HQUSAG Grafenwoer,<br>Tax Relieve Office MWW,<br>Tax Reliev, Unit 2810",
        "ocr_OrderNr": "GR-NF1-189559",
        "ocr_ValidFrom": "09-2021",
        "ocr_ValidUntil": "09-2022",
}
INVOICE = {
    "TotalAmount": 119,
    "TotalRemonon": 105,
    "TotalRefund": 14,
    "InvoiceNr": "A-10000-01-2109-GR-NF1-189559.1",
    "Period": "September 2021",
    "Date": "1.10.2021"
}

RECEITS = [
    {
        "vendor": {
            "name": "Muster Vendor",
            "ustdid": "xxx-xxx-xxxxxx",
            "RemononID": "48483",
            "ocr_MerchantStreet": "Am He",
            "ocr_MerchantCity": "",
            "ocr_MerchantPostcode": ""
        },
        "TotalAmount": 119,
        "TotalRomonon": 105,
        "TotalRefund": 14,
    }
]

TESTINPUT = {
    "title": f"Sammelrechnung {INVOICE['InvoiceNr']}",
    "profile": PROFILE,
    "nf_form": NF_FORM,
    "invoice": INVOICE,
    "receits": RECEITS
}