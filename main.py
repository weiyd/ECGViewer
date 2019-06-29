from ECGXMLViewer.data_access.ecg_access import ECGData

if __name__ == '__main__':
    ecg = ECGData('data/72612.xml')
    print(ecg.Data)
