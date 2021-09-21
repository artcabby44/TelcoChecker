import itertools

globe_tm = ['917', '905', '906', '915', '916', '917', '926', '927', '935', '936', '937', '945', '953', '954', '955', '956', '965', '966', '967', '997', '996', '995', '994', '979', '978', '977', '975']
smart = ['908', '919', '920', '921', '928', '929', '961', '951', '949', '947', '939', '998', '999']
tnt = ['907', '909', '910', '912', '930', '950', '948', '946', '938']
sun = ['922', '923', '923', '925', '931', '932', '943', '942', '941', '940', '934', '934', '973', '974']

while True:
    prefix = str(input("Enter prefix: ex.915,924 enter 'exit' to quit \n "))
    if prefix == "exit":
        break
    else:
        network = ""
        
        for gl_tm in globe_tm: #iterate list
            if prefix in gl_tm:         #conditions
                network = "GLOBE"
        for sm in smart: #iterate list
            if prefix in sm:         #conditions
                network = "SMART"
        for tn in tnt: #iterate list
            if prefix in tn:         #conditions
                network = "TALK N TEXT"
        for sn in sun: #iterate list
            if prefix in sn:         #conditions
                network = "SUN"
        

        print(network) 


