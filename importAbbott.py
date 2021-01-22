import csv
import datetime
class AbbotImport():
    def __init__(self, *args, **kwargs):
        self.abDict= {}
        self.abb_Dict = {}
    def getabbotData(self, fileName):
        with open(fileName, newline='') as csvfile:
          reader = csv.reader(csvfile, delimiter=chr(28), lineterminator=chr(30))
          self.abDict ={rows[1]:rows[2]for rows in reader}
        return self.abDict
    def mode(self, fileName):
        modeclass = AbbotImport()
        mode = modeclass.getabbotData(fileName)
        self.abb_Dict = {
                        'name_given':mode.get('name_given', 'Not Given'),
                        'name_family':mode.get('name_family', 'Not Given'),
                        'followup_physician':mode.get('Follow-up Physician', '-'),
                        'sess_date':mode.get('Session Timestamp'),
                        'type':mode.get('type', '-'),
                        'model':mode.get('Device Model Number', '-'),
                        'device_name':mode.get('Device Model Name','-'),
                        'serial':mode.get('Device Serial Number', '-'),
                        'mfg':'Abbot',

                        ###### diagnostics
                        'ra_percent_paced':mode.get('Event Histogram Percent Paced In Atrium', '0'), # ra pacing percentage
                        'rv_percent_paced':mode.get('Event Histogram Percent Paced In Ventricle', '0'), # rv pacing percentage
                        'lv_percent_paced':mode.get('', '0'), # LV pacing percentage
                        'biv_percent_paced':mode.get('Percentage Biventricular Pacing Limit', '0'), # biventricular pacing percentage

                        
                        ####### arrhythmia log
                        'at_burden':mode.get('', '0'), #at/af burden in pecentage form
                        'ataf_reset':mode.get('Total Number of AT/AF Episodes Since Last Cleared', '0'),
                        'ataf_total'
                        'total_pac_count'
                        'total_pvc_count'
                        'nsvt_counter_life'
                        'vt_counter_life'
                        'vt1_counter_life'
                        'vf_counter_life'
                        'nsvt_counter_reset':mode.get('LFDA Non Sustained Episodes', '0'),
                        'vt_counter_reset'
                        'vt1_counter_reset'
                        'vf_counter_reset'

                        ####### test results
                        # RA
                        'ra_test_sense':mode.get('Atrial Signal Amplitude', '0'),
                        'ra_test_threshold':mode.get('A. Capture Test Threshold Amplitude', '0'),
                        'ra_test_pulsewidth':mode.get('A. Capture Test Pulse Width', '0'),
                        'ra_test_impedance':mode.get('Atrial Pacing Lead Impedance', '0'),
                        # RV
                        'rv_test_sense':mode.get('Ventricular Signal Amplitude', '0'),
                        'rv_test_threshold':mode.get('RV. Capture Test Threshold Amplitude', '0'),
                        'rv_test_pulsewidth':mode.get('RV. AutoCapture Capture Test Pulse Width', '0'),
                        'rv_test_impedance':mode.get('RV Pacing Lead Impedance', '0'),
                        'hv_test_impedance':mode.get('HV Lead Impedance','0'),                      
                        
                        # LV
                        'lv_test_threshold':mode.get('LV. AutoCapture Capture Test Pulse Amplitude (threshold)', '0'),
                        'lv_test_pulsewidth':mode.get('LV. AutoCapture Capture Test Pulse Width', '0'),
                        'lv_test_impedance':mode.get('LV Pacing Lead Impedance', '0'),

                        ######  Settings
                        'mode':mode.get('Mode', '-'),                       
                        'lowrate':mode.get('Base Rate', '0'),
                        'max_tracking_rate':mode.get('Maximum Tracking Rate', '0'),
                        'max_sensor_rate':mode.get('Maximum Sensor Rate', '0'), ##############################################
                        
                        'sensed_AV_delay':mode.get('Sensed AV Delay', '0'),
                        'ra_amplitude':mode.get('Atrial Pulse Amplitude', '0'),
                        'ra_pulsewidth':mode.get('Atrial Pulse Width', '0'),
                        'ra_pace_polarity':mode.get('A Pace Polarity', '-'),
                        'ra_sense_polarity':mode.get('A Sense Polarity', '-'),
                        'ra_sensitivity':mode.get('', '0'),
                        'rv_amplitude':mode.get('RV Pulse Amplitude', '0'),
                        'rv_pulsewidth':mode.get('RV Pulse Width', '0'),
                        'rv_sensitivity':mode.get('', '0'),
                        'rv_pace_polarity':mode.get('V Pace Polarity', '-'),
                        'rv_sense_polarity':mode.get('V Sense Polarity', '-'),
                        'lv_amplitude':mode.get('LV Pulse Amplitude', '0'),
                        'lv_pulsewidth':mode.get('LV Pulse Width', '0'),
                        'lv_polarity':mode.get('', '-'),










                        
                        'ra_polarity':mode.get('A Pace Polarity', '-'),
                        'ra_pulsewidth':mode.get('Atrial Pulse Width', '0'),

                        'rv_sense':mode.get('Ventricular Signal Amplitude', '0'),
                        'rv_polarity':mode.get('V Pace Polarity', '-'),
                        'rv_threshold':mode.get('RV. Capture Test Threshold Amplitude', '0'),
                        'rv_pulsewidth':mode.get('RV Pulse Width', '0'),
                        'rv_impedance':mode.get('Ventricular Pacing Lead Impedance', '0'),
                        'hv_impedance':mode.get('HV Lead Impedance', '0'),

                        'lv_sense':mode.get('', '0'),
                        'lv_impedance':mode.get('LV Pacing Lead Impedance', '0'),
                        'lv_threshold':mode.get('', '0'),
                        'lv_amplitude':mode.get('lv_amplitude', '0'),
                        'lv_pulsewidth':mode.get('lv_pulsewidth', '0'),
                        'lv_polarity':mode.get('', '-'),

                        ######  Battery
                        'batt_voltage':mode.get('batt_voltage', '0'),
                        'batt_remaining':mode.get('batt_remaining', '-'),
                        'batt_status':mode.get('Longevity Estimate', '-'),
                        'batt_chrge_time':mode.get('', '0')}
        return self.abb_Dict